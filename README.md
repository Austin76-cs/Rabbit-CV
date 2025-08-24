🐇 Real-Time Rabbit Detection with YOLOv8
This project uses a custom-trained YOLOv8 model to detect rabbits in real-time from a webcam feed. The script captures video, processes each frame through the model, and displays the output with bounding boxes around any detected rabbits.

🌟 Features
Real-Time Detection: Utilizes a live webcam feed for immediate object detection.

Custom YOLOv8 Model: Employs a fine-tuned model (best.pt) specifically trained to recognize rabbits.

High-Resolution Support: Configured to run at a 1280x720 resolution.

Hardware Acceleration: Automatically uses a CUDA-enabled GPU if available for faster processing, otherwise falls back to the CPU.

🛠️ Prerequisites
Before you begin, ensure you have the following installed:

Python 3.8 or higher

A webcam connected to your computer

You will also need the following Python libraries:

opencv-python

torch

ultralytics

⚙️ Installation
Clone the repository (or download the files):

git clone [https://github.com/your-username/your-repository-name.git](https://github.com/Austin76-cs/Rabbit-CV)](https://github.com/Austin76-cs/Rabbit-CV.git)
cd your-repository-name

Install the required libraries using pip:

pip install opencv-python torch ultralytics

(Note: For GPU support with PyTorch, please follow the specific installation instructions on the official PyTorch website to get the correct version for your CUDA setup.)

Place the model file:
Make sure the custom model file, best.pt, is in the same directory as the Python script.

▶️ Usage
To run the rabbit detection script, execute the following command in your terminal from the project's root directory:

python your_script_name.py

A window titled "YOLOv8 Rabbit Detection" will open, showing your webcam feed.

The model will draw bounding boxes and labels on the screen whenever a rabbit is detected.

The confidence threshold is set to 0.35, meaning only detections with 35% or higher confidence will be shown.

🛑 Controls
To stop the script and close the application, press the 'q' key while the webcam window is active.
