from flask import Flask, render_template, request
from ultralytics import YOLO
import cv2
import os

app = Flask(__name__)
model = YOLO("yolov8n.pt")  # Pretrained model

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/detect', methods=['POST'])
def detect():
    if 'image' not in request.files:
        return 'No image uploaded', 400

    file = request.files['image']
    if file.filename == '':
        return 'No selected file', 400

    path = 'static/upload.jpg'
    file.save(path)

    results = model(path)[0]
    annotated_frame = results.plot()

    # Filter: Only draw dogs (COCO class 16)
    dog_class_id = 16
    filtered_boxes = [box for box in results.boxes.data if int(box[5]) == dog_class_id]
    
    img = cv2.imread(path)
    for box in filtered_boxes:
        x1, y1, x2, y2 = map(int, box[:4])
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

    output_path = 'static/output.jpg'
    cv2.imwrite(output_path, img)

    return render_template("index.html", result=True)

if __name__ == '__main__':
    app.run(debug=True)
