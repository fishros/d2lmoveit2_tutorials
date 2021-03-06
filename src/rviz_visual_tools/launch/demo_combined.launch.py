# Copyright 2018 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

"""
<launch>

  <!-- Load Rviz -->
  <node name="$(anon rviz)" pkg="rviz" type="rviz" respawn="false"
        args="-d $(find rviz_visual_tools)/launch/demo.rviz" output="screen">
  </node>

  <!-- Fake transform from world origin to robot origin (base) -->
  <node pkg="tf" type="static_transform_publisher" name="base_to_world" args="0 0 0 0 0 0 /world /base 30" />

  <arg name="debug" default="false" />
  <arg unless="$(arg debug)" name="launch_prefix" value="" />
  <arg     if="$(arg debug)" name="launch_prefix" value="gdb --ex run --args" />

  <!-- Start demo -->
  <node name="rviz_visual_tools_demo"
        launch-prefix="$(arg launch_prefix)"
        pkg="rviz_visual_tools" type="demo" output="screen">
  </node>
</launch>
"""


def generate_launch_description():
    rviz_config = os.path.join(
        get_package_share_directory("rviz_visual_tools"), "launch", "demo.rviz"
    )

    return LaunchDescription(
        [
            Node(
                package="rviz2",
                node_executable="rviz2",
                arguments=["--display-config", rviz_config],
                output="screen",
            ),
            Node(
                package="tf2_ros",
                node_executable="static_transform_publisher",
                arguments=["0", "0", "0", "0", "0", "0", "/world", "/base"],
                output="screen",
            ),
            Node(
                package="rviz_visual_tools",
                node_executable="rviz_visual_tools_demo",
                output="screen",
            ),
            Node(
                package="rviz_visual_tools",
                node_executable="rviz_visual_tools_imarker_simple_demo",
                output="screen",
            ),
        ]
    )
