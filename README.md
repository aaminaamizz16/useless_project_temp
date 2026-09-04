<img width="1280" height="640" alt="git (1)" src="https://github.com/user-attachments/assets/8920b256-2ba8-4988-b824-5351134eb4bd" />



# 🚪 Kadakk Purath (കടക്ക് പുറത്ത്): Automated Selective-Access Door System


## Basic Details
### Team Name: [cipher]


### Team Members
- Team Lead: [Malavika Vijayakumar] - [LBSITW THIRUVANANTHAPURAM]
- Member 2: [Amina Nujooma] - [LBSITW THIRUVANANTHAPURAM]

### Project Description
How can we stop an unlikable person from entering our door without anyone actually asking us(eg: toxic relatives and friends)

An intelligent, computer-vision-based selective door automation and access-denial system built with Python and OpenCV. Named after the iconic phrase **"Kadakk Purath"** (*"Get Out"*), this project automates personal boundaries by dynamically identifying who is at your door.
### Project solution
Welcome friends are greeted warmly with an open door and cheerful audio, while toxic acquaintances, are met with an immediate shut door and custom rejection dialogues.
The system is currently implemented as an interactive software demonstration with keyboard triggers (`t` to scan, `q` to quit), complete with an architectural roadmap for embedded hardware integration using an ESP32 and high-torque servo motor.


### The Solution (that nobody asked for)
[**Kadakk Purath** shifts the burden of boundary enforcement entirely to software:
* **Selective Blacklist Architecture:** Rather than requiring an extensive whitelist of everyone who can enter, the system stores reference facial embeddings of the specific person (or people) you wish to block. Anyone else is treated as a welcome guest.
* **Contextual Audio Dialogues:**
  * **Friendly Guest:** Welcomes the visitor with an affirmative dialogue and sets the door state to **OPEN (90°)**.
  * **Toxic Guest:** Plays an intermediate suspense dialogue during verification, flags `"Toxic friend detected"`, simulates a door slam to **SHUT (0°)**, and plays the closing punchline dialogue.
* **Control Emulation:** Uses keyboard shortcuts (`t` to trigger face capture and evaluation, `q` to exit) to allow predictable, interactive testing on any computer without needing physical sensors wired up.
* **Hardware-Ready:** Designed with clean serial dispatch hooks (`'F'` for Friend, `'N'` for Nemesis) to drive physical microcontrollers and servos.

---

## ✨ Features

- **Real-Time Facial Recognition:** Uses 128-dimensional facial embeddings (`face_recognition` / `dlib`) via OpenCV webcam video capture.
- **Dynamic Access Policy:**
  - **Good Friend Detected:** Confirms non-blacklist status, opens the door to 90°, and triggers welcome audio.
  - **Toxic Friend Detected:** Matches the blacklisted profile, triggers verification dialogue 1, slams the door shut to 0°, and delivers the rejection punchline dialogue 2.
  - **New / Third-Party Visitors:** Automatically classified as safe guests, validating the default-allow model.
- **Non-Blocking Audio Engine:** Utilizes `pygame.mixer` to ensure speech and audio play smoothly without stuttering or freezing the camera feed.]

### Technologies or components used
for software
Python 3.11: Core programming language.
OpenCV (cv2): Webcam video capture, frame processing, and on-screen display.
face_recognition (dlib): Face detection and 128-d facial embedding comparison.
Pygame (pygame.mixer): Non-blocking audio playback for dialogue MP3s.
VS Code: Development environment.


### Implementation
For Software:
Run: py -3.11 main.py
Workflow:
Loads and encodes toxic_target.jpg.
Opens webcam feed.
Press t to scan face:
Friend: Displays "Good friend detected" | Opens door (90°) | Plays welcome.mp3.
Toxic Friend: Displays "Toxic friend detected" | Shuts door (0°) | Plays toxic_phase1.mp3 & toxic_phase2.mp3.
Press q to exit.
# Installation
[commands]
pip install opencv-python face_recognition pygame

# Run
[commands]

### Project Documentation
For Software:

# Screenshots (Add at least 3)
![Screenshot1](Add screenshot 1 here with proper name)
"C:\Users\AMINA NUJOOMA\Downloads\WhatsApp Image 2026-09-04 at 08.52.23.jpeg"
![Screenshot2](demo)
"C:\Users\AMINA NUJOOMA\Downloads\WhatsApp Image 2026-09-04 at 08.52.24.jpeg"
"
*Add caption explaining what this shows*

![Screenshot3](Add screenshot 3 here with proper name)
C:\Users\AMINA NUJOOMA\Downloads\WhatsApp Image 2026-09-04 at 08.52.25 (1).jpeg"
*Add caption explaining what this shows*

# Diagrams
+------------------------------------+
                    |             START                  |
                    |     (Run: py -3.11 main.py)        |
                    +-----------------+------------------+
                                      |
                                      v
                    +------------------------------------+
                    |       Initialize System            |
                    | - Load & encode 'toxic_target.jpg' |
                    | - Init Pygame Audio Mixer          |
                    | - Start Webcam Video Stream        |
                    +-----------------+------------------+
                                      |
                                      v
                    +------------------------------------+
                    |         Live Video Loop            |
                    |       (Display Camera Feed)        |
                    +-----------------+------------------+
                                      |
                         +------------+------------+
                         |                         |
                         v                         v
                   [ Key: 't' ]               [ Key: 'q' ]
                         |                         |
                         v                         v
        +----------------------------------+  +---------+
        |        Capture Active Frame      |  |  EXIT   |
        |      & Extract Face Encodings    |  +---------+
        +----------------+-----------------+
                         |
                         v
                /------------------\
               /    Does face match \
              <   toxic_target.jpg?  >
               \                    /
                \------------------/
                     /          \
           YES      /            \      NO
                   /              \
                  v                v
    +-------------------------+  +-------------------------+
    |   TOXIC FRIEND DETECTED |  |   GOOD FRIEND DETECTED  |
    +-------------------------+  +-------------------------+
    | 1. Play Dialogue 1      |  | 1. Show: "Good Friend"  |
    | 2. Show: "Toxic Friend" |  | 2. Virtual Door: 90°    |
    | 3. Virtual Door: 0°     |  |    (OPEN)               |
    |    (SLAM SHUT)          |  | 3. Play Welcome Audio   |
    | 4. Play Dialogue 2      |  +------------+------------+
    |    ("Kadakk Purath!")   |               |

+------------+------------+ |
| :--- | <br> +--------------+-------------+
|

                                v
                   [ Return to Live Video Loop ]
For Hardware:

# Schematic & Circuit
![Circuit]("C:\Users\AMINA NUJOOMA\Downloads\WhatsApp Image 2026-09-04 at 08.52.26.jpeg"
"C:\Users\AMINA NUJOOMA\Downloads\WhatsApp Video 2026-09-04 at 08.52.26.mp4")
*Add caption explaining connections*

![Schematic](Add your schematic diagram here)
*Add caption explaining the schematic*

# Build Photos
![Components](Add photo of your components here)
*List out all components shown*

![Build](Add photos of build process here)
*Explain the build steps*

![Final](Add photo of final product here)
*Explain the final build*

### Project Demo
# Video
["C:\Users\AMINA NUJOOMA\Downloads\WhatsApp Video 2026-09-04 at 08.49.54.mp4"
"C:\Users\AMINA NUJOOMA\Downloads\WhatsApp Video 2026-09-04 at 09.01.26.mp4"
"C:\Users\AMINA NUJOOMA\Downloads\WhatsApp Video 2026-09-04 at 08.52.26.mp4"
]
*Explain what the video demonstrates*

# Additional Demos
[Add any extra demo materials/links]

## Team Contributions
- [Amina Nujooma]: [installation]
- [Malavika vijayakumar]: [implementation main.py]


---
Made with ❤️ at TinkerHub Useless Projects 

![Static Badge](https://img.shields.io/badge/TinkerHub-24?color=%23000000&link=https%3A%2F%2Fwww.tinkerhub.org%2F)
![Static Badge](https://img.shields.io/badge/UselessProjects--26-26?link=https%3A%2F%2Ftinkerhub.org%2Fevents%2F1M8ORET9A1%2Fuseless-projects-3.0)



