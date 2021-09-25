sudo apt-get update
sudo apt-get install curl
curl http://fishros.com/tools/install/rosdepc | bash 
sudo apt-get install ros-foxy-moveit
rosdepc install -r --from-paths . --ignore-src --rosdistro $ROS_DISTRO -y
sudo apt install ros-foxy-joint-state-controller
colcon build --cmake-args -DCMAKE_BUILD_TYPE=Release