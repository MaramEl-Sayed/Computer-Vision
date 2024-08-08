import cv2
import os

# Open the video file
video_path = '.\\AutoCarCliberation\\soda1.avi'
cap = cv2.VideoCapture(video_path)


# Create a folder to save frames
output_folder = '.\\AutoCarCliberation\\output_frames'
os.makedirs(output_folder, exist_ok=True)

# Read frames and save them
frame_count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1
    frame_filename = f"{output_folder}/frame_{frame_count:04d}.jpg"
    cv2.imwrite(frame_filename, frame)

# Release the video capture object
cap.release()

print(f"{frame_count} frames saved in {output_folder}")