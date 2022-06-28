sudo docker run -it -p 5901:5901 -p 6901:6901 -p 1025:22 \
  -v ~/aloysiogl/particle_filter:/home/ros/catkin_ws/src/particle_filter \
  -v ~/aloysiogl/f1tenth_gym_ros:/home/ros/catkin_ws/src/f1tenth_gym_ros \
  --net=host \
  simulator