# Image Text Extraction using Tesseract OCR

This project focuses on extracting text from images using the Tesseract OCR (Optical Character Recognition) engine. It captures live video frames, allows the user to select a frame, and processes the selected image to extract text.

## Getting Started

To get started with this project, follow these steps:

1. Install the required dependencies and libraries mentioned below:

   - Python: The primary programming language for implementing the image text extraction.
   - OpenCV: A computer vision library used for capturing live video frames and image processing.
   - PIL (Python Imaging Library): A library for image processing and manipulation.
   - pytesseract: A Python wrapper for the Tesseract OCR engine.
   - pyttsx3: A library for text-to-speech conversion.

2. Connect a webcam or ensure that your device has a camera to capture live video frames.

3. Run the provided Python script (`text_extraction.py`) to start the program.

4. The program will open a live video window. Press the SPACE key to capture a frame when desired.

5. The captured image will be processed to extract text using the Tesseract OCR engine.

6. The extracted text will be displayed on the terminal console and as an overlay on the processed image.

7. Additionally, the extracted text will be converted to speech using the pyttsx3 library and played through the system's speakers.

## Technologies Used

The following technologies and libraries are used in this project:

- Python: The primary programming language for implementing the image text extraction.
- OpenCV: A computer vision library used for capturing live video frames and image processing.
- PIL (Python Imaging Library): A library for image processing and manipulation.
- Tesseract OCR: An optical character recognition engine for extracting text from images.
- pytesseract: A Python wrapper for the Tesseract OCR engine.
- pyttsx3: A library for text-to-speech conversion.

## Usage

Follow the instructions below to use the image text extraction program:

1. Run the Python script (`text_extraction.py`).

2. The live video window will open, displaying the camera feed.

3. Press the SPACE key to capture a frame when desired.

4. The captured image will be processed, and the extracted text will be displayed on the terminal console.

5. The processed image with the text overlay will be displayed in a separate window.

6. The extracted text will be converted to speech and played through the system's speakers.

7. Repeat the process to capture and extract text from different frames.

## Future Enhancements

Here are some potential areas for future enhancements:

- Implement image preprocessing techniques, such as image denoising, resizing, or enhancement, to improve the accuracy of text extraction from images.
- Explore different OCR engines or advanced OCR techniques to compare and enhance the text extraction performance.
- Implement text classification or entity recognition techniques to extract specific types of information from the extracted text.
- Develop a graphical user interface (GUI) for the image text extraction program, providing a more user-friendly and intuitive interface.

