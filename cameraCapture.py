import cv2

cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("❌ Camera not recognized! Check if it is plugged in.")
else:
    # Only run the loop if the camera works
    print("✅ Camera found. Press 'q' to quit.")
    
    while True:
        ret, frame = cam.read()
        
        if not ret:
            print("Failed to grab frame")
            break
        
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("My Camera", gray_frame)
        
        # Proper way to exit loop
        if cv2.waitKey(1) == ord('q'):
            break

# Cleanup happens here naturally
cam.release()
cv2.destroyAllWindows()