import cv2
import numpy as np
import time

def GetLine(frame, HEIGHT, WIDTH):
    line_check_height = int(HEIGHT / 7 * 5)
    center_point = (int(WIDTH / 2), 10)
    check_contour = [0,0]

    m_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    m_hsv = m_hsv[line_check_height - 350:line_check_height + 350,0:WIDTH ]

    lower_color = (207, 127, 0)#(0, 138, 134)#(226, 175, 169)
    upper_color = (237, 144, 255)#(255, 165, 152)#(255, 255, 255)

    m_range = cv2.inRange(m_hsv, lower_color, upper_color)
    contours, hierarchy = cv2.findContours(m_range, cv2.RETR_EXTERNAL, \
                                                cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if y < 15:
            cv2.rectangle(m_range, (x, y), (x + w, y + h), (255, 0, 0), 3)
            if len(check_contour) == 2:
                break
            # print('x :', x, 'y :', y)
            # print('center Width', WIDTH / 2)
            if (x > WIDTH / 2):
                check_contour[1] = x
            elif (x <= WIDTH / 2):
                check_contour[0] = x + w

    print('check_contour :',check_contour)
        # cv2.drawContours(m_range, [cnt], 0, (255, 0, 0), 3)
    got_center = int((check_contour[1] - check_contour[0]) / 2 + check_contour[0])
    cv2.circle(frame, center_point, 3, (255, 0, 0), 10)
    cv2.circle(frame, (got_center, 0), 3, (255, 0, 0), 5)   
    if center_point[0] > got_center and center_point[0] - got_center > 15:
        print('go right')
    elif center_point[0] < got_center and got_center - center_point[0] > 15:
        print('go left')

    cv2.imshow('img', m_range)
    cv2.imshow('img2', frame)  