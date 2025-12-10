from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution, TextSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
               PathJoinSubstitution([
                    FindPackageShare('slam_toolbox'),
                    'launch',
                    'online_async_launch.py'
                ])
            ]),
        ),

       IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
               PathJoinSubstitution([
                    FindPackageShare('ldlidar_ros2'),
                    'launch',
                    'ld06.launch.py'
                ])
            ]),
        ),

       IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
               PathJoinSubstitution([
                   FindPackageShare('ros2_icm20948'),
                   'imu_localization_launch.py',
                ])
            ]),
        ),


       IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
               PathJoinSubstitution([
                    FindPackageShare('nav2_bringup'),
                    'launch',
                    'navigation_launch.py'
                ])
            ]),
       launch_arguments={
            'params_file': PathJoinSubstitution([
                FindPackageShare('nav2_bringup'),
                'params',
                'nav2_params.yaml'
            ]),
            'use_sim_time': 'false',
            'autostart': 'true'
        }.items(),
        ),


    ])
