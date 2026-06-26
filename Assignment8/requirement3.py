import cv2

cap = cv2.VideoCapture(0)

w = int(cap.get(3))
h = int(cap.get(4))

fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("Incident_Record.avi", fourcc, 20.0, (w, h))

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    out.write(frame)
    cv2.imshow("Recording View", frame)
    
    # Exit on ESC key (ASCII value 27)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
