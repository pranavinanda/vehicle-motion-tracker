# Vehicle Motion Tracker Using Optical Flow

## 1. Project Description
This project tracks the movement of vehicles in a video using Python and OpenCV. It uses the Lucas-Kanade Optical Flow algorithm to track selected feature points across consecutive video frames.

The movement of these points is displayed using red dots and green motion trails.

## 2. Technologies Used
- Python 3.12.3
- OpenCV
- NumPy
- Visual Studio Code

## 3. Installation Requirements

Install the required Python libraries using:

```bash
pip install opencv-python numpy
```

## 4. Project Files
- `vehicle_tracker.py` – Main Python source code.
- `input_video.mp4` – Input video used for vehicle tracking.
- `README.md` – Project documentation.

## 5. How to Run the Project

1. Install Python and Visual Studio Code.
2. Install the required libraries.
3. Place the input video in the same folder as the Python program.
4. Make sure the video filename is `input_video.mp4`.
5. Open the project folder in Visual Studio Code.
6. Run the Python file:

```bash
python vehicle_tracker.py
```

7. A window will display the video with tracked feature points and motion trails.
8. Press **Q** to close the output window.

## 6. Working Principle

The project follows these steps:

1. Reads the input video frame by frame.
2. Converts each frame into grayscale.
3. Defines a Region of Interest (ROI) to focus feature detection on a selected area.
4. Detects trackable feature points using the Shi-Tomasi corner detection method.
5. Tracks these points between consecutive frames using the Pyramidal Lucas-Kanade Optical Flow algorithm.
6. Calculates the displacement of tracked points.
7. Displays red dots at tracked positions and green lines representing their movement.
8. Periodically detects new feature points to maintain tracking.

## 7. Output
The output is a video window showing tracked feature points and their motion trails, helping visualize vehicle movement.

## 8. Limitations
- The program tracks feature points rather than identifying complete vehicles.
- It does not calculate actual vehicle speed in km/h.
- Tracking accuracy depends on video quality, lighting, and movement.
- It does not perform vehicle counting or vehicle classification.

## 9. Conclusion
This project demonstrates vehicle motion visualization using computer vision techniques, particularly feature detection and optical flow tracking.