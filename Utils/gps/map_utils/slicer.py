# generated with ChatGPT
from PIL import Image
import os
import argparse

def split_into_tiles(image_path, output_folder, tile_size=128):
    # Load the image
    image = Image.open(image_path)
    image_width, image_height = image.size

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over the image and cut it into tiles
    for y in range(0, image_height, tile_size):
        for x in range(0, image_width, tile_size):
            # Crop the tile
            box = (x, y, x + tile_size, y + tile_size)
            tile = image.crop(box)

            # Save the tile as PNG with the name based on coordinates
            tile_filename = os.path.join(output_folder, f"tile_{(x/128):.0f}_{(y/128):.0f}.png")
            tile.save(tile_filename)
            print(f"Saved: {tile_filename}")

if __name__ == "__main__":
    # Command line argument setup
    parser = argparse.ArgumentParser(description="Split an image into tiles.")
    parser.add_argument("image_path", type=str, help="Path to the PNG file.")
    parser.add_argument("output_folder", type=str, help="Path to the output folder for tiles.")
    parser.add_argument("--tile_size", type=int, default=128, help="Size of each tile in pixels (default 128).")

    # Parse arguments
    args = parser.parse_args()

    # Run the function to split the image
    split_into_tiles(args.image_path, args.output_folder, args.tile_size)

