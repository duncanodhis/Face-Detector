---

# Real-Time Face Detection and Recognition Tool

## Overview

This application provides real-time face detection and recognition capabilities using the Google Cloud Vision API and OpenCV. It captures video from your webcam, detects faces, and allows you to capture and save frames with detected faces.

## Features

- Real-time face detection using Google Cloud Vision API.
- Live video feed with face bounding boxes drawn around detected faces.
- Option to capture and save frames with detected faces.
- Enhanced image quality with adjustable contrast and brightness.

## Requirements

- **Python 3.x**
- **Google Cloud Vision API**:
  - Set up a Google Cloud project and enable the Vision API.
  - Obtain and configure your service account credentials.
- **Required Python Libraries**:
  - `google-cloud-vision`
  - `opencv-python-headless`
  - `pillow`
  - `numpy`

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/face-detection-app.git
   cd face-detection-app
   ```

2. **Install the required Python libraries**:
   ```bash
   pip install google-cloud-vision opencv-python-headless pillow numpy
   ```

3. **Configure Google Cloud Vision API**:
   - Create a service account key in your Google Cloud project.
   - Download the JSON key file and set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable:
     ```bash
     export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service-account-file.json"
     ```

## Usage

1. **Run the Application**:
   ```bash
   python face_detection_app.py
   ```

2. **Interacting with the Application**:
   - **Live Video Feed**: The application will display a live video feed from your webcam with detected faces outlined in green rectangles.
   - **Capture Face**: Click the "Capture Face" button to save the current frame with detected faces as an image file.

3. **Captured Files**:
   - Saved images will be stored in the same directory as the script, with filenames including the timestamp of the capture.

## Code Overview

- **`face_detection_app.py`**: Main script containing the application logic.
  - `RealTimeFaceDetectionApp`: Class handling video capture, face detection, and GUI updates.
  - `update_video()`: Method that continuously updates the video feed.
  - `process_frame(frame)`: Method that processes each video frame to detect faces.
  - `capture_face()`: Method that saves the current frame with detected faces.

## Troubleshooting

- **Google Cloud Vision API Errors**:
  - Ensure your service account credentials file is correctly configured.
  - Check your Google Cloud project for API quota and billing issues.

- **Video Issues**:
  - Verify that your webcam is properly connected and accessible.
  - Adjust video resolution and frame rate settings if necessary.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For questions or support, please contact [Your Name] at [Your Email Address].

---
