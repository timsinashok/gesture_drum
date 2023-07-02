import cv2

def display_video():
    # Open the default camera (index 0)
    cap = cv2.VideoCapture(0)

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Failed to open camera")
        return

    # Create a named window to display the video
    cv2.namedWindow("Video", cv2.WINDOW_NORMAL)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Check if the frame was successfully captured
        if not ret:
            print("Failed to capture frame")
            break

        # Display the frame in the "Video" window
        cv2.imshow("Video", frame)

        # Exit loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and destroy all windows
    cap.release()
    cv2.destroyAllWindows()

# Call the display_video() function to show live video stream
display_video()
