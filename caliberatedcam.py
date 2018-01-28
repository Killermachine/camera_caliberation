import cv2
import numpy as np 

K = np.array([[239.04527396,0.,313.31625459],[0.,239.33115443,221.67111166],[0.,0.,1.]],dtype=np.float32)
D = np.array([[-2.97044734e-01,8.01397918e-02,4.10788000e-05,1.56613119e-04,-8.93097849e-03]],dtype=np.float32)
Knew = K.copy()
Knew[(0,1), (0,1)] = 2 * Knew[(0,1), (0,1)]

cap = cv2.VideoCapture(1)
frame_num = 0
while(True):
	ret,frame = cap.read()

	img_undistorted = cv2.undistort(frame, K, D,Knew)
	# hold 'q' for 2 seconds to quit
	if cv2.waitKey(2) & 0xFF == ord('q'):
		break
	cv2.imshow("frame",img_undistorted)

cap.release()
cv2.destroyAllWindows()