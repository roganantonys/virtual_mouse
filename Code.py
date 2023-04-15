import cv2
import mediapipe as mp
import pyautogui


cap=cv2.VideoCapture(0)  # to capture the video value '0' is for selecting the main camera
hand_detector=mp.solutions.hands.Hands() #used for the hand detection
drawing_utils=mp.solutions.drawing_utils # to draw the dots around the finger
screen_width,screen_height=pyautogui.size() #to find out the total screen size 
index_y=0 

while True: 
    _, frame=cap.read() # to read the image
    frame=cv2.flip(frame,1)
    frame_height,frame_width,_=frame.shape
    rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)  #used to convert the image to rgb colour image because mediapipe only works with RGB image
    output=hand_detector.process(rgb_frame)
    hands=output.multi_hand_landmarks 
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame,hand) #to draw the dots around the finger taken hand as a source and showcase it in frame
            landmarks=hand.landmark  #to seperate the index finger 
            for id,landmark in enumerate(landmarks):
                x=int(landmark.x * frame_width)  #to find the x coordinates
                y=int(landmark.y * frame_height) #to find the y coordinates
                print(x,y)
                if id==8: 
                    cv2.circle(img=frame,center=(x,y),radius=10,color=(0,255,255)) #to create a circle around the index finger
                    index_x=screen_width/frame_width *x
                    index_y=screen_height / frame_height *y
                    pyautogui.moveTo(index_x,index_y) #to move the cursor on the screen based on x and y directions

                if id==4: 
                    cv2.circle(img=frame,center=(x,y),radius=10,color=(0,255,255)) #to create a circle around the index finger
                    thum_x=screen_width/frame_width *x
                    thum_y=screen_height / frame_height *y
                    print("outside",abs(index_y-thum_y))
                    if abs(index_y-thum_y)<100:
                        pyautogui.click() #to make a click
                        pyautogui.sleep(1)
                        print("click")
                

          
    cv2.imshow("virtual mouse",frame) #it shows the video
    cv2.waitKey(1)
