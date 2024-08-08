
#Run on nano
import cv2

camera = cv2.VideoCapture(0)
if not camera.isOpened():
    print("Not found camera")

fourcc = cv2.VideoWriter_fourcc(*"PIM1")
out = cv2.VideoWriter("myvideo.avi", fourcc, 30, (640,480))

## write the number of seconds inside the loop
#120 means 4 seconds (120/30=4)
for _ in range(120):
    ret, frame = camera.read()
    #framGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
    out.write(frame)

    cv2.imshow("myvideo", frame)

camera.release()
cv2.destroyAllWindows()
