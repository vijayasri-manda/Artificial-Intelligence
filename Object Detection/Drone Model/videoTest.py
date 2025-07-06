from ultralytics import YOLO

# Load a pretrained YOLO11n model
model = YOLO("yolo11n.pt")

# Define source as YouTube video URL
source = "videoplayback.mp4"

# Run inference on the source
results = model(source,show=True,save=True)  # generator of Results objects
