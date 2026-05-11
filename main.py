from take_screenshots import *
from stitch_images import *
from measure_duration import *
from config import *



def stitch_images_columnwise(images, overlap):
    results = []
    for x in range(NUM_SCREENSHOTS[0]):
        column_images = images[x*NUM_SCREENSHOTS[1]:(x + 1)*NUM_SCREENSHOTS[1]]
        print(f"Stitching column {x} with {len(column_images)} images...")
        print(column_images)
        vertical_overlaps = calculate_vertical_overlaps(column_images, overlap, tol=0)

        ## maybe take average of overlaps for all overlaps?
        average_overlap = int(np.mean(vertical_overlaps))
        vertical_overlaps = [average_overlap] * len(vertical_overlaps)
        stitched_column = stitch_images_in_column(column_images, vertical_overlaps)
        stitched_column.save(f"stitched_column_{x}.png")
        results.append(stitched_column)
    return results

def stitch_columns_together(column_images, overlap):
    
    horizontal_overlaps = calculate_horizontal_overlaps(column_images, overlap)
    stitched_image = stitch_images_in_row(column_images, horizontal_overlaps)
    return stitched_image







### taking screenshots

loaded_images = measure(load_images, IMAGE_PATHS)
print("loaded images")
print(loaded_images)

column_images = measure(stitch_images_columnwise, loaded_images)

measure(stitch_columns_together, column_images)
print("Done!")