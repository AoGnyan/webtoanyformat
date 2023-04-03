import os
from PIL import Image

input_dir = "/path/to/webp/files"
output_dir = "/path/to/jpg/files"
old_dir = "/path/to/old/files"
file_number = 1

# Create the "old" directory if it doesn't exist
if not os.path.exists(old_dir):
    os.makedirs(old_dir)

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for file_name in os.listdir(input_dir):
    if file_name.endswith(".webp"):
        # Open the image using PIL
        image_path = os.path.join(input_dir, file_name)
        with Image.open(image_path) as image:
            # Convert the image to RGB format
            rgb_image = image.convert("RGB")

            # Create the output file path
            output_file_name = f"{file_number:02d}.jpg"
            output_path = os.path.join(output_dir, output_file_name)

            # Save the image as JPEG
            rgb_image.save(output_path)
            print(f"Converted {image_path} to {output_path}")

        # Move the original file to the "old" directory
        old_file_path = os.path.join(old_dir, file_name)
        os.rename(image_path, old_file_path)
        print(f"Moved {image_path} to {old_file_path}")

        # Increment the file number
        file_number += 1