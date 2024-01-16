import cv2
import pyautogui
import numpy as np

# create resolution of the screen
rs = pyautogui.size()

# filename to store the recording for ex - D:\aakash\Live_Recording.mp4
filename = input("Enter file name and path: ")

# fix the frame rate
fps = 60.0

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter(filename, fourcc, fps, rs)

cv2.namedWindow('Live_Recording', cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live_Recording", (600, 400))

try:
    while True:
        img = pyautogui.screenshot()
        f = np.array(img)
        f = cv2.cvtColor(f, cv2.COLOR_BGR2RGB)  # Correct color conversion
        output.write(f)
        cv2.imshow("Live_Recording", f)

        if cv2.waitKey(1) == ord("q"):
            break
finally:
    output.release()
    cv2.destroyAllWindows()
