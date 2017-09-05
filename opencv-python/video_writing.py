# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 12:38:45 2017

@author: abench
"""

import cv2

camera_num=0
cap=cv2.VideoCapture(camera_num)


fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

while(cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:
        frame=cv2.flip(frame,1)
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()