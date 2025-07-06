import cv2
import math
import os

DESIRED_HEIGHT = 480
DESIRED_WIDTH = 480


def resize_and_show(image, window_name="Image"):
    h, w = image.shape[:2]
    if h < w:
        img = cv2.resize(image, (DESIRED_WIDTH, math.floor(h / (w / DESIRED_WIDTH))))
    else:
        img = cv2.resize(image, (math.floor(w / (h / DESIRED_HEIGHT)), DESIRED_HEIGHT))

    cv2.imshow(window_name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Example list of image filenames
IMAGE_FILENAMES = ["pointing_up.jpg", "thumbs_down.jpg", "thumbs_up.jpg","victory.jpg"]

# Check if files exist and read
images = {name: cv2.imread(name) for name in IMAGE_FILENAMES}

for name, image in images.items():
    if image is not None:
        print(f"Displaying: {name}")
        resize_and_show(image, window_name=name)
    else:
        print(f"Failed to load: {name}")
