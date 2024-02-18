import numpy as np
from PIL import ImageGrab
from functools import partial

def convert_to_color(rgb):
    """
    Convert an RGB value to a primary, secondary, or tertiary color.

    Args:
    rgb (tuple): Tuple containing RGB values.

    Returns:
    str: Name of the primary, secondary, or tertiary color.
    """

    # Define colors
    colors = {
        (255, 0, 0): "Red",
        (0, 255, 0): "Green",
        (0, 0, 255): "Blue",
        (255, 255, 0): "Yellow",
        (255, 0, 255): "Magenta",
        (0, 255, 255): "Cyan",
        (255, 128, 0): "Orange",
        (128, 255, 0): "Chartreuse",
        (0, 255, 128): "Spring Green",
        (0, 128, 255): "Azure",
        (128, 0, 255): "Violet",
        (255, 0, 128): "Rose"
    }


    # Check if the RGB value matches a primary color
    for color, name in colors.items():
        if rgb == color:
            return name
        
    # If not a primary, secondary, or tertiary color, determine the closest color
    min_dist = float('inf')
    closest_color = None
    closest_rgb = None
    for color, name in colors.items():
        dist = sum((x - y) ** 2 for x, y in zip(rgb, color))
        if dist < min_dist:
            min_dist = dist
            closest_color = name
            closest_rgb = color

    return closest_rgb





def get_adjusted_rgb(rgb_tuple):
    # Find the largest, second largest, and smallest values
    largest = max(rgb_tuple)
    smallest = min(rgb_tuple)
    second_largest = sorted(rgb_tuple)[-2]
    # Convert the tuple according to the criteria
    converted_rgb = (x if x == largest else 0 if x == smallest else x for x in rgb_tuple)

    # Print the result
    rgb_tuple = tuple(converted_rgb)
    return rgb_tuple


def get_frame_avg(frames):
    if not frames:
        return None  # Return None if the list is empty
    tuple_length = len(frames[0])  # Get the length of each tuple
    tuple_sum = [0] * tuple_length  # Initialize a list to store the sum of each element
    for tpl in frames:
        for i in range(tuple_length):
            tuple_sum[i] += tpl[i]  # Sum up each element of the tuples
    average_tuple = tuple(int(sum_elem / len(frames)) for sum_elem in tuple_sum)  # Calculate the average
    return average_tuple





def get_average_color():
    # Take a screenshot of the entire screen
    ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)
    
    average_colors = []
    num_shots = 1
    for _ in range(num_shots):
        img = ImageGrab.grab()
        img = img.crop((2560, 0, 2560 + 1920, 1080))

        # Convert the screenshot to a numpy array
        screenshot_np = np.array(img)

        # Calculate the average color of the screenshot
        average_color = tuple(np.mean(screenshot_np, axis=(0, 1)).astype(int))
        average_colors.append(average_color)

    # Calculate the average of the average RGB values for all shots
    overall_average_color = tuple(np.mean(average_colors, axis=0).astype(int))
    return overall_average_color

if __name__ == "__main__":
    average_color = get_average_color()
    print(f"Average RGB color of the screen: {average_color}")
