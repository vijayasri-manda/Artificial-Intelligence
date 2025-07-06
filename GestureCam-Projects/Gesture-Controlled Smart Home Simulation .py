import cv2
import mediapipe as mp
import tkinter as tk
from threading import Thread

# Initialize MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Tkinter GUI
root = tk.Tk()
root.title("💡 Smart Home - Light Control")
root.geometry("300x150")
status_label = tk.Label(root, text="Light is OFF", font=("Arial", 18))
status_label.pack(pady=30)

light_on = False

def update_status(is_on):
    global light_on
    light_on = is_on
    status_label.config(text="Light is ON" if is_on else "Light is OFF", fg="green" if is_on else "red")

def detect_gesture():
    global light_on
    cap = cv2.VideoCapture(0)

    while True:
        success, frame = cap.read()
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb_frame)

        if result.multi_hand_landmarks:
            for handLms in result.multi_hand_landmarks:
                lm = handLms.landmark

                # Thumb and finger tip indexes
                thumb_tip = lm[4]
                index_tip = lm[8]
                middle_tip = lm[12]
                ring_tip = lm[16]
                pinky_tip = lm[20]

                # Simple fist detection (all fingers curled)
                if (index_tip.y > lm[6].y and
                    middle_tip.y > lm[10].y and
                    ring_tip.y > lm[14].y and
                    pinky_tip.y > lm[18].y):
                    if not light_on:
                        root.after(0, update_status, True)
                else:
                    if light_on:
                        root.after(0, update_status, False)

                mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

        cv2.imshow("Gesture Camera", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

# Start gesture detection in background thread
Thread(target=detect_gesture, daemon=True).start()

root.mainloop()
