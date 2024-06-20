# etch-a-sketch-3D-bot
A 3D printed bot for drawing with Etch-A-Sketch

![demo](./etch_a_sketch_demo.jpg)

## Hardware
2x stepper motor
I'm using 28BYJ-48, it just works but not recommended because:
1. it's very slow (10 rpm to prevent step losses)
2. inaccurate (check out the movement compensation code in `serial_write.py`)

## 3D printed connecter and frames
In `3D_parts` folder.

## Arduino
Code are in `stepper_oneRevolution`, will read intruction from serial port.

## Control code
* `route_planner.py` is a very simple dfs planner, will generate many redundant steps, but it works
* `serial_write.py` send the steps to Arduion and drive the moter.


## Todo (maybe never)
1. store the data in on-board flash so that it doesn't need to be connected to a PC
2. support bluetooth or wifi (w/ esp32)
3. better route planner
4. better stepper motors
