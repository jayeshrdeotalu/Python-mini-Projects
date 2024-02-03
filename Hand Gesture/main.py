import cv2 as cv    


def centre(drawn, x, y, w, h):
    x =  int((x + w)/2)
    y =  int((y + h)/2)
    drawn = cv.circle(drawn, (x, y), radius=1, color=(0, 0, 255), thickness=1)
    return drawn


# Initailise video
capture = cv.VideoCapture(0)

# import classifier 
cascade = cv.CascadeClassifier('/home/om/Downloads/Backup/Open_CV_basics/harcascade_face_reg_default.xml')

while True:
    isTrue, frame = capture.read()
    # Check if frame is captured or not
    if not isTrue:
        break
    cv.imshow('Live Video', frame)

    # make it gray
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('Live Gray', gray_frame)

    # get the coordinates
    live_rect = cascade.detectMultiScale(gray_frame, 1.1, 2)
    print(f'The number of face found is {len(live_rect)}')

    # show the rectangle
    
    for (x, y, w, h) in live_rect:
        x_center = int(((w - x) / 2) + x)
        y_center = int(((h - y) / 2) + y)

        drawn = cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)
        drawn = cv.circle(drawn, (x_center, y_center), radius=1, color=(0, 255, 0), thickness=1)

        cv.imshow('Drawn', drawn)   

    # to stop recording
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# destroy all windows
capture.release()
cv.destroyAllWindows()