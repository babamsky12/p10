import cv2
from pyzbar.pyzbar import decode 
import datetime

capture=cv2.VideoCapture(0)
capture.set(3, 640)
capture.set(4, 480)
QRdetector=cv2.QRCodeDetector()
while True:
    _,img=capture.read()
    data,one, _=QRdetector.detectAndDecode(img)
    success, border = capture.read()
    if data:
        a=data
        break

    cv2.imshow('qrcodescanner app', img)
    if cv2.waitKey(1)==ord('s'):
        break


capture.release()
cv2.destroyAllWindows()

for code in decode(border):
        StoredInfo = open("infos.txt", "w")
        StoredInfo.write(f"{code.data.decode('utf-8')}\n" ) 
        DateAndTime = datetime.datetime.now()
        StoredInfo.write(DateAndTime.strftime("Date: %y-%m-%d | Time: %H:%M:%S"))  
        StoredInfo.close()


