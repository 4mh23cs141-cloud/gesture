# Hand Gesture Laptop Controller

## 📌 Project Overview

This project allows you to control your laptop using **hand gestures through a webcam**.
It uses computer vision to detect hand movements and converts them into system actions such as moving the mouse, clicking, adjusting volume, zooming, taking screenshots, and drawing in the air.

The system detects hand landmarks using **MediaPipe** and performs actions using **PyAutoGUI**.

---

## 🚀 Features

* 🖱 **Mouse Control** – Move the cursor using your index finger
* 👆 **Mouse Click** – Touch thumb and index finger to click
* 🔊 **Volume Control** – Increase or decrease volume using finger distance
* 🔍 **Zoom In / Zoom Out** – Control zoom with hand gestures
* 📸 **Screenshot Capture** – Take a screenshot using a gesture
* ✍ **Air Drawing** – Draw on the screen using your finger
* 🎥 **Real-Time Webcam Detection**

---

## 🛠 Technologies Used

* Python
* OpenCV
* MediaPipe
* PyAutoGUI
* NumPy

---

## 📂 Project Structure

```
HandGestureLaptopControl/
│
├── basic.py          # Main Python program
├── README.md         # Project documentation
├── screenshot.png    # Example screenshot (optional)
```

---

## ⚙️ Installation

1. Clone the repository

```
git clone https://github.com/your-username/hand-gesture-laptop-control.git
```

2. Go to the project folder

```
cd hand-gesture-laptop-control
```

3. Install required libraries

```
pip install opencv-python mediapipe pyautogui numpy
```

---

## ▶️ Run the Project

Run the Python script:

```
python basic.py
```

Your webcam will open and start detecting hand gestures.

Press **Q** to exit the program.

---

## ✋ Gesture Controls

| Gesture             | Action      |
| ------------------- | ----------- |
| Move index finger   | Move mouse  |
| Thumb + index close | Mouse click |
| Fingers far apart   | Volume up   |
| Fingers closer      | Volume down |
| Very far apart      | Screenshot  |
| Move index finger   | Draw in air |

---

## 💡 Applications

* Touchless computer control
* Accessibility for people with disabilities
* Smart home systems
* Gesture-based human-computer interaction

---

## 🔮 Future Improvements

* Add more gesture commands
* Control music and media players
* Use machine learning for better gesture recognition
* Add GUI interface

---

## 👨‍💻 Author

Punith
Computer Science Engineering Student

---

⭐ If you like this project, give it a star on GitHub!
