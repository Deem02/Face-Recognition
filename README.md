# Real-Time Face Recognition Application

This real-time face recognition application utilizes Flask, OpenCV, MTCNN, and FaceNet to identify and authenticate individuals through a webcam feed. The system captures video, detects faces, and compares them with stored face images to determine authorization. It's an efficient solution for implementing secure, real-time access control based on facial recognition technology.

## Table of Contents
1. [Overview](#overview)
2. [Project Structure](#project-structure)
3. [Installation](#installation)
   - [Prerequisites](#prerequisites)
   - [Dependencies](#dependencies)
4. [Usage](#usage)
   - [Running the Application](#running-the-application)
   - [Adding Stored Face Images](#adding-stored-face-images)
5. [Code Explanation](#code-explanation)
   - [app.py](#app.py)
   - [index.html](#index.html)
   - [Face Recognition Logic](#face-recognition-logic)
6. [Example Outputs](#example-outputs)
   - [Authorized](#authorized)
   - [Unauthorized](#unauthorized)

## Overview
This project is a real-time face recognition application using Flask, OpenCV, MTCNN, and FaceNet. It captures video from the webcam, detects faces, and compares them with stored face images to determine if the person is authorized.

## Project Structure
```
face_recognition_app/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── stored_face_images/
```

- **app.py**: The main Flask application file that includes the server setup, routes, and face recognition logic.
- **templates/index.html**: The HTML template for the web interface.
- **static/stored_face_images/**: Directory containing stored face images for comparison.

## Installation

### Prerequisites
- Python 3.6+
- Pip package manager

### Dependencies
Install the required packages using pip:
```bash
pip install flask opencv-python-headless numpy mtcnn keras_facenet scikit-learn
```

## Usage

### Running the Application
To start the Flask server, run the following command in the project directory:
```bash
python app.py
```

The application will be accessible at `http://127.0.0.1:5000/` in your web browser.

### Adding Stored Face Images
1. Place the images of authorized faces in the `static/stored_face_images/` directory.
2. Ensure that the images are in `.jpg`, `.jpeg`, or `.png` format.

## Code Explanation

### app.py
- **FaceRecognition Class**: Handles face detection, preprocessing, embedding extraction, and embedding comparison.
- **Routes**:
  - `/`: Renders the home page.
  - `/video_feed`: Streams video frames with face recognition results.
- **generate_frames Function**: Captures video frames from the webcam, performs face detection and recognition, and annotates the frames based on the recognition results.

### index.html
- A simple HTML template that displays the real-time video feed from the webcam.

### Face Recognition Logic
1. **Face Detection**: Uses MTCNN to detect faces in the video frames.
2. **Face Embeddings**: Uses FaceNet to extract 128-dimensional embeddings for detected faces.
3. **Comparison**: Compares the embeddings of the detected face with those of stored faces using cosine similarity. If the similarity exceeds a threshold, the person is marked as authorized.


# Example Outputs

### Authorized
When a face matches with any of the stored face images, the output is annotated with "Authorized".

#![Athorized](https://github.com/user-attachments/assets/347a30fe-9432-4083-be4f-16f618d1a41f)

### Unauthorized
When a face does not match any of the stored face images, the output is annotated with "Unauthorized".
![Unauthorized](https://github.com/user-attachments/assets/3b9dfbee-8f66-4887-9436-b9541e01907e)

