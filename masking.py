import os
import cv2
import numpy as np
from ultralytics import YOLO
import shutil

# Set paths
WORKING_DIR = "D:/TRIK/Semester 3/PMLD/py" # Change your to working folder
image = "3leaf.png"  # Change image path here
IMAGE_FOLDER = "Snapshot"  # Change the folder where images are stored
MODEL_PATH = "daun200.pt" # Model's name

SOURCE_IMAGE = os.path.join(IMAGE_FOLDER, image)
OUTPUT_FOLDER = "Outputs"
DAUN_FOLDER = "Daun"
MASKS_FOLDER = "Masks"
RUNS_FOLDER = "runs"

# Change to the working directory and load the model
os.chdir(WORKING_DIR)
model = YOLO(MODEL_PATH)

# Field of view calculations
dsensor = 200
theta, alpha = 16, 12
sudut = np.tan(np.radians(theta / 2))
sudut2 = np.tan(np.radians(alpha / 2))
nilaiH = 2 * dsensor * sudut
nilaiW = 2 * dsensor * sudut2

# Ensure necessary folders exist
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
os.makedirs(DAUN_FOLDER, exist_ok=True)
os.makedirs(MASKS_FOLDER, exist_ok=True)

# Run prediction
results = model.predict(source=SOURCE_IMAGE, conf=0.25, save=True, show_boxes=True, show_labels=True)

# Load the original image and create a blank mask
original_image = cv2.imread(SOURCE_IMAGE)
combined_mask = np.zeros(original_image.shape[:2], dtype=np.uint8)

# Process results
for result in results:
    boxes = result.boxes
    masks = result.masks

    for i, box in enumerate(boxes):
        x, y, w, h = (float(coord) for coord in box.xywh[0])
        lebar_objek_mm = abs(round((nilaiW * w) / 400, 3))
        panjang_objek_mm = abs(round((nilaiH * h) / 300, 3))
        luas_objek_mm2 = abs(round(lebar_objek_mm * panjang_objek_mm, 3))
        print(f"Bounding Box: {w:.0f} px x {h:.0f} px")
        print(f"Width: {lebar_objek_mm} mm, Height: {panjang_objek_mm} mm, Area: {luas_objek_mm2} mm²\n")

        if masks is not None:
            mask_data = (masks.data[i].numpy() * 255).astype(np.uint8)
            mask_resized = cv2.resize(mask_data, (original_image.shape[1], original_image.shape[0]))
            combined_mask = cv2.bitwise_or(combined_mask, mask_resized)

# Apply mask and save results
masked_image = cv2.bitwise_and(original_image, original_image, mask=combined_mask)
cv2.imwrite(os.path.join(DAUN_FOLDER, f"{image.split('.')[0]}_masked.png"), masked_image)

bw_mask = (combined_mask > 0).astype(np.uint8) * 255
cv2.imwrite(os.path.join(MASKS_FOLDER, f"{image.split('.')[0]}_mask.png"), bw_mask)

# Save predicted image if it exists
predicted_image_path = os.path.join(RUNS_FOLDER, "segment", "predict", f"{image.split('.')[0]}.jpg")
if os.path.exists(predicted_image_path):
    predicted_image = cv2.imread(predicted_image_path)
    cv2.imwrite(os.path.join(OUTPUT_FOLDER, f"{image.split('.')[0]}_outputs.png"), predicted_image)

# Clean up runs folder
shutil.rmtree(RUNS_FOLDER, ignore_errors=True)
