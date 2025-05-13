import cv2
import os
import re
import easyocr
import time
from PIL import Image
import numpy as np

VIDEO_PATH = "traffic1.mp4"     
OUTPUT_FILE = "video1_results.txt"

def preprocess_image(image_path):
    img = cv2.imread(image_path)
    
    # Converting to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    thresh = cv2.adaptiveThreshold(
        gray, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV, 11, 2
    )
    
    cv2.imwrite(image_path, thresh)

def validate_indian_plate(text):
    """Strict regex for Indian license plates."""
    # Formats: KA 02 MN 1826, DL 4C AB 1234, TN 38 N 5489
    pattern = r"^[A-Z]{2}\s?[0-9]{1,2}\s?[A-Z]{1,3}\s?[0-9]{4}$"
    return re.match(pattern, text.replace(" ", ""))

def detect_plates(image_path):
    """Detect Indian plates using EasyOCR with preprocessing."""
    # 1. Preprocessing the image
    preprocess_image(image_path)
    
    # 2. Initializing EasyOCR
    if not hasattr(detect_plates, 'reader'):
        detect_plates.reader = easyocr.Reader(["en"])
    
    results = detect_plates.reader.readtext(image_path, detail=1)
    
    plates = []
    for detection in results:
        text = detection[1].strip().upper()
        confidence = float(detection[2]) * 100 
    
        # Threshold 70%
        if validate_indian_plate(text) and confidence >= 70.0:
            plates.append({
                "plate": text.replace(" ", ""),  
                "confidence": confidence
            })
    
    return plates

def process_video(video_path, output_file):
    """Process video frame-by-frame."""
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = 0
    
    with open(output_file, "w") as f:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            if frame_count % int(fps) == 0:
                timestamp = time.strftime('%H:%M:%S', time.gmtime(frame_count / fps))
                temp_image = f"temp_frame_{frame_count}.jpg"
                cv2.imwrite(temp_image, frame)
                
                plates = detect_plates(temp_image)
                for plate in plates:
                    line = f"{timestamp} | {plate['plate']} | Confidence: {plate['confidence']:.2f}%"
                    print(line)
                    f.write(line + "\n")
                
                os.remove(temp_image)  
            
            frame_count += 1
    
    cap.release()
    print(f"\n Results saved to {output_file}")

if __name__ == "__main__":
    if os.path.exists(VIDEO_PATH):
        print("\nProcessing video...")
        process_video(VIDEO_PATH, OUTPUT_FILE)
    else:
        print(f"Video not found: {VIDEO_PATH}")