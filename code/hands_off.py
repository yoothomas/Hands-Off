import cv2
import time

def count(x):
    total = 0
    for i in x:
        if i == 1:
            total += 1

    return total >= 4


def hands_off():
    face_cascade = cv2.CascadeClassifier('code\\algorithm\haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('code\\algorithm\hand.xml')

    video = cv2.VideoCapture(0)

    queue = [0,0,0,0,0]
    eye_rubs = 0


    start = time.time()
    while True:
        if eye_rubs == 3:
            end = time.time()
            video.release()
            cv2.destroyAllWindows()
            return eye_rubs/(end-start) * 60

        check, frame = video.read()
        faces = face_cascade.detectMultiScale(frame,
                                            scaleFactor=1.1, minNeighbors=5)
        
        eyes = eye_cascade.detectMultiScale(frame,
                                            scaleFactor=1.1, minNeighbors=20)

        face_address = {}
        for x,y,w,h in faces:
            frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)
            face_address['x'] = x
            face_address['y'] = y
            face_address['x2'] = x+w
            face_address['y2'] = y+h
            break
        
        valid_eyes = 0

        for x,y,w,h in eyes:
            if len(face_address) > 0 and x >= face_address['x'] - w and x <= face_address['x2'] and y >= face_address['y'] - h and y <= face_address['y2']:
                frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)
                valid_eyes += 1

        #Comment this line out for demo purposes
        cv2.imshow('Face & Eyes Detector', frame)

        queue.insert(0, valid_eyes)
        queue.pop(-1)

        if (count(queue)):
            print("EYE RUB")
            cv2.imwrite("code\eye_rubs\\frame%d.png" % eye_rubs, frame) 
            eye_rubs += 1
            time.sleep(2)
            queue = [0,0,0,0,0]

        key = cv2.waitKey(1)

        print(valid_eyes)

        if key == ord('q'):
            end = time.time()
            print(start, end, start-end, eye_rubs, eye_rubs/(end-start) * 60)
            video.release()
            cv2.destroyAllWindows()
            return eye_rubs/(end-start) * 60

        time.sleep(0.02)
    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    hands_off()