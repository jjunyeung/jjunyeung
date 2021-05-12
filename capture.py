# -*- coding: utf-8 -*-
import cv2

import os

cam = cv2.VideoCapture(0)  # 카메라를 객체로 저장시키고 키겠습니다

cam.set(3, 640)  # set video width

cam.set(4, 480)  # set video height

face_detector = cv2.CascadeClassifier(
    'C:\Users\choij\PycharmProjects\cctv\INHASECURITY-main\haarcascade\haarcascade_frontalface_default.xml')

# body_detector = cv2.CascadeClassifier('/home/pi/Desktop/cctv/opencv-master/data/haarcascades/haarcascade_fullbody.xml') #여 부분을 파이썬 인터페이스에서 경로참조 해갖고 .xml파일
# 참조 했으면 좋겠음


# For each person, enter one numeric face id

body_id = input(
    '\n enter user id end press <return> ==>  ')  # 여기 부분도 고쳐야 할것 같지않나..? 지금 보면 내가 객체가 몇명 있을줄 알고 미리 배열을 선언해서 인식하고있어... 그냥
# 객체인식하고자 하는 사람 이름 쳐서 친 횟수로 따져서 좀 하면 될것 같은데.. 연관성이 뭘까 고민좀 해보기 또는 그냥 얘가 알아서 count=count+1 해서 나오는 숫자를 배열의 자리로 넘겨주는 식으로 하면 될거같은데?

print("\n [INFO] Initializing body capture. Look the camera and wait ...")

# Initialize individual sampling face count

count = 0

while (True):

    ret, img = cam.read()

    # img = cv2.flip(img, -1) # flip video image vertically

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    # bodies = body_detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # face_image_gray = gray[y:y+h, x:x+w]

        # face_image_color = img[y:y+h, x:x+w]

        # faces_in_body = body_detector.detectMultiScale(face_image_gray)

        # for (xf,yf,wf,hf) in faces_in_body:

        # cv2.rectangle(face_image_color,(xf,yf),(xf+wf,yf+hf),(255,0,0),2)

        count += 1  # 사진 장수 카운트업

        # Save the captured image into the datasets folder

        cv2.imwrite("trainervideo/User." + str(body_id) + '.' + str(count) + ".jpg",
                    gray[y:y + h, x:x + w])  # ~의 파일형태로 이미지 저장

        cv2.imshow('image', img)  # 관련함수 cv.imread() : 함수를 이용하여 이미지 파일을 읽습니다. 이미지 파일의 경로는 절대/상대경로가 가능합니다.
        # cv2.imshow() : 함수는 이미지를 사이즈에 맞게 보여줍니다.
        # cv2.imwrite() : 함수를 이용하여 변환된 이미지나 동영상의 특정 프레임을 저장합니다.

        # 여기서부터 종료작업

    k = cv2.waitKey(100) & 0xff  # Press 'ESC' for exiting video

    if k == 27:

        break

    elif count >= 400:  # Take 30 face sample and stop video

        break

# Do a bit of cleanup

print("\n [INFO] Exiting Program and cleanup stuff")

cam.release()

cv2.destroyAllWindows()



