# Real robot

## Connect to robot and be able to read topics

On the vehicle:

```
export ROS_MASTER_URI={vehicle_ip} # with http:// before and the port 11311 in the end
export ROS_HOST={vehicle_ip}
export ROS_IP={vehicle_ip}
```

On the laptop:

```
export ROS_MASTER_URI={vehicle_ip} # with http:// before and the port 11311 in the end
export ROS_HOST={laptop_ip}
export ROS_IP={vehicle_ip} # TODO: try without that
```

In rviz see the frame name (maybe it's should be laser)
