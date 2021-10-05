import cv2
import time
import HandTrackingModule as htm
import pyautogui

wCam, hCam = 640, 480

cap = cv2.VideoCapture(1)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0

detector = htm.handDetector(detectionCon=0.6,maxHands=2)

tipIds = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    img = detector.findHands(img)


    nbr = detector.numb()
    if nbr == 0:
        print('0')
    elif nbr == 1:
        lmList1 = detector.findPosition(img, draw=False,handNo=0)
        print('1')   
    #Le jeu se joue avec 2 mains donc cette partie est le plus importante
    elif nbr == 2:
        lmList1 = detector.findPosition(img, draw=False,handNo=0)
        lmList2 = detector.findPosition(img, draw=False,handNo=1)
        print('2')
        fingers1 = []
        fingers2 = []
        if len(lmList1) != 0:
            if lmList1[tipIds[0]][1] > lmList1[tipIds[0] - 1][1]:
                fingers1.append(1)
            else:
                fingers1.append(0)

            # 4 Fingers
            for id in range(1, 5):
                if lmList1[tipIds[id]][2] < lmList1[tipIds[id] - 2][2]:
                    fingers1.append(1)
                else:
                    fingers1.append(0)
            #print('fingers1')        
            #print(fingers1)
        if len(lmList2) != 0:
            if lmList2[tipIds[0]][1] > lmList2[tipIds[0] - 1][1]:
                fingers2.append(1)
            else:
                fingers2.append(0)

            # 4 Fingers
            for id in range(1, 5):
                if lmList2[tipIds[id]][2] < lmList2[tipIds[id] - 2][2]:
                    fingers2.append(1)
                else:
                    fingers2.append(0)
            #print('fingers2')
            #print(fingers2)
        #Interprétation du résultat des doigts obtenus(fingers1 et fingers2)
        #Traduction des positions de doigts en des actions

        #Ma main gauche
        
        #mvt en avant
        if ( (fingers2[0]==1)&(fingers2[1]==0)&(fingers2[2]==0)&(fingers2[3]==0)&(fingers2[4]==0)):
            pyautogui.press('z')
        #mvt en arriére
        if ( (fingers2[0]==0)&(fingers2[1]==1)&(fingers2[2]==0)&(fingers2[3]==0)&(fingers2[4]==0)):
            pyautogui.press('s')
        #mvt a droite
        if ( (fingers2[0]==1)&(fingers2[1]==1)&(fingers2[2]==0)&(fingers2[3]==0)&(fingers2[4]==0)):
            pyautogui.press('d')
        #mvt a gauche
        if ( (fingers2[0]==0)&(fingers2[1]==1)&(fingers2[2]==1)&(fingers2[3]==0)&(fingers2[4]==0)):
            pyautogui.press('q')
        #sauter
        if ( (fingers2[0]==1)&(fingers2[1]==1)&(fingers2[2]==1)&(fingers2[3]==1)&(fingers2[4]==1)):
            pyautogui.press('escape')

        if ( (fingers2[0]==0)&(fingers2[1]==1)&(fingers2[2]==1)&(fingers2[3]==1)&(fingers2[4]==1)):
            pyautogui.press('ctrl')


        #Ma main droite
        #tirer
        if ( (fingers1[0]==1)&(fingers1[1]==0)&(fingers1[2]==0)&(fingers1[3]==0)&(fingers1[4]==0)):
            pyautogui.press('enter')  
        #rechargement de l'arme
        if ( (fingers1[0]==1)&(fingers1[1]==1)&(fingers1[2]==0)&(fingers1[3]==0)&(fingers1[4]==0)):
            pyautogui.press('r')
        #Rotation avec le souris

        







    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN,
                3, (255, 0, 0), 3)
    
    cv2.imshow("Image", img)
    

    k=cv2.waitKey(1)
    if k == ord('q'):
        print("Closing the window")
        break

cap.release()

cv2.destroyAllWindows()