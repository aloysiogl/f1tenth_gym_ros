# Mapping

## Using hector slam

### Install

Should be ok with just using apt

```
sudo apt install ros-melodic-hector-slam
```

Otherwise look at the repository [https://github.com/tu-darmstadt-ros-pkg/hector_slam](https://github.com/tu-darmstadt-ros-pkg/hector_slam).

### Configuring

In `catkin_ws/src/src/hector_slam/hector_mapping/launch/mapping_default.launch` make sure that base_frame and odom_frame both point to a frame which is provided by the car simulation, the scans should be provided in the scan topic. 
```
mapping_default.launch

<arg name="base_frame" default="ego_racecar/laser"/>
<arg name="odom_frame" default="ego_racecar/laser"/>
```

### Run mapping

You can either run the simulation or a bag file containing the simulation (see insctructions for each case). Launch hector slam + visualization with the following command:

```
roslaunch hector_slam_launch tutorial.launch
```

## Using gmapping

### Install

Better to install directly from the repo [https://github.com/ros-perception/slam_gmapping.git](https://github.com/ros-perception/slam_gmapping.git).

First use `sudo apt install ros-melodic-slam-gmapping` (preferred) or `sudo apt install ros-melodic-gmapping` to install the dependencies.

```
# Reminder (create catkin_ws)
mkdir -p catkin_ws/src
cd catkin_ws/src
source /opt/ros/<DISTRO>/setup.bash
catkin_init_workspace

git clone https://github.com/ros-perception/slam_gmapping.git

cd ..
catkin_make

source devel/setup.bash
```

You might also need `rosmake gmapping` (probably need to be in the same dir). Make sure you can roscd to the package.

In the end source your environment: `source devel/setup.bash`.

### Configuration

On gmapping in `catkin_ws/src/src/slam_gmapping/gmapping/launch/slam_gmapping_pr2.launch` you should configure remappings to base_frame and odom, it listens to scan under the topic scan, so you'll most likely remove the remapping as shown below:
```
slam_gmapping_pr2.launch

# Remove this line
<remap from="scan" to="base_scan"/>

# Add those
<param name="base_frame" value="ego_racecar/laser_model"/>
<param name="odom" value="ego_racecar/laser_model"/>

```

### Run mapping

You can either run the simulation or a bag file containing the simulation (see insctructions for each case). Launch mapping with the following command:

```
roslaunch gmapping slam_gmapping_pr2.launch
```

Start rviz and display the map topic.

## Running simulation

### Running directly the car simulation

First, some configurations need to be set on the lauch files:

On hector slam in `catkin_ws/src/src/hector_slam/hector_slam_launch/launch`, put `use_sim_time` to false:
```
tutorial.launch

<param name="/use_sim_time" value="false"/>
```

On gmapping in `catkin_ws/src/src/slam_gmapping/gmapping/launch`, put `use_sim_time` to false:
```
slam_gmapping_pr2.launch

<param name="use_sim_time" value="false"/>
```

Start the car simulation (the dockerfile for f1tenth_gym) and disable the map server node:

```
rosnode kill map_server
```

### Runnig from a bag file

Record a run with `rosbag record -O [filename]`. And make sure to not record with `map_server` running. 

Play a record using `rosbag play [filename] --clock`. The clock option makes sure that the timestamps correspond to the current times. You might want to reduce the rate with the `-r` option. `use_sim_time` should be true (it is by default normally).

## Saving map

To save the map we rely on the `map_server` package using the command:

```
rosrun map_server map_saver −f [filename]
```
