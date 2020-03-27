import cv2

captura = cv2.VideoCapture('00_Ficheros/video.mp4')

while captura.isOpened():
    
    resultado, video = captura.read()

    if resultado == True:
        cv2.imshow('Mi video', video)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
captura.release()
cv2.destroyAllWindows()