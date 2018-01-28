import cv2 
import os

img_dir = "./images"
if not os.path.exists(img_dir):
	os.makedirs(img_dir)

cap = cv2.VideoCapture(0)
# Width
cap.set(3,1280);
# Height
cap.set(4,720);

frame_num = 0
while(True):
	ret,frame = cap.read()
	cv2.imshow("frame",frame)

	# press 's' to save frame
	if cv2.waitKey(1) & 0xFF == ord('s'):
		cv2.imwrite(img_dir + "/" + str(frame_num) + ".jpg",frame)
		frame_num += 1

	# hold 'q' for 2 seconds to quit
	if cv2.waitKey(2) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()