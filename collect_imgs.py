import os
import cv2

DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 3
dataset_size = 100

# Start with camera index 0 and adjust if needed
cap = cv2.VideoCapture(0)  # Change to 1, 2, etc., if 0 doesn't work

if not cap.isOpened():
    print("Error: Could not open video source.")
    exit()

for j in range(number_of_classes):
    class_dir = os.path.join(DATA_DIR, str(j))
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)

    print('Collecting data for class {}'.format(j))

    # Initial screen to wait for 'Q' press to start collecting images
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        cv2.putText(frame, 'Ready? Press "Q" to start!', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
        cv2.imshow('frame', frame)

        # Check for 'q' or 'Q' key press (case insensitive)
        if cv2.waitKey(1) & 0xFF in [ord('q'), ord('Q')]:
            print("Starting to collect images for class {}".format(j))
            break

    # Collect images for the current class
    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        cv2.imshow('frame', frame)
        cv2.imwrite(os.path.join(class_dir, '{}.jpg'.format(counter)), frame)
        counter += 1

        # Allow 'Q' to exit early if needed
        if cv2.waitKey(1) & 0xFF in [ord('q'), ord('Q')]:
            print("Early exit from data collection.")
            break

cap.release()
cv2.destroyAllWindows()
