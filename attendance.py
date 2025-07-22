import cv2
import datetime

# Load the face detection model
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Start webcam
cap = cv2.VideoCapture(0)

# Attendance log
attendance_log = []

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if timestamp not in attendance_log:
            attendance_log.append(timestamp)
            print(f"✅ Face detected at: {timestamp}")

    cv2.imshow('Attendance System', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Save attendance to a file
with open("attendance_log.txt", "w") as file:
    for time in attendance_log:
        file.write(f"{time}\n")
print("📝 Attendance saved to attendance_log.txt")

