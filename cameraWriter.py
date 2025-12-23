import cv2

# 1. Initialize the camera (0 is usually the default webcam)
cam = cv2.VideoCapture(0)

# 2. Force resolution to 640x480
# Note: Some cameras might not support exact 640x480 and will choose the closest one.
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 3. Get the actual resolution being used
# IMPORTANT: The VideoWriter size must match the input frame size exactly,
# otherwise the video file will be empty or corrupted.
width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(f"Recording Resolution: {width}x{height}")

# 4. Define the codec and create VideoWriter object
# 'mp4v' is the standard codec for .mp4 files on Windows/Linux
fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
fps = 20.0 
output_filename = "recording.mp4"

# Create the writer object
writer = cv2.VideoWriter(output_filename, fourcc, fps, (width, height))

try:
    if not cam.isOpened():
        print("❌ Error: Camera not found.")
    else:
        print(f"✅ Recording started: Saving to '{output_filename}'")
        print("Click the video window and press 'q' to stop recording.")

        while True:
            # Capture frame-by-frame
            ret, frame = cam.read()

            if not ret:
                print("❌ Error: Can't receive frame (stream end?). Exiting ...")
                break

            # Write the frame to the video file
            writer.write(frame)

            # Display the resulting frame
            cv2.imshow('Video Recording', frame)

            # Press 'q' to exit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("Stop signal received.")
                break

finally:
    # 5. Cleanup Resources
    # This block runs even if the code crashes, ensuring the file saves correctly.
    cam.release()
    writer.release()  # <--- Crucial! Closes the file stream.
    cv2.destroyAllWindows()
    print("✅ Resources released. Video saved successfully.")