# Project Name: wiz ambient lighting

## Overview:

This project is a Python script that streams live color data  from your monitor to control Wiz smart lights. It continuously captures the average color of the screen and updates the Wiz light accordingly, creating a dynamic and immersive lighting experience.

Upcoming Features
- [ ]  Brightness Control
- [ ] Ambience based on Sound Output
- [ ] Tweak in algorithm for more seamless changes

## Dependencies:

- Python 3.6 or above
- `pywizlight`: Python library for controlling Wiz smart lights
- `numpy`: Library for numerical computing in Python
- `PIL`: Python Imaging Library for image processing
- `functools`: Module for higher-order functions and operations on callable objects
## Setup:

1. Ensure Python 3.6 or above is installed on your system.
2. Install the required dependencies using pip:
    
Copy code

```python
pip install pywizlight PIL numpy
```

3. Clone or download the project repository.

## Usage:

1. Run the Python script provided in the repository.
    
    Copy code
    
    `python main.py`
    
2. Modify the IP address of the Wiz smart light (`light = wizlight("192.168.1.2")`) to match your device's IP address.
3. The script continuously captures the average color of the screen and adjusts the Wiz smart light accordingly.
4. Enjoy the dynamic lighting effects!
5. `CTRL + C` To exit.

## Customization:

- You can adjust the frame length (`frame_length` parameter in `get_rgb` function) to control the smoothness and responsiveness of color transitions.
- Control frames captured by altering `await asyncio.sleep(0.5)`


## Notes:

- This script utilizes asyncio for asynchronous execution to ensure smooth performance.
- Ensure that your Wiz smart light is connected to the same network as the device running the script for proper communication.

## Contributors:

- (Steve The Jobless)[https://github.com/SteveTheJobless] with the help ChatGPT :)

## License:

This project is licensed under the MIT License.
