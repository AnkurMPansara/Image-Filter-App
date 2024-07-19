import numpy as np
from PIL import Image
import tkinter as tk
from tkinter import filedialog
import os

# Define filter functions with internal parameters
def grayscale_filter(image_array):
    """Apply a grayscale filter to the image array."""
    return np.dot(image_array[..., :3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)

def invert_filter(image_array):
    """Apply an invert filter to the image array."""
    return 255 - image_array

def custom_filter(image_array):
    """Apply a custom filter to the image array with predefined parameters."""
    param1 = 50
    param2 = 30
    return np.clip(image_array + param1 - param2, 0, 255).astype(np.uint8)

# List of available filter names
FILTER_NAMES = ['grayscale', 'invert', 'custom']

# Mapping from filter names to filter functions
FILTER_FUNCTIONS = {
    'grayscale': grayscale_filter,
    'invert': invert_filter,
    'custom': custom_filter
}

def load_image(file_path):
    """Load an image from a file and convert it to a numpy array."""
    image = Image.open(file_path)
    return np.array(image)

def save_image(image_array, file_path):
    """Save a numpy array as an image file."""
    image = Image.fromarray(image_array)

    # Check if file path has an extension
    if not os.path.splitext(file_path)[1]:
        raise ValueError("No file extension provided in the output path.")

    try:
        image.save(file_path)
    except ValueError as e:
        print(f"Error saving image: {e}")
        raise

def apply_filter(image_array, filter_name):
    """Apply the selected filter to the image array."""
    if filter_name in FILTER_FUNCTIONS:
        return FILTER_FUNCTIONS[filter_name](image_array)
    else:
        raise ValueError(f"Unknown filter: {filter_name}")

def select_file_dialog(title, filetypes):
    """Open a file dialog to select a file."""
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(title=title, filetypes=filetypes)
    return file_path

def save_file_dialog(title, filetypes):
    """Open a file dialog to select a save location."""
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.asksaveasfilename(title=title, filetypes=filetypes, defaultextension=".png")
    return file_path

def main():
    # Open file dialog for input image
    input_path = select_file_dialog("Select the input image file", [("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    if not input_path:
        print("No input file selected. Exiting.")
        return

    # Open file dialog for output image
    output_path = save_file_dialog("Save the processed image file", [("PNG Files", "*.png"), ("JPEG Files", "*.jpg;*.jpeg"), ("All Files", "*.*")])
    if not output_path:
        print("No output file selected. Exiting.")
        return

    # Prompt for the filter to apply
    filter_name = input(f"Enter the filter to apply (options: {', '.join(FILTER_NAMES)}): ")
    
    if filter_name not in FILTER_NAMES:
        print(f"Filter '{filter_name}' not available. Choose from: {', '.join(FILTER_NAMES)}")
        return

    # Load image
    image_array = load_image(input_path)

    # Apply filter
    filtered_image_array = apply_filter(image_array, filter_name)

    # Save processed image
    try:
        save_image(filtered_image_array, output_path)
        print(f"Processed image saved to: {output_path}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
