# ✅ Supported Gestures:
# ✊ Fist (All fingers folded)
#
# ✋ Open Hand (All fingers extended)
#
# 👆  Pointing (Only index finger up)
#
# 👍 Thumbs Up
#
# 👎 Thumbs Down

#  q for closing cam


import cv2
import mediapipe as mp
# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1,min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils
# Finger tip landmark indexes
fingers_tips_ids = [4, 8, 12, 16, 20]

# Define function to detect gesture
def get_gesture(hand_landmarks):
    fingers = []

    # Thumb
    if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
        fingers.append(1)  # Open
    else:
        fingers.append(0)  # Closed

    # Other fingers
    for tip in [8, 12, 16, 20]:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            fingers.append(1)  # Open
        else:
            fingers.append(0)  # Closed

    # Interpret gesture based on finger states
    if fingers == [0, 0, 0, 0, 0]:
        return "Fist"
    elif fingers == [1, 1, 1, 1, 1]:
        return "Open Hand"
    elif fingers == [0, 1, 0, 0, 0]:
        return "Pointing"
    elif fingers == [1, 0, 0, 0, 0]:
        return "Thumbs Up"
    elif fingers == [0, 0, 0, 0, 1]:
        return "Thumbs Down"
    else:
        return "Unknown"

# Start webcam
cap = cv2.VideoCapture(0)
while True:
    success, image = cap.read()
    if not success:
        break


    image = cv2.flip(image, 1)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_image)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(image, handLms, mp_hands.HAND_CONNECTIONS)

            # Detect gesture
            gesture = get_gesture(handLms)
            cv2.putText(image, f'Gesture: {gesture}', (10, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Hand Gesture Recognition", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
