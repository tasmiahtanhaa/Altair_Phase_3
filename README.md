# Project Altair - Phase 3

## Student Information
- **Name:** Tasmiah Tanha
- **Department:** CSE
- **Student ID:** [240041206]

## Environment & Versions
- **OS:** Ubuntu 24.04 (via WSL2 on Windows 11)
- **ROS 2 Distribution:** Jazzy Jalisco
- **Python Version:** 3.12

## Package Overview
- `altair_phase3`: Contains the core Python nodes for Phase 3:
  - `telemetry_node.py`: Publishes simulated rover telemetry data (battery, temperature, mode).
  - `drive_node.py`: Publishes velocity commands (`geometry_msgs/msg/Twist`) for movement control.
  - `nav_node.py`: Implements a ROS 2 Service Server (`std_srvs/srv/SetBool`) to toggle navigation state.

## Build Instructions
```bash
cd ~/altair_ws
colcon build --packages-select altair_phase3
