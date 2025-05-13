# Indian Number Plate Detection 

This project processes traffic footage (`traffic1.mp4`) to detect and extract Indian vehicle number plates using Optical Character Recognition (OCR). The recognized plates are saved with timestamps and confidence scores in a text file.

## Objective

To identify valid Indian number plates from a video and store the results in a structured `.txt` format. The video was sourced from Google Drive (link to be added).

## Video Details

- Filename: `traffic1.mp4`
- Source: Google Drive (link will be inserted)
- Purpose: Used as input for OCR-based license plate recognition

## What is OCR?

OCR (Optical Character Recognition) is a technology that enables computers to read and extract text from images or videos. It is commonly used for digitizing documents, reading signs, and recognizing vehicle license plates.

## OCR Engine Used

We used `EasyOCR`, a deep learning-based OCR library known for its strong performance on real-world text and flexibility with different fonts and formats.

Reasons for using EasyOCR:
- Performs well on noisy and varied real-world images
- Supports English, which is used in Indian number plates
- Easy to integrate with Python

## Preprocessing Steps

Each frame from the video is preprocessed before applying OCR to enhance detection accuracy:
1. Converted to grayscale to simplify the image
2. Adaptive thresholding is applied to improve text visibility
3. The processed image is saved temporarily for OCR input

## Output

- Output File: `video1_results.txt`
- Each line includes:
  - Timestamp (format: HH:MM:SS)
  - Recognized number plate (e.g., KA01AB1234)
  - Confidence score (e.g., 92.45%)

**Confidence** indicates the level of certainty the OCR model has in the accuracy of the detected text.

## Libraries Used

| Library     | Purpose                                      |
|-------------|----------------------------------------------|
| `cv2`       | For video and image processing               |
| `os`        | Handling file operations                     |
| `re`        | Regular expressions for validating plates    |
| `easyocr`   | Optical Character Recognition engine         |
| `time`      | Generating time-based frame information      |

