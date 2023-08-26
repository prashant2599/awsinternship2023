import cv2
import numpy as np

# Open the webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the frame
    cv2.imshow('Video Stream', frame)
    cv2.waitKey()
        

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
