import cv2
import numpy as np
cams_test = 10
for i in range(0, cams_test):
    cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)
    test=cap.isOpened()
    print("i : "+str(i)+" /// result: "+str(test))
    
    
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# Check if the webcam is opened correctly
if not cam.isOpened():
    raise IOError("Cannot open webcam")
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cv2.namedWindow("test")
cv2.resizeWindow("test",1280,720)
ret, frame = cam.read()
print(frame.shape)
ret,frame_still= cam.read()
img_counter = 0
frame_still = cv2.GaussianBlur(frame_still,(35,35),0)
bins=np.array([0,51,102,153,204,255])
frame_still[:,:,:] = np.digitize(frame_still[:,:,:],bins,right=True)*51
greyscale2 = cv2.cvtColor(frame_still, cv2.COLOR_BGR2GRAY)
Thresh=100
while True:
    ret, frame = cam.read()
    frame = cv2.GaussianBlur(frame,(35,35),0)
    bins=np.array([0,51,102,153,204,255])
    frame[:,:,:] = np.digitize(frame[:,:,:],bins,right=True)*51
    greyscale1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   

    
    ret,background = cv2.threshold(greyscale1-greyscale2,200,255,cv2.THRESH_BINARY)
    #ret, thresh_img = cv2.threshold(greyscale2, 200, 255, cv2.THRESH_BINARY_INV)
    if not ret:
        print("failed to grab frame")
        break
        
    cv2.imshow("test", background)
    cv2.resizeWindow("test",1280,920)
    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed 
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        ret, frame_still = cam.read()
        frame_still = cv2.GaussianBlur(frame_still,(35,35),0)
        bins=np.array([0,51,102,153,204,255])
        frame_still[:,:,:] = np.digitize(frame_still[:,:,:],bins,right=True)*51
        greyscale2 = cv2.cvtColor(frame_still, cv2.COLOR_BGR2GRAY)
        print("read frame_still")
        
    
       

cam.release()

cv2.destroyAllWindows()

