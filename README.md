
# YOLOv8 Dog Detector

A simple web application to detect dogs in images using a pretrained YOLOv8 model.


## Description

This project uses the **Ultralytics YOLOv8** pretrained model to detect dogs from images uploaded via a web interface built with **Flask**.  
Bounding boxes around detected dogs are drawn using **OpenCV (cv2)**.


## Libraries Used

- [Ultralytics YOLO](https://github.com/ultralytics/ultralytics) (`ultralytics`)
- Flask
- OpenCV (`cv2`)
- os (standard Python library)

---

## Dataset

- COCO dataset (used by the pretrained YOLOv8 model for training)


## Features

- Upload an image via a web page.
- Detect dogs only (COCO class id 16).
- Draw bounding boxes around detected dogs using OpenCV.
- Display the resulting image on the web page.

## Usage

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd <repository-folder>
    ```

2. Install dependencies (recommended in a virtual environment):

    ```bash
    pip install ultralytics flask opencv-python
    ```

3. Run the Flask app:

    ```bash
    python app.py
    ```

4. Open your browser and go to `http://127.0.0.1:5000/`.

5. Upload an image containing dogs and click "Detect".

---

