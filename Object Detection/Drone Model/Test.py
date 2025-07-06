from ultralytics import YOLO
# Load a model
model = YOLO("yolo11n.pt")  # pretrained YOLO11n model

# # Run batched inference on a list of images
results = model(["0_Ddm2FAnYWo3bg1Y5.jpg", "images.jpeg"])  # return a list of Results objects

print(results)
# Process results list
for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    result.show()  # display to screen
    result.save(filename="result.jpg")  # save to disk
