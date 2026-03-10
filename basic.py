import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import math
import time

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

screen_w, screen_h = pyautogui.size()

cap = cv2.VideoCapture(0)

canvas = np.zeros((480, 640, 3), dtype=np.uint8)

screenshot_time = 0

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    h, w, c = img.shape

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:

            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

            lm = handLms.landmark

            x1, y1 = int(lm[8].x * w), int(lm[8].y * h)   # index finger
            x2, y2 = int(lm[4].x * w), int(lm[4].y * h)   # thumb

            # ----------------
            # Mouse movement
            # ----------------
            screen_x = int(lm[8].x * screen_w)
            screen_y = int(lm[8].y * screen_h)

            pyautogui.moveTo(screen_x, screen_y)

            # ----------------
            # Distance
            # ----------------
            length = math.hypot(x2 - x1, y2 - y1)

            # draw line between fingers
            cv2.line(img, (x1,y1), (x2,y2), (255,0,0), 2)

            # ----------------
            # Mouse click
            # ----------------
            if length < 30:
                pyautogui.click()
                time.sleep(0.3)

            # ----------------
            # Volume control
            # ----------------
            if length > 120:
                pyautogui.press("volumeup")

            if length < 50:
                pyautogui.press("volumedown")

            # ----------------
            # Zoom
            # ----------------
            if length > 170:
                pyautogui.hotkey("ctrl","+")  # zoom in

            if length < 20:
                pyautogui.hotkey("ctrl","-")  # zoom out

            # ----------------
            # Screenshot
            # ----------------
            if length > 200 and time.time() - screenshot_time > 2:
                pyautogui.screenshot("gesture_screenshot.png")
                screenshot_time = time.time()
                print("Screenshot taken")

            # ----------------
            # Air Drawing
            # ----------------
            cx = int(lm[8].x * 640)
            cy = int(lm[8].y * 480)

            cv2.circle(canvas, (cx,cy), 5, (0,255,0), -1)

    cv2.imshow("Webcam", img)
    cv2.imshow("Air Draw", canvas)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()