# Real robot

## Connect to robot and be able to read topics

On the vehicle:

```bash
export ROS_MASTER_URI={vehicle_ip} # with http:// before and the port 11311 in the end
export ROS_HOST={vehicle_ip}
export ROS_IP={vehicle_ip}
```

On the laptop:

```bash
export ROS_MASTER_URI={vehicle_ip} # with http:// before and the port 11311 in the end
export ROS_HOST={laptop_ip}
export ROS_IP={vehicle_ip} # TODO: try without that
```

In rviz see the frame name (maybe it's should be laser)

## Publish the odom topic

Go to `racecar/racecar/config/racecar-v2/vesc.yaml` and change the following:

```yaml
# publish odom to base link tf
vesc_to_odom/publish_tf: true
```

## For mapping

You'll probably need to publish the `odom` topic (follow instructions above).

In the same line (at least for gmapping) you need to disable sim time, as the sleep to update the `odom` tf will be helted if you don't update the sim time, to do so, for gmapping go to `catkin_ws/src/src/slam_gmapping/gmapping/launch/slam_gmapping_pr2.launch` and change:

```xml
slam_gmapping_pr2.launch

<param name="use_sim_time" value="false"/>
```

In the same file, make sure that you set the right frames:

```xml
slam_gmapping_pr2.launch

<!-- # Remove this line -->
<remap from="scan" to="base_scan"/>

<!-- # Add this line only -->
<param name="base_frame" value="base_link"/>
```
