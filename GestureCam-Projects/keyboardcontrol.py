import cv2
import mediapipe as mp
import tkinter as tk
from pynput.keyboard import Controller
import threading
import time
import math

# Initialize keyboard controller
keyboard = Controller()

# MediaPipe hands setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Keyboard layout (QWERTY)
KEYS = [
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M', 'Space']
]

# Create main window
root = tk.Tk()
root.title("🖥️ Gesture Virtual Keyboard")
root.geometry("800x400")
root.config(bg="black")

typed_text = tk.StringVar()
typed_text.set("")

# Frame to hold keys
frame_keys = tk.Frame(root, bg="black")
frame_keys.pack(pady=20)

# Draw keys on Tkinter
button_dict = {}
for row_index, row_keys in enumerate(KEYS):
    row_frame = tk.Frame(frame_keys, bg="black")
    row_frame.pack()
    for key in row_keys:
        btn = tk.Label(row_frame, text=key, font=("Helvetica", 20), bg="gray20", fg="white", width=5, height=2, relief="raised", bd=3)
        btn.pack(side="left", padx=5, pady=5)
        button_dict[key] = btn

# Text box to show typed text
text_box = tk.Label(root, textvariable=typed_text, font=("Helvetica", 24), bg="black", fg="white", relief="sunken", width=50, height=2)
text_box.pack(pady=10)

# Helper function to calculate distance between two points
def distance(pt1, pt2):
    return math.sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)

# Gesture keyboard thread
def gesture_keyboard():
    cap = cv2.VideoCapture(0)
    pressed_key = None
    debounce_time = 0.5  # seconds
    last_press = time.time() - debounce_time

    while True:
        success, frame = cap.read()
        if not success:
            continue
        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = hands.process(rgb)

        if results.multi_hand_landmarks:
            handLms = results.multi_hand_landmarks[0]
            lm = handLms.landmark

            # Index finger tip coordinates
            index_finger_tip = lm[8]
            x_px = int(index_finger_tip.x * w)
            y_px = int(index_finger_tip.y * h)

            # Thumb tip coordinates
            thumb_tip = lm[4]
            thumb_x = int(thumb_tip.x * w)
            thumb_y = int(thumb_tip.y * h)

            # Detect pinch (distance between index fingertip and thumb tip)
            dist = distance((x_px, y_px), (thumb_x, thumb_y))

            # Map finger position to keyboard buttons
            # We'll check which key's Tkinter widget bbox contains (x_px, y_px)

            found_key = None
            for key, btn in button_dict.items():
                bx1 = btn.winfo_rootx() - root.winfo_rootx()
                by1 = btn.winfo_rooty() - root.winfo_rooty()
                bx2 = bx1 + btn.winfo_width()
                by2 = by1 + btn.winfo_height()
                # Since finger coords from webcam (0,w),(0,h), and button coords from window,
                # We must map webcam coords to window coords roughly
                # We'll map webcam frame size (w,h) to tkinter window size (root.winfo_width(), root.winfo_height())

                # Get scale ratios
                scale_x = root.winfo_width() / w
                scale_y = root.winfo_height() / h

                mapped_x = int(x_px * scale_x)
                mapped_y = int(y_px * scale_y)

                if bx1 <= mapped_x <= bx2 and by1 <= mapped_y <= by2:
                    found_key = key
                    break

            # Highlight the hovered key
            for key, btn in button_dict.items():
                if key == found_key:
                    btn.config(bg="dodgerblue")
                else:
                    btn.config(bg="gray20")

            # If pinch detected and debounce time passed
            if dist < 40 and found_key is not None and (time.time() - last_press) > debounce_time:
                last_press = time.time()
                if found_key == "Space":
                    typed_text.set(typed_text.get() + " ")
