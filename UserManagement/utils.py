import os

# import cv2
import face_recognition

from PHA.settings import BASE_DIR


def face_recognize(loc):
    # cam = cv2.VideoCapture(0)
    # s, img = cam.read()
    # print(s, img)
    k = True
    if k:
        media_root = os.path.join(BASE_DIR)
        loc = (str(media_root) + loc)
        face_1_image = face_recognition.load_image_file(loc)
        # print(loc)
        # print(face_1_image)
        face_1_face_encoding = face_recognition.face_encodings(face_1_image)[0]

        # small_frame = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
        #
        # rgb_small_frame = small_frame[:, :, ::-1]
        loc2 = (str(media_root) + "/media/ab.jpg")
        face_2_image = face_recognition.load_image_file(loc2)
        face_2_face_encoding = face_recognition.face_encodings(face_2_image)[0]

        # face_locations = face_recognition.face_locations(rgb_small_frame)
        # print("face locations {}".format(face_locations))
        # face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        check = face_recognition.compare_faces([face_1_face_encoding], face_2_face_encoding)

        print(check)
        if check[0]:
            return True

        else:
            return False
