
import os

### config

## calibration for different zoom levels, just to keep track of them.
# name | zoomlevel (for file names)...
# ...| number of columns and rows | delay between screenshots (moving right and top) | expected overlap in pixels (right/left and top/bottom)
CALIBRATION = {
    "just under the clouds": [1, (10,12), (2.5, 1.0), (660, 548)],
    "Atlas max zoom":[3, (15, 16), (2.0, 1.0), (470,350)],
}


# define number of screenshots and delay between them
NUM_SCREENSHOTS = (15, 15) # 10 columns, 12 rows
DELAY_BETWEEN_SCREENSHOTS = (2.0, 1.0) #  moving right and top in seconds
OVERLAP = (470, 323) # overlap in pixels to the right/left and top/bottom
TOLERANCE = 20 # tolerance in pixels for finding the best overlap


OUTPUT_DIR = "screenshots"
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(f"{OUTPUT_DIR}/columns", exist_ok=True)

IMAGE_PATHS = [f"screenshots/screenshot_{x}_{y}.png" for x in range(NUM_SCREENSHOTS[0]) for y in range(NUM_SCREENSHOTS[1])]
OUTPUT_PATH = "stitched.png"
#print(IMAGE_PATHS)