import cv2
import numpy as np
import time as t

cap = cv2.VideoCapture(0)
HEIGHT, WIDTH = cap.read()[1].shape[:2]
frames = 0

FPS = '20'

while cap.isOpened():
    startTime = t.time()
    ret, frame = cap.read()
    frames += 1
    if not ret:
        break

    if frames % 30 == 0:
        print('now frame :',frames)
    
    # size big - 4 FPS
    # frameArr = frame[int(HEIGHT / 3 * 2) : HEIGHT - 1, int(WIDTH / 3) : int(WIDTH / 3 * 2)]

    # size small - 20 FPS
    frameArr = frame[0 : int(HEIGHT / 9 * 1), int(WIDTH / 9 * 4) : int(WIDTH / 9 * 5)]
    
    outCheck = False
    for row in frameArr:
        for column in row:
            if column[1] < 50 and 150 > column[2] > 100 and column[0] > 50:
                cv2.putText(frame, 'got yellow', (500, 100), 0, fontScale=2, color=(0,0,0), thickness=5)
                outCheck = True
                break
            # 이거 포함하면 12FPS
            # elif column[2] > 150 and column[1] < 50 and column[0] < 50:
            #     cv2.putText(frame, 'got red', (500, 100), 0, fontScale=2, color=(0,0,0), thickness=5)
            #     outCheck = True
            #     break
        if outCheck:
            break

    # 연산량이  이렇게  되면  8FPS
    # for row in frameArr:
    #     for column in row:
    #         if column[0] > 150 and column[1] < 50 and column[1] < 50:
    #             cv2.putText(frame, 'got green', (500, 100), 0, fontScale=2, color=(0,0,0), thickness=5)
    #             outCheck = True
    #             break
    #     if outCheck:
    #         break

    # for row in frameArr:
    #     for column in row:
    #         if column[1] > 150 and column[2] < 50 and column[0] < 50:
    #             cv2.putText(frame, 'got blue', (500, 100), 0, fontScale=2, color=(0,0,0), thickness=5)
    #             outCheck = True
    #             break
    #     if outCheck:
    #         break

    finishedTime = t.time()
    if frames % 15 == 0:
        FPS = str(1 / (finishedTime - startTime))
        FPS = FPS[:4]
    
    cv2.putText(frame, FPS, (100, 100), 0, fontScale=2, color=(0,0,0), thickness=5)

    cv2.imshow('test', frame)

    if cv2.waitKey(1) == 27:
        break



cap.release()
cv2.destroyAllWindows()
