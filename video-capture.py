import cv2


capture = cv2.VideoCapture(0)

while True:
  
  ret, fram = capture.read()
  
  cv2.imshow('frame', frame)
  
  if cv2.waitKey(1) & 0xFF == ord('q'):
    
        break
  
capture.release()

cv2.destroyAllWindows()
