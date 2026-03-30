import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

cap = cv2.VideoCapture(0)

def count_fingers(hand_landmarks):
    finger_tips = [4, 8, 12, 16, 20]
    fingers = []

    # Thumb
    if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other fingers
    for tip in finger_tips[1:]:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers


while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb)

    gesture = ""

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:

            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            fingers = count_fingers(hand_landmarks)

            # Gesture Detection
            if fingers == [0,0,0,0,0]:
                gesture = "FIST ✊"

            elif fingers == [0,1,0,0,0]:
                gesture = "ONE ☝️"

            elif fingers == [0,1,1,0,0]:
                gesture = "TWO ✌️"

            elif fingers == [0,1,1,1,0]:
                gesture = "THREE 🤟"

            elif fingers == [0,1,1,1,1]:
                gesture = "FOUR 🖖"

            elif fingers == [1,1,1,1,1]:
                gesture = "FIVE 🖐️"

            elif fingers == [1,0,0,0,0]:

                thumb_tip = hand_landmarks.landmark[4]
                wrist = hand_landmarks.landmark[0]

                if thumb_tip.y < wrist.y:
                    gesture = "THUMBS UP 👍"
                else:
                    gesture = "THUMBS DOWN 👎"

            elif fingers == [1,0,0,0,1]:
                gesture = "ROCK 🤘"

            elif fingers == [1,1,0,0,1]:
                gesture = "OK SIGN 👌"

            else:
                gesture = "UNKNOWN"

    cv2.putText(
        frame,
        gesture,
        (20, 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.5,
        (0, 255, 0),
        3
    )

    cv2.imshow("AI Hand Gesture Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('a'):
        break

cap.release()
cv2.destroyAllWindows()