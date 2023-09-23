# Sign-Language-Recognition-with-YOLO-V8

This is a project that uses YOLOv8, a state-of-the-art object detection model, to recognize sign language alphabets from images or videos. The project uses PyTorch as the deep learning framework and OpenCV as the computer vision library.

## Features

- The project can detect and recognize 26 sign language alphabets (A-Z) from images or videos using YOLOv8.
- The project can display the detected alphabets and their confidence scores on the screen using OpenCV.
- The project can also output the detected alphabets as text or speech using pyttsx3.

## Requirements

- Python 3.8 (or higher)
- PyTorch 1.9.0 (or higher)
- OpenCV 4.5.3 (or higher)
- pyttsx3 2.90 (or higher)

## Installation

- Clone this repository to your local machine using the command:

    ```bash
    git clone https://github.com/Mochoye/Sign-Language-Recognition-with-YOLO-V8.git
    ```

- Download the pretrained YOLOv8 model from [here] and place it in the **weights** folder.
- Install the required packages using the command:

    ```bash
    pip install ultralytics 
    ```

## Usage

- Run the main script using the command:

    ```bash
    python detect.py --source [image/video path or 0 for webcam]
    ```

- The script will detect and recognize the sign language alphabets from the source and display them on the screen.
- The script will also output the detected alphabets as text or speech depending on the **--output** argument.


## Feedback

If you have any feedback or questions about this project, you can leave a comment on the discussion page [here].
