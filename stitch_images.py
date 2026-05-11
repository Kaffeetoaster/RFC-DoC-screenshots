from PIL import Image
import numpy as np


from measure_duration import measure
from config.config import IMAGE_PATHS, OVERLAP, NUM_SCREENSHOTS

def load_images(paths):
    images = []
    for path in paths:
        image = Image.open(path).convert("RGB")
        if image is None:
            raise FileNotFoundError(f"Could not read image: {path}")
        images.append(image)
    if not images:
        raise ValueError("IMAGE_PATHS must contain at least one image")
    return images

def find_vertical_overlap(img1, img2, average_overlap, tol = 30):
    arr1 = np.array(img1)
    arr2 = np.array(img2)

    best_overlap = None
    best_score = float("inf")

    for overlap in range(average_overlap - tol, average_overlap + tol + 1):
        region1 = arr1[:overlap]      # top of img1
        region2 = arr2[-overlap:]     # bottom of img2

        score = np.mean(
            (region1.astype(np.float32) - region2.astype(np.float32)) ** 2
        )

        if score < best_score:
            best_score = score
            best_overlap = overlap
    print(f"Best vertical overlap: {best_overlap} pixels with MSE score: {best_score}")
    return best_overlap

def find_horizontal_overlap(img1, img2, average_overlap, tol = 30):
    arr1 = np.array(img1)
    arr2 = np.array(img2)

    best_overlap = None
    best_score = float("inf")

    for overlap in range(average_overlap - tol, average_overlap + tol + 1):
        region1 = arr1[:, -overlap:]      # right of img1
        region2 = arr2[:, :overlap]     # left of img2

        score = np.mean(
            (region1.astype(np.float32) - region2.astype(np.float32)) ** 2
        )

        if score < best_score:
            best_score = score
            best_overlap = overlap
    print(f"Best horizontal overlap: {best_overlap} pixels with MSE score: {best_score}")
    return best_overlap

def calculate_horizontal_overlaps(images, average_overlap, tol = 30):
    overlaps = []
    for i in range(len(images) - 1):
        overlap = find_horizontal_overlap(images[i], images[i + 1], average_overlap, tol)
        overlaps.append(overlap)
    return overlaps

def calculate_vertical_overlaps(images, average_overlap, tol = 30):
    overlaps = []
    for i in range(len(images) - 1):
        overlap = find_vertical_overlap(images[i], images[i + 1], average_overlap, tol)
        overlaps.append(overlap)
    return overlaps

def stitch_images_vertical(img1, img2, overlap, show_seam = False):
    w, h = img1.size

    result = Image.new("RGB", (w, h * 2 - overlap))

    result.paste(img2, (0, 0))
    result.paste(img1.crop((0, overlap, w, h)), (0, h))

    if show_seam == True:
        # Seam position
        seam_y = h
        seam_height = 3
        # Extract seam strip
        seam = result.crop((0, seam_y, w, seam_y + seam_height))
        seam = seam.convert("RGBA")
        # Create transparent green overlay
        green = Image.new("RGBA", seam.size, (0, 255, 0, 120))

        # Composite
        highlighted = Image.alpha_composite(seam, green)

        # Paste back
        result.paste(highlighted, (0, seam_y))
    return result

def stitch_images_in_column(img_list,  overlaps):
    w, h = img_list[0].size
    total_height = h * len(img_list) - sum(overlaps)

    result = Image.new("RGB", (w, total_height))
    
    current_y = total_height
    for i, img in enumerate(img_list):
        current_y -= h  # Move up by the height of the image
        if i==0:
            result.paste(img, (0, current_y))
        else:
            current_y += overlaps[i - 1]  # Shift down by the overlap of the previous image
            result.paste(img, (0, current_y))

    return result

def stitch_images_in_row(img_list, overlaps):
    w, h = img_list[0].size
    total_width = w * len(img_list) - sum(overlaps)

    result = Image.new("RGB", (total_width, h))
    
    current_x = 0
    for i, img in enumerate(img_list):
        result.paste(img, (current_x, 0))
        if i < len(overlaps):
            current_x += w - overlaps[i]  # Shift right by the width minus the overlap

    return result

def stitch_images_columnwise(images,number_x, number_y,overlap):
    results = []
    for x in range(number_x):
        column_images = images[x*number_y:(x + 1)*number_y]
        print(f"Stitching column {x} with {len(column_images)} images...")
        print(column_images)
        vertical_overlaps = calculate_vertical_overlaps(column_images, overlap, tol=25)

        ## maybe take average of overlaps for all overlaps?
        average_overlap = int(np.mean(vertical_overlaps))
        vertical_overlaps = [average_overlap] * len(vertical_overlaps)
        stitched_column = stitch_images_in_column(column_images, vertical_overlaps)
        stitched_column.save(f"stitched_column_{x}.png")
        results.append(stitched_column)
    return results

def stitch_columns_together(column_images, overlap):
    
    horizontal_overlaps = calculate_horizontal_overlaps(column_images, overlap, tol=25)
    stitched_image = stitch_images_in_row(column_images, horizontal_overlaps)
    return stitched_image



loaded_images = measure(load_images, IMAGE_PATHS)
print("loaded images")
print(loaded_images)

column_images = measure(stitch_images_columnwise, loaded_images,NUM_SCREENSHOTS[0], NUM_SCREENSHOTS[1], OVERLAP[1])

measure(stitch_columns_together, column_images, OVERLAP[0]).save("stitched.png")
print("Done!")