import cv2

captura = cv2.VideoCapture(0)

ancho = int(captura.get(cv2.CAP_PROP_FRAME_WIDTH))
alto = int(captura.get(cv2.CAP_PROP_FRAME_HEIGHT))

codigo = cv2.VideoWriter_fourcc(*'DIVX')
grabador = cv2.VideoWriter('00_Ficheros/video.mp4',codigo,20,(ancho,alto))

while True:
    resultado, video = captura.read()

    grabador.write(video)

    cv2.imshow('Nuestro video', video)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

captura.release()
grabador.release()
cv2.destroyAllWindows()