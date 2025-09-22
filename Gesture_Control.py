import cv2
import mediapipe as mp
from math import hypot
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import screen_brightness_control as sbc
import numpy as np

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=2)
mpDraw = mp.solutions.drawing_utils

# Audio
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volMin, volMax = volume.GetVolumeRange()[:2]

volbar = 400
volper = 0
brightbar = 400
brightper = 0

while True:
    success, img = cap.read()
    if not success:
        print("Error: Failed to capture image.")
        break

    # Flip image horizontally
    img = cv2.flip(img, 1)

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    if results.multi_hand_landmarks:
        for hand_no, handlandmark in enumerate(results.multi_hand_landmarks):
            hand_lmList = []
            for id, lm in enumerate(handlandmark.landmark):
                h, w, _ = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                hand_lmList.append([id, cx, cy])
            
            mpDraw.draw_landmarks(img, handlandmark, mpHands.HAND_CONNECTIONS)

            if len(hand_lmList) > 8:
                x1, y1 = hand_lmList[4][1], hand_lmList[4][2]  # Thumb
                x2, y2 = hand_lmList[8][1], hand_lmList[8][2]  # Index finger

                cv2.circle(img, (x1, y1), 13, (255, 0, 0), cv2.FILLED)
                cv2.circle(img, (x2, y2), 13, (255, 0, 0), cv2.FILLED)
                cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)

                length = hypot(x2 - x1, y2 - y1)
                cx_mean = np.mean([lm[1] for lm in hand_lmList])

                # Right hand = right side
                if cx_mean > img.shape[1] // 2:  
                    vol = np.interp(length, [30, 350], [volMin, volMax])
                    volbar = np.interp(length, [30, 350], [400, 150])
                    volper = np.interp(length, [30, 350], [0, 100])
                    volume.SetMasterVolumeLevel(vol, None)

                    # Vertical bar right
                    cv2.rectangle(img, (img.shape[1]-50, 150), (img.shape[1]-20, 400), (0,0,255), 4)
                    cv2.rectangle(img, (img.shape[1]-50, int(volbar)), (img.shape[1]-20, 400), (0,0,255), cv2.FILLED)
                    cv2.putText(img, f"Volume: {int(volper)}%", (img.shape[1]-150, 140), cv2.FONT_ITALIC, 1, (0,255,98), 3)

                # Left hand = left side
                else:  
                    bright = np.interp(length, [30, 350], [0, 100])
                    brightbar = np.interp(length, [30, 350], [400, 150])
                    brightper = np.interp(length, [30, 350], [0, 100])
                    sbc.set_brightness(int(brightper))

                    # Vertical bar left
                    cv2.rectangle(img, (20, 150), (50, 400), (255,255,0), 4)
                    cv2.rectangle(img, (20, int(brightbar)), (50, 400), (255,255,0), cv2.FILLED)
                    cv2.putText(img, f"Bright: {int(brightper)}%", (60, 140), cv2.FONT_ITALIC, 1, (0,255,255), 3)

    cv2.imshow('Hand Control', img)
    if cv2.waitKey(1) & 0xFF == ord(' '):
        break

cap.release()
cv2.destroyAllWindows()
