# Detect hands
if result_hands.multi_hand_landmarks:
    if detect_hands_on_wheel(result_hands.multi_hand_landmarks):
        detected_objects.append("Hands on Wheel")
    else:
        detected_objects.append("Hands off Wheel")
        
    for hand_landmarks in result_hands.multi_hand_landmarks:
        hand_side = get_hand_side(hand_landmarks)
        detected_objects.append(hand_side)
        
        # Draw landmarks
        mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        
        # Calculate bounding box for hand
        x_min = int(min([landmark.x for landmark in hand_landmarks.landmark]) * w)
        y_min = int(min([landmark.y for landmark in hand_landmarks.landmark]) * h)
        x_max = int(max([landmark.x for landmark in hand_landmarks.landmark]) * w)
        y_max = int(max([landmark.y for landmark in hand_landmarks.landmark]) * h)
        
        # Draw bounding box
        color = (0, 255, 255)
        cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), color, 2)
        
        # Draw label
        text = "%s" % (hand_side)
        cv2.putText(frame, text, (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
