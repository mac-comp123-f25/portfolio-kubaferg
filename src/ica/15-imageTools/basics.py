from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def main():
    # Load image
    pic = Picture("../SampleImages/mightyMidway.jpg")

    # Get width and height
    width = pic.getWidth()
    height = pic.getHeight()

    # Number of pixels = width * height
    print("Number of pixels:", width * height)

    # Make copy
    new_pic = pic.copy()

    # Set corner pixels to red
    red = (255, 0, 0)
    new_pic.setColor(0, 0, red)                      # top-left
    new_pic.setColor(width - 1, 0, red)              # top-right
    new_pic.setColor(0, height - 1, red)             # bottom-left
    new_pic.setColor(width - 1, height - 1, red)     # bottom-right

    # Save result
    new_pic.save("../SampleImages/mightyMidway-redCorners.jpg")

    # Explore to zoom in
    new_pic.explore()

    keep_windows_open()

if __name__ == "__main__":
    main()
