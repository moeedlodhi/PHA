from datetime import timedelta
import os

# import cv2
from django.utils import timezone
import face_recognition

from PHA.settings import BASE_DIR, TOKEN_EXPIRED_AFTER_SECONDS


def face_recognize(loc,second):
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
        loc2 = second
        face_2_image = face_recognition.load_image_file(loc2)
        face_2_face_encoding = face_recognition.face_encodings(face_2_image)[0]

        # face_locations = face_recognition.face_locations(rgb_small_frame)
        # print("face locations {}".format(face_locations))
        # face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        check = face_recognition.compare_faces([face_1_face_encoding], face_2_face_encoding)

        if check[0]:
            return True

        else:
            return False


# If token is expired then it will be removed
def token_expire_handler(token):
    time_elapsed = timezone.now() - token.created
    left_time = timedelta(seconds=TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed
    is_expired = left_time < timedelta(seconds=0)
    if is_expired:
        token.delete()
    return is_expired


lsit='364,365||131'
print(lsit.split('||'))
