# -*- coding: utf-8 -*-
import cv2

import numpy as np

import os

recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.read('C:\Users\choij\PycharmProjects\cctv\INHASECURITY-main\trainer\trainer.yml')


def Detect():
    body_detect = False

    cascadePath = "C:\Users\choij\PycharmProjects\cctv\INHASECURITY-main\haarcascade\haarcascade_frontalface_default.xml"

    faceCascade = cv2.CascadeClassifier(cascadePath);

    body_detector = cv2.CascadeClassifier(
        'C:\Users\choij\PycharmProjects\cctv\INHASECURITY-main\haarcascade\haarcascade_upperbody.xml')

    font = cv2.FONT_HERSHEY_SIMPLEX

    # iniciate id counter

    id = 0

    # names related to ids: example ==> loze: id=1,  etc

    # 이런식으로 사용자의 이름을 사용자 수만큼 추가해준다.

    names = ['None', 'loze', 'junyoung', 'minjung',
             'minjung']  # 찾고자하는 사람을 등록하여준다. 여기다가 값을 받아서 사람찾기 이름 등록하는 부분을 구현해주면 될듯

    # Initialize and start realtime video capture

    cam = cv2.VideoCapture(0)
    # cam=cv2.imread('/home/pi/Desktop/cctv/test.png')

    cam.set(3, 640)  # set video widht

    cam.set(4, 480)  # set video height

    # Define min window size to be recognized as a face

    minW = 0.1 * cam.get(3)

    minH = 0.1 * cam.get(4)

    while True:

        ret, img = cam.read()

        # img = cv2.flip(img, 1) # Flip vertically

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(

            gray,

            scaleFactor=1.2,

            minNeighbors=5,

            minSize=(int(minW), int(minH)),

        )

        bodies = body_detector.detectMultiScale(

            gray,

            scaleFactor=1.2,

            minNeighbors=5,

            minSize=(int(minW), int(minH)),

        )

        for (x, y, w, h) in faces:

            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

            id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

            # Check if confidence is less them 100 ==> "0" is perfect match
            if (100 - confidence >= 55):

                id = names[id]  # 사람의 이름 그니까

                confidence = "  {0}%".format(round(100 - confidence))  # 만약 정확도가 100이하라면 100에서 정확도를 뺴서 인식도를 나타내라

                cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)  # 사람이름 이름 출력

                cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)  # 정확도 퍼센트 출력


            # elif (100-confidence <= 55) :

            else:

                cv2.putText(img, "UNKNOWN", (x + 5, y - 5), font, 1, (255, 255, 255), 2)  # 사람이름 이름 출력

                if body_detect:

                    for (bx, by, bw, bh) in bodies:
                        cv2.rectangle(img, (bx, by), (bx + bw, by + bh), (255, 0, 0), 2)

                        body_img = img[y:by + bh, x:bx + bw]  # 인식된 얼굴 이미지 crop

                        body_img = cv2.resize(body_img, dsize=(0, 0), fx=0.04, fy=0.04)  # 축소

                        body_img = cv2.resize(body_img, (bw, bh), interpolation=cv2.INTER_AREA)  # 확대

                        img[y:by + bh, x:bx + bw] = body_img

                        # m = cv2.resize('/home/pi/Desktop/cctv/mozaic.png',dsize=(h,w), interpolation=cv2.INTER_LINEAR)
                        # bodyimg[y:y+h, x:x+w] = m

                        # break

                    # 여기까지

                # confidence = "  {0}%".format(round(100 - confidence))

            cv2.imshow('camera', img)

        # 종료준비

        k = cv2.waitKey(10) & 0xff  # Press 'ESC' for exiting video

        if k == 27:
            break

    # Do a bit of cleanup

    print("\n [INFO] Exiting Program and cleanup stuff")

    # cv2.imshow(img)

    cam.release()

    cv2.destroyAllWindows()
