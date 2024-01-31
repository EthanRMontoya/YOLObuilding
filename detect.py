import os
from ultralytics import YOLO
import cv2

# Set the path to the video file
video_path = 'tanky.mov'

# Load the video
cap = cv2.VideoCapture(video_path)
ret, frame = cap.read()

# Set the path to the YOLO model
model_path = os.path.join('.', 'runs', 'detect', 'train19', 'weights', 'best.pt')

# Load the YOLO model
model = YOLO(model_path)

# Set the detection threshold (adjust as needed)
threshold = 0.01  # Increase this value for lower confidence detection

# Create a window to display the video
cv2.namedWindow('Object Detection', cv2.WINDOW_NORMAL)

while ret:
    # Perform object detection on the current frame
    results = model(frame)[0]

    # Process the detected objects
    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        # Draw bounding box and label regardless of the score
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
        cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

    # Display the current frame
    cv2.imshow('Object Detection', frame)

    # Read the next frame
    ret, frame = cap.read()

    # Check for the 'q' key to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
