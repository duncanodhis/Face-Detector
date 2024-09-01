import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import io
import os
import cv2
import numpy as np
from google.cloud import vision
from datetime import datetime

# Initialize Google Cloud Vision client
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = ""
client = vision.ImageAnnotatorClient()

class RealTimeFaceDetectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Real-Time Face Detection and Recognition Tool")
        self.root.geometry("1280x720")  # Set initial window size

        # Configure grid layout
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=0)

        # Create UI elements
        self.canvas = tk.Canvas(root, bg='black')
        self.canvas.grid(row=0, column=0, sticky='nsew')

        self.capture_button = tk.Button(root, text="Capture Face", command=self.capture_face)
        self.capture_button.grid(row=1, column=0, pady=10, padx=10, sticky='ew')

        self.video_source = 0  # Use the default webcam
        self.vid = cv2.VideoCapture(self.video_source)
        self.vid.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # Set width
        self.vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)  # Set height
        self.vid.set(cv2.CAP_PROP_FPS, 30)           # Set frame rate

        self.update_video()

    def update_video(self):
        ret, frame = self.vid.read()
        if ret:
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            rgb_frame = self.enhance_image(rgb_frame)
            self.process_frame(rgb_frame)
            self.tk_image = ImageTk.PhotoImage(image=Image.fromarray(rgb_frame))
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)
            self.canvas.config(width=self.root.winfo_width(), height=self.root.winfo_height() - 50)
        
        # Adjust the delay to balance performance and smoothness
        self.root.after(10, self.update_video)

    def enhance_image(self, frame):
        # Enhance image quality
        frame = cv2.convertScaleAbs(frame, alpha=1.2, beta=20)  # Increase contrast and brightness
        frame = cv2.GaussianBlur(frame, (3, 3), 0)              # Optional: Smooth image
        return frame

    def process_frame(self, frame):
        # Convert frame to bytes
        _, buffer = cv2.imencode('.jpg', frame)
        content = buffer.tobytes()
        
        image = vision.Image(content=content)
        response = client.face_detection(image=image)
        faces = response.face_annotations

        # Draw rectangles around detected faces
        for face in faces:
            box = face.bounding_poly
            vertices = [(vertex.x, vertex.y) for vertex in box.vertices]
            self.draw_rectangle(frame, vertices)

    def draw_rectangle(self, frame, vertices):
        points = np.array(vertices, np.int32)
        points = points.reshape((-1, 1, 2))
        cv2.polylines(frame, [points], isClosed=True, color=(0, 255, 0), thickness=2)

    def capture_face(self):
        # Save the current frame as an image
        ret, frame = self.vid.read()
        if ret:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"captured_face_{timestamp}.jpg"
            cv2.imwrite(filename, frame)
            print(f"Face captured and saved as {filename}")

    def __del__(self):
        self.vid.release()

if __name__ == "__main__":
    root = tk.Tk()
    app = RealTimeFaceDetectionApp(root)
    root.mainloop()
