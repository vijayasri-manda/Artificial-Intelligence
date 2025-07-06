import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.8)
mp_draw = mp.solutions.drawing_utils

# Get screen size
screen_width, screen_height = pyautogui.size()
prev_x, prev_y = 0, 0
smoothening = 5

# Initialize webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height

click_threshold = 20  # Distance threshold for clicking

def get_position(landmarks, idx, frame):
    h, w, _ = frame.shape
    cx = int(landmarks.landmark[idx].x * w)
    cy = int(landmarks.landmark[idx].y * h)
    return cx, cy

while True:
    success, frame = cap.read()
    frame = cv2.flip(frame, 1)  # Mirror image
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            index_x, index_y = get_position(hand_landmarks, 8, frame)
            thumb_x, thumb_y = get_position(hand_landmarks, 4, frame)

            # Convert coordinates to screen position
            screen_x = np.interp(index_x, (100, 540), (0, screen_width))
            screen_y = np.interp(index_y, (100, 400), (0, screen_height))

            # Smooth movement
            cur_x = prev_x + (screen_x - prev_x) / smoothening
            cur_y = prev_y + (screen_y - prev_y) / smoothening
            pyautogui.moveTo(cur_x, cur_y)
            prev_x, prev_y = cur_x, cur_y

            # Draw landmarks
            cv2.circle(frame, (index_x, index_y), 10, (255, 0, 0), cv2.FILLED)
            cv2.circle(frame, (thumb_x, thumb_y), 10, (255, 0, 0), cv2.FILLED)

            # Click detection
            dist = np.hypot(index_x - thumb_x, index_y - thumb_y)
            if dist < click_threshold:
                pyautogui.click()
                cv2.circle(frame, (index_x, index_y), 15, (0, 255, 0), cv2.FILLED)
                time.sleep(0.25)  # Debounce

    # Show webcam feed
    cv2.imshow("🖐️ Virtual Mouse Controller", frame)
    if cv2.waitKey(1) & 0xFF == 27:  # ESC to quit
        break

cap.release()
cv2.destroyAllWindows()

# Move mouse with index finger
#
# Click with thumb and index finger pinch
#
# Adjustable screen dimensions
#
# Smooth cursor movement
#
