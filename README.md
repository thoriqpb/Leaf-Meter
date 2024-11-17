# Leaf Meter🍃
A big thank you to our team members for making this project a success:
1. **Thoriq Putra Belligan**
2. **Muhammad Harits Naufal Kurniwan**
3. **Naufal Najib**
4. **Muhammad Adib Elfito**

This project is part of the **Project Mandiri Lintas Disiplin (PMLD)** course. The outcome is a tool that automatically measures leaf dimensions for up to 3 leaves using **YOLOv8 instance segmentation**.

## Components and Software🔩
This project involves three main components:
- **Raspberry Pi 4B**: Serves as both the computer and microcontroller.
- **Camera**: (Exact specifications unknown) Captures images for analysis.
- **Time-of-Flight Sensor (VL53L0X)**: A laser-based distance sensor for accurate measurements.

For the interface, we used QTDesigner to create and design the Graphical User Interface (GUI).

## Input and Outputs📷
The program processes snapshots captured by the camera. During the analysis phase, it calculates the width and height of the object based on the masked object's pixel dimensions and its distance from the camera.

<div align="center"> <img src="https://github.com/thoriqpb/Leaf-Meter/blob/main/images/GUI_display.jpg" alt="GUI Display" width="600"> </div>

Users can save all image outputs and leaf dimension data simply by clicking the `save` button.
