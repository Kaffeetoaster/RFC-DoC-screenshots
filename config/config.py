
import os

### config

## calibration for different zoom levels
# name | zoomlevel (for file names)...
# ...| number of columns and rows | delay between screenshots (moving right and top) | expected overlap in pixels (right/left and top/bottom)
CALIBRATION = {
    "just under the clouds": [1, (10,12), (2.5, 1.0), (660, 548)],
    "max zoomed in":[],
}


# define number of screenshots and delay between them
NUM_SCREENSHOTS = (10, 12) # 10 columns, 12 rows
DELAY_BETWEEN_SCREENSHOTS = (2.5, 1.0) #  moving right and top in seconds
OVERLAP = (660, 548) # overlap in pixels to the right/left and top/bottom



OUTPUT_DIR = "screenshots"
os.makedirs(OUTPUT_DIR, exist_ok=True)

IMAGE_PATHS = [f"screenshots/screenshot_{x}_{y}.png" for x in range(NUM_SCREENSHOTS[0]) for y in range(NUM_SCREENSHOTS[1])]
OUTPUT_PATH = "stitched.png"
#print(IMAGE_PATHS)