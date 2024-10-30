# Install the specific version of Ultralytics YOLO if you need to
# pip install ultralytics==8.2.103

import os
from ultralytics import YOLO

# Change the working directory
os.chdir("D:/TRIK/Semester 3/PMLD/py")  # Update to your folder path

# Load your trained YOLO model
model = YOLO("best.pt")  # Make sure 'best.pt' is ready for action

# Run the prediction on the image
results = model.predict(
    source="leaf_area.jpg",     # Input image
    conf=0.25,                  # Confidence threshold for predictions
    save=True,                  # Save the output image
    name="predict_",            # Name for the output folder
    show_boxes=True,            # Display the predicted bounding boxes
    show=False                  # Don't show the image now
)

# Output location for the predicted image
print("Prediction complete! Check your results in the 'runs/segment/predict_*' folder.")
