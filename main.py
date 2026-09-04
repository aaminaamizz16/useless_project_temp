import cv2
import cvzone
from cvzone.FaceDetectionModule import FaceDetector
import serial
import time
import pygame
import numpy as np

# -------------------------------------------------------------
# 1. AUDIO ENGINE SETUP
# -------------------------------------------------------------
pygame.mixer.init()

def play_single_sound(file_path):
    """Loads and plays a single sound, waiting until it finishes."""
    try:
        sound = pygame.mixer.Sound(file_path)
        sound.play()
        while pygame.mixer.get_busy():
            time.sleep(0.05)
    except Exception as e:
        print(f"Audio playback error ({file_path}): {e}")

# -------------------------------------------------------------
# 2. SERIAL LINK TO ESP32 (Auto-handles absent hardware)
# -------------------------------------------------------------
COM_PORT = 'COM5'
BAUD_RATE = 115200

try:
    esp32 = serial.Serial(COM_PORT, BAUD_RATE, timeout=0.1)
    time.sleep(2)
    print("ESP32 Serial Link Established.")
except Exception as e:
    print(f"Running in Keyboard Test Mode (Hardware not connected).")
    esp32 = None

# -------------------------------------------------------------
# 3. LOAD TARGET (TOXIC FRIEND) FACE TEMPLATE
# -------------------------------------------------------------
try:
    toxic_raw = cv2.imread("toxic_frnd.jpg", cv2.IMREAD_GRAYSCALE)
    if toxic_raw is None:
        raise Exception("Could not find 'toxic_frnd.jpg' in your folder!")
    # Standardize image size to 120x120 pixels for comparison
    toxic_template = cv2.resize(toxic_raw, (120, 120))
    print("Toxic friend face template loaded successfully.")
except Exception as e:
    print(f"Error: {e}")
    exit()

# -------------------------------------------------------------
# 4. INITIALIZE CAMERA & CVZONE DETECTOR
# -------------------------------------------------------------
detector = FaceDetector(minDetectionCon=0.6)
video_capture = cv2.VideoCapture(0)

print("Sentry Ready. Press 't' on the camera window to simulate trigger, or 'q' to quit.")

# -------------------------------------------------------------
# 5. MAIN MONITORING LOOP
# -------------------------------------------------------------
while True:
    success, frame = video_capture.read()
    if not success:
        break

    # Read serial trigger sent from ESP32 (if hardware is plugged in)
    esp_trigger = ""
    if esp32 and esp32.in_waiting > 0:
        try:
            esp_trigger = esp32.readline().decode('utf-8').strip()
        except:
            pass

    # Read keyboard inputs
    key = cv2.waitKey(1) & 0xFF

    # TRIGGER CONDITION: ESP32 sends 'SCAN_NOW' OR user presses 't' key on keyboard
    trigger_detected = (esp_trigger == "SCAN_NOW") or (key == ord('t'))

    if trigger_detected:
        print("\nTrigger activated! Analyzing face...")
        
        # Detect faces in frame using cvzone
        frame, bboxs = detector.findFaces(frame, draw=False)

        if bboxs:
            # Grab bounding coordinates of the detected face
            x, y, w, h = bboxs[0]['bbox']
            x, y = max(0, x), max(0, y)
            face_roi = frame[y:y+h, x:x+w]

            if face_roi.size != 0:
                # Convert detected face to grayscale and resize to match template
                gray_face = cv2.cvtColor(face_roi, cv2.COLOR_BGR2GRAY)
                gray_face_resized = cv2.resize(gray_face, (120, 120))

                # Compare live face against toxic template
                result = cv2.matchTemplate(gray_face_resized, toxic_template, cv2.TM_CCOEFF_NORMED)
                _, max_val, _, _ = cv2.minMaxLoc(result)

                print(f"Face Match Score: {max_val:.2f}")

                # Threshold for toxic face match
                if max_val > 0:
                    print(">> TOXIC FRIEND DETECTED!")
                    
                    # 1. Play first dialogue upon face recognition
                    print("Playing dialogue 1 (Recognition)...")
                    play_single_sound("toxic_frnd1.wav")
                    
                    # 2. Tell ESP32 to slam door shut to 0 degrees
                    if esp32:
                        esp32.write(b'N')
                        time.sleep(0.3)
                    
                    # 3. Play second dialogue once door is shut
                    print("Playing dialogue 2 (Door Shut)...")
                    play_single_sound("toxic_frnd2.wav")

                else:
                    print(">> GOOD FRIEND DETECTED!")
                    
                    # 1. Tell ESP32 to open door fully to 90 degrees
                    if esp32:
                        esp32.write(b'F')
                        time.sleep(0.3)
                    
                    # 2. Play welcome dialogue as door turns 90 degrees
                    print("Playing welcome dialogue...")
                    play_single_sound("my_frnd.wav")

                if esp32:
                    esp32.reset_input_buffer()
        else:
            print("No face detected in front of camera!")

    # Display live feed with status banner
    cv2.putText(frame, "SENTRY ACTIVE - Press 't' to test trigger", (20, 40), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    cv2.imshow("Nemesis Sentry Cam", frame)

    # Press 'q' on keyboard to quit
    if key == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
if esp32:
    esp32.close()