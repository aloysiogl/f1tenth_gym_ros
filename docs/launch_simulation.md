# Start simulation

Runs on docker a simulated f1tenth car. There are two docker images that should be created `f1tenth_gym` which can be build from this repo and `simulator` which is an image capable of running ros melodic with vnc, a suitable base can be found at [https://github.com/aloysiogl/docker-ros-vnc](https://github.com/aloysiogl/docker-ros-vnc). 

Run on separate terminals
```
run_simulator.sh
docker.sh
```

The first one starts the simulator image, used to install dependencies, run rviz etc. The other one starts the simulated f1tenth instances on the given environment (both should've been built prior to this operation).