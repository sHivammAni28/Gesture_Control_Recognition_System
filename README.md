# Gesture Control Recognition System

A computer vision-based application that allows you to control your computer's volume and screen brightness using hand gestures captured through your webcam.

## Features

- **Volume Control**: Use your right hand to adjust system volume
- **Brightness Control**: Use your left hand to adjust screen brightness
- **Real-time Hand Detection**: Powered by MediaPipe for accurate hand landmark detection
- **Visual Feedback**: Live display of control bars and percentage values
- **Intuitive Gestures**: Simple thumb-to-index finger distance controls

## How It Works

The application uses computer vision to detect hand landmarks and calculates the distance between your thumb and index finger to control different system functions:

- **Right Hand (Right side of screen)**: Controls system volume
- **Left Hand (Left side of screen)**: Controls screen brightness
- **Gesture**: Pinch your thumb and index finger together to decrease, spread them apart to increase

## Requirements

### Python Dependencies

```
cv2 (OpenCV)
mediapipe
numpy
pycaw
screen-brightness-control
comtypes
```

### System Requirements

- Windows OS (for audio control via pycaw)
- Webcam/Camera
- Python 3.7+

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd Gesture_control
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv mp_env
   mp_env\Scripts\activate  # On Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install opencv-python mediapipe numpy pycaw screen-brightness-control comtypes
   ```

## Usage

1. **Run the application**:
   ```bash
   python Gesture_Control.py
   ```

2. **Position yourself in front of the camera**:
   - Ensure good lighting for better hand detection
   - Keep your hands visible in the camera frame

3. **Control gestures**:
   - **Volume**: Use your right hand on the right side of the screen
   - **Brightness**: Use your left hand on the left side of the screen
   - **Gesture**: Vary the distance between thumb and index finger

4. **Exit**: Press the spacebar to quit the application

## Visual Interface

- **Hand Landmarks**: Blue circles and lines show detected hand positions
- **Control Bars**: 
  - Red bar on the right for volume control
  - Yellow bar on the left for brightness control
- **Percentage Display**: Real-time percentage values for both controls

## Technical Details

### Hand Detection
- Uses MediaPipe Hands solution for real-time hand landmark detection
- Supports detection of up to 2 hands simultaneously
- Tracks 21 landmarks per hand

### Control Mapping
- **Distance Range**: 30-350 pixels between thumb and index finger
- **Volume Range**: Maps to system volume range (typically -65.25 to 0.0 dB)
- **Brightness Range**: Maps to 0-100% screen brightness

### Hand Side Detection
- Determines hand side based on the mean x-coordinate of all hand landmarks
- Right side of screen (x > width/2) = Volume control
- Left side of screen (x ≤ width/2) = Brightness control

## Troubleshooting

### Common Issues

1. **Camera not detected**:
   - Check if your camera is working and not being used by another application
   - Try changing the camera index in `cv2.VideoCapture(0)` to `cv2.VideoCapture(1)` or higher

2. **Hand detection not working**:
   - Ensure good lighting conditions
   - Keep hands clearly visible and unobstructed
   - Try adjusting the `max_num_hands` parameter in MediaPipe

3. **Audio control not working**:
   - Ensure you're running on Windows (pycaw is Windows-specific)
   - Check if you have proper audio devices configured

4. **Brightness control not working**:
   - Some systems may require administrator privileges
   - External monitors might not support software brightness control

## Dependencies Explanation

- **OpenCV (cv2)**: Computer vision library for camera capture and image processing
- **MediaPipe**: Google's framework for hand landmark detection
- **NumPy**: Numerical operations and array handling
- **pycaw**: Windows Core Audio API wrapper for volume control
- **screen-brightness-control**: Cross-platform screen brightness control
- **comtypes**: COM interface support for Windows audio control

## Customization

You can modify the following parameters in the code:

- **Distance thresholds**: Change the `[30, 350]` range for gesture sensitivity
- **Hand detection confidence**: Adjust MediaPipe parameters
- **Visual elements**: Modify colors, sizes, and positions of UI elements
- **Control ranges**: Adjust volume and brightness mapping ranges

## Future Enhancements

- Support for additional gestures (multiple fingers, hand orientation)
- Cross-platform audio control (macOS, Linux)
- Gesture customization interface
- Multiple monitor brightness control
- Gesture recording and playback

## License

This project is open source. Please check the license file for more details.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## Acknowledgments

- MediaPipe team for the excellent hand detection framework
- OpenCV community for computer vision tools
- Contributors to pycaw and screen-brightness-control libraries
