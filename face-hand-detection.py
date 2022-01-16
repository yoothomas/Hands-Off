import cv2
#4.5.4_3

#cv2

#/usr/local/Cellar/opencv/4.5.4_3/lib/python3.9/site-packages/cv2/python-3.9/cv2.cpython-39-darwin.so
img = cv2.imread('image.jpg')
while True:
    cv2.imshow('mandrill',img)

    if cv2.waitKey(1) & 0xFF == 27:
        break


cv2.destroyAllWindows()