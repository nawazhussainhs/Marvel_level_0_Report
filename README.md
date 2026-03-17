# Nawaz's D&P Level 0 Report
---
## Task 01 – 3D Printing

### Objective
The objective of this task was to understand how a 3D printer works and to learn about STL files, slicing software, and basic printer settings.  
For this task, an STL model was downloaded from the internet, opened in slicing software, and prepared for printing.

---

### Learnings

#### PLA Material
PLA (Polylactic Acid) is one of the most commonly used materials in 3D printing. It is made from renewable resources such as corn starch and sugarcane. PLA is easy to print with and is widely used for beginners.

#### Bed Temperature
PLA can sometimes be printed without heating the print bed. However, using a heated bed improves adhesion and helps the first layer stick properly. A bed temperature of around **50–60°C** works well for PLA.

#### Cooling
The cooling fan of the printer helps the layers solidify faster. Proper cooling improves print quality and helps maintain better detail in the printed object.

#### Printing Speed
Printing speed also affects the final quality of the print. A moderate speed of around **50–60 mm/s** provides a good balance between print quality and printing time.

---

### Post-Processing

#### Joining Parts
If a model is printed in multiple parts, they can be joined using adhesives such as **super glue (cyanoacrylate)** or **epoxy**.

#### Painting
3D printed objects can be painted after printing to improve their appearance or add color.

#### Sanding
The surface of a printed object can be smoothed using sandpaper. Sanding should be done gently using finer sandpaper to avoid damaging the plastic.

---

### My 3D Print

Below are the images of the final 3D printed model.

![3D Print Image 1](https://raw.githubusercontent.com/nawazhussainhs/Marvel_level_0_images/refs/heads/main/myprint1.jpeg)

![3D Print Image 2](https://raw.githubusercontent.com/nawazhussainhs/Marvel_level_0_images/refs/heads/main/myprint2.jpeg)

---
## Task 02 – API

### Objective
The objective of this task was to understand how APIs work and how applications can fetch data from external services. A simple web interface was created that retrieves movie information using a movie API.

---

### Learnings

#### Understanding APIs
An API (Application Programming Interface) allows different software applications to communicate with each other. It enables a program to request data from another service and receive a response.

#### API Requests and Responses
When a user searches for a movie, the application sends a request to the movie API. The API processes the request and returns information such as the movie title, poster, genre, rating, and plot.

#### User Interface Development
A basic movie search interface was created where users can type the name of a movie and view its details.

#### Practical Example
The application can fetch details for movies such as *Interstellar* and *Inception*. The API returns information including the poster, genre, director, IMDb rating, and a short description.

#### Practical Understanding
Through this task, I understood how a webpage can connect with an external API, send requests, receive data, and display the information dynamically.

---

### Screenshots

#### Movie Search – Interstellar
![Interstellar Search](https://raw.githubusercontent.com/nawazhussainhs/Marvel_level_0_images/refs/heads/main/Interstellar.png)

#### Movie Search – Inception
![Inception Search](https://raw.githubusercontent.com/nawazhussainhs/Marvel_level_0_images/refs/heads/main/Inception.png)

---

## Task 03 – Working with GitHub

### Objective
The objective of this task was to understand how GitHub works and to learn the basic workflow such as repositories, forks, issues, and pull requests by exploring the provided repository.

### Learnings

#### Understanding GitHub
GitHub is a platform used for version control and collaboration. It allows developers to store their code in repositories and work together on projects.

#### Repository Management
I learned how to create new repositories, manage files inside them, and delete repositories when they are no longer needed.

#### Forking a Repository
The provided repository was forked into my GitHub account so that I could explore and work on it independently.

#### Making Changes
I explored the repository structure and understood how changes can be made and later contributed back through pull requests.

#### Practical Understanding
Through this task, I became familiar with the GitHub interface and the basic workflow used in collaborative software development.

---

## Task 04 – Command Line on Ubuntu

### Objective
To get familiar with the Ubuntu command line and understand how files and directories can be created and managed using terminal commands.

### Methodology
The Ubuntu terminal was used to practice basic commands for directory navigation, file creation, and file management. A folder named **test** was created and different commands were executed inside it to understand how command line operations work.

### Commands Used

First, a directory named **test** was created and the terminal was moved into that directory.

```bash
mkdir test
cd test
pwd
```

Next, a new empty file was created and the contents of the directory were listed.

```bash
touch file.txt
ls
```

Then multiple folders were generated using a sequence pattern.

```bash
mkdir B{0001..2600}
```

After that, text was written into two files using the `echo` command.

```bash
echo "this is file one" > file1.txt
echo "this is file two" > file2.txt
```

Finally, the contents of the two files were combined using the `cat` command.

```bash
cat file1.txt file2.txt
```

Output:

```text
this is file one
this is file two
```

### Practical Understanding
Through this task, I learned how to navigate directories, create files and folders, generate multiple directories using command patterns, and combine file contents using basic Ubuntu terminal commands.

### Screenshots

#### Terminal commands
![Terminal Commands](https://raw.githubusercontent.com/nawazhussainhs/Marvel_level_0_images/refs/heads/main/terminal_commands.png)

#### Folder creation
![Folder Creation](https://raw.githubusercontent.com/nawazhussainhs/Marvel_level_0_images/refs/heads/main/folder_creation.png)

#### File Concatenation
![File Concatenation](https://raw.githubusercontent.com/nawazhussainhs/Marvel_level_0_images/refs/heads/main/file_concatenation.png)

#### Directory Listing
![Directory Listing](https://raw.githubusercontent.com/nawazhussainhs/Marvel_level_0_images/refs/heads/main/listing.png)

---

## Task 05 – Matrix Puzzle (NumPy)

### Objective
To learn basic NumPy operations and use them to decode a scrambled matrix and reveal a hidden image using Matplotlib.

### Description
In this task, a scrambled matrix was downloaded and analyzed using NumPy. The matrix was reshaped and manipulated using operations such as reshaping, flipping, and transposing. After correcting the orientation of the matrix, the hidden image was revealed using Matplotlib.

### Tools Used
- Python  
- NumPy  
- Matplotlib  

### Implementation
The matrix was reshaped into a square array and adjusted using NumPy operations. Finally, the image was displayed using `matplotlib.pyplot.imshow()`.

```python
import numpy as np
import matplotlib.pyplot as plt

data = np.load("encoded_array.npy")

img = data.T

left  = img[:, ::2]
right = img[:, 1::2]

merged = np.hstack((left, right))

left_half  = merged[:, :100]
right_half = merged[:, 100:]

decoded = np.vstack((left_half, right_half))

plt.imshow(decoded, cmap="gray")
plt.axis("off")
plt.show()
```
### OUTPUT

![Decoded image](https://raw.githubusercontent.com/nawazhussainhs/Marvel_level_0_images/refs/heads/main/NUMPY_DECODED.png)

---

## Task 06 – Portfolio Webpage

### Objective
The objective of this task was to create a simple personal portfolio webpage that presents basic information such as an introduction, interests, projects, and useful links.

### Description
In this task, a basic portfolio webpage was created using HTML. The page includes sections such as an introduction, projects, and links to other platforms. After creating the webpage, the project files were uploaded to a GitHub repository.

### Tools Used
- HTML  
- Git  
- GitHub  

### Learnings
- Creating a simple webpage using HTML  
- Structuring information clearly on a webpage  
- Uploading project files to GitHub  
- Understanding how a portfolio website can be used to showcase personal work

### Screenshot

![Portfolio Website](https://raw.githubusercontent.com/nawazhussainhs/Marvel_level_0_images/refs/heads/main/portfolio.png)

![Portfolio Website](https://raw.githubusercontent.com/nawazhussainhs/Marvel_level_0_images/refs/heads/main/portfolio2.png
)
---

## Task 07 – Writing Resource Article using Markdown

### Objective
The objective of this task was to write a technical resource article on a chosen topic using Markdown and publish it on the MARVEL website.

### Outcomes & Learnings
For this task, I wrote an article on **Printed Circuit Board (PCB) Design**. The article explains what a PCB is, the basic PCB design process, and some important concepts used in electronics design.

### Article

Click the link below to view the article:

[PCB Design Article](PASTE_YOUR_ARTICLE_LINK_HERE)

---

## Task 08 – Tinkercad Ultrasonic Distance Measurement

### Objective
The objective of this task was to create a Tinkercad account and build a simple circuit to estimate the distance between an ultrasonic sensor and an object using an Arduino.

### Description
In this task, an **HC-SR04 ultrasonic sensor** was connected to an **Arduino UNO** in Tinkercad. The sensor sends ultrasonic waves and measures the time taken for the echo to return after hitting an object. Using this time delay, the distance between the sensor and the object can be calculated.

A second version of the circuit was also created where a **servo motor** rotates along with the ultrasonic sensor to simulate a simple radar scanning system.

### Components Used
- Arduino UNO  
- HC-SR04 Ultrasonic Sensor  
- Servo Motor  
- Breadboard  
- Jumper Wires  

### Working Principle
The Arduino sends a trigger signal to the ultrasonic sensor. The sensor emits ultrasonic waves which reflect off nearby objects. The time taken for the echo signal to return is measured and converted into distance using a simple formula in the Arduino code.

### Circuit Diagrams

#### Ultrasonic Sensor Circuit
![Ultrasonic Distance Circuit](https://github.com/nawazhussainhs/Marvel_level_0_images/blob/main/schematic.png?raw=True)

#### Ultrasonic Sensor with Servo Circuit
![Ultrasonic Servo Circuit](https://github.com/nawazhussainhs/Marvel_level_0_images/blob/main/schematic_servo.png?raw=True)

### Simulation

#### Distance Measurement Simulation
![Ultrasonic Distance Working](https://raw.githubusercontent.com/nawazhussainhs/Marvel_level_0_images/refs/heads/main/working.png)

#### Ultrasonic Radar with Servo Simulation
![Ultrasonic Servo Working](https://raw.githubusercontent.com/nawazhussainhs/Marvel_level_0_images/refs/heads/main/withservo_working.png)

### Learnings
- Creating circuits using **Tinkercad**  
- Interfacing an **HC-SR04 ultrasonic sensor with Arduino**  
- Measuring distance using ultrasonic signals  
- Understanding basic **sensor-based distance measurement**

---

## Task 09 – Speed Control of DC Motor using L298N Driver

### Objective
The objective of this task was to understand how to control the speed of a DC motor using an Arduino Uno and the L298N motor driver. Using an Arduino board and the L298N H-Bridge motor driver, the speed of a 5V DC motor was controlled using PWM signals.

### About the L298N Motor Driver
The **L298N** is a dual H-Bridge motor driver module commonly used to control DC motors and stepper motors. It allows a microcontroller such as Arduino to control motors that require higher current and voltage than the Arduino can supply directly.

The motor driver works using an **H-Bridge circuit**, which allows:
- Controlling the **direction of rotation**
- Controlling the **speed of the motor using PWM**
- Driving motors that require higher current

### Implementation
In this task, an Arduino Uno was connected to the L298N motor driver module and a DC motor. A 9V battery was used to power the motor while the Arduino controlled the motor through digital pins. The speed of the motor was controlled by sending PWM signals to the enable pin of the motor driver.

The circuit was first simulated using **Tinkercad**, and then the hardware setup was tested with an actual motor driver and DC motor.

### Screenshots

![Hardware Setup](https://raw.githubusercontent.com/nawazhussainhs/Marvel_level_0_images/refs/heads/main/dc.jpeg)

![Circuit Schematic](https://raw.githubusercontent.com/nawazhussainhs/Marvel_level_0_images/refs/heads/main/schematic_diagram.png)

![Tinkercad Simulation](https://raw.githubusercontent.com/nawazhussainhs/Marvel_level_0_images/refs/heads/main/tinkercad_simulation.png)

![Serial Monitor Output](https://raw.githubusercontent.com/nawazhussainhs/Marvel_level_0_images/refs/heads/main/tinkercad_serial_monitor_readings.png)

### Demonstration Video

▶️ [Watch the Simulation Video](https://youtu.be/sfCmW3ocwdY?si=zbngWVYYj1YBJzpa)

### Practical Understanding
Through this task, I learned how motor drivers work and why they are required when controlling motors with microcontrollers. I also understood how PWM signals from Arduino can be used to change the speed of a DC motor and how an H-Bridge circuit allows both direction and speed control.

---

## Task 10 – LED Toggle Using ESP32

### Objective
The objective of this task was to learn the working of the ESP32 microcontroller and create a simple web server that can control LEDs connected to the ESP32 GPIO pins.

### Implementation
In this task, an ESP32 board was used to host a small web server. The ESP32 was connected to a WiFi network and served a webpage that allowed the user to control LEDs connected to its GPIO pins.

When a button on the webpage is pressed, a request is sent to the ESP32 server, which then toggles the corresponding LED connected to the board.

This demonstrates how ESP32 can be used for **basic IoT applications**, where hardware devices can be controlled remotely through a web interface.

### Screenshots

![ESP32 Hardware](https://raw.githubusercontent.com/nawazhussainhs/Marvel_level_0_images/refs/heads/main/esp.jpeg)

![ESP32 Web Control](https://raw.githubusercontent.com/nawazhussainhs/Marvel_level_0_images/refs/heads/main/esp2.jpeg)

### Demonstration Video

▶️ [Watch the Simulation Video](https://youtube.com/shorts/Lf4gxOWPkQ0?si=Dudz6qAsAhgCta3o)

### Practical Understanding
Through this task, I learned how to:
- Configure the ESP32 as a web server  
- Connect ESP32 to a WiFi network  
- Control GPIO pins using HTTP requests  
- Build a simple IoT-based LED control system using a web interface

---

## Task 11 – Soldering Prerequisites

### Objective
The objective of this task was to learn about basic soldering equipment and practice soldering by building a simple LED circuit on a perf board.

### About Soldering
Soldering is the process of joining electronic components using molten solder to form a strong electrical and mechanical connection. It is an important skill in electronics for assembling circuits on PCBs or perf boards.

### Soldering Equipment
The following tools are commonly used in soldering:

- **Soldering Iron** – Used to heat the solder and component leads  
- **Solder Wire** – A metal alloy used to create electrical connections  
- **Flux** – Helps improve solder flow and prevents oxidation  
- **Perf Board** – A board used for assembling prototype circuits  
- **Wire Cutter** – Used to trim excess component leads after soldering  

### Implementation
In this task, a simple LED circuit was assembled on a perf board. The LEDs and resistors were placed on the board and their leads were soldered on the opposite side to form proper electrical connections.

### Screenshots

![Soldered Board](https://raw.githubusercontent.com/nawazhussainhs/Marvel_level_0_images/refs/heads/main/solder1.jpeg)

![LED Circuit](https://raw.githubusercontent.com/nawazhussainhs/Marvel_level_0_images/refs/heads/main/solder2.jpeg)

### Practical Understanding
Through this task, I learned how to safely handle a soldering iron, create proper solder joints, and assemble simple circuits on a perf board.

---

## Task 12 – 555 IC Astable Multivibrator

### Objective
The objective of this task was to study the working of the 555 timer IC in astable mode and generate a square wave with approximately 60% duty cycle.

### About 555 Timer IC
The **555 timer IC** is a widely used integrated circuit for generating time delays, pulses, and oscillations. In **astable mode**, the IC continuously switches between HIGH and LOW states, producing a square wave output without requiring any external trigger.

### Components Used
- 555 Timer IC  
- Resistor **R1 = 4.7 kΩ**  
- Resistor **R2 = 10 kΩ**  
- Capacitors **1 µF and 10 µF**  
- Breadboard  
- 9V Battery  
- Oscilloscope  

### Implementation
In this task, the 555 timer IC was configured in **astable multivibrator mode** using resistors of **4.7 kΩ and 10 kΩ** and capacitors of **1 µF and 10 µF**. The circuit was powered using a **9V battery**.

The output of the 555 timer IC produced a continuous square wave signal. The waveform was observed using an **oscilloscope** to verify the frequency and duty cycle of the signal.

### Screenshots

#### Timer Circuit
![555 Timer Circuit](https://raw.githubusercontent.com/nawazhussainhs/Marvel_level_0_images/refs/heads/main/555_1C.png)

#### Extended Circuit
![Astable Circuit](https://raw.githubusercontent.com/nawazhussainhs/Marvel_level_0_images/refs/heads/main/555_timer_ic.png)

#### Schematic Diagram
![Schematic Diagram](https://raw.githubusercontent.com/nawazhussainhs/Marvel_level_0_images/refs/heads/main/SCHEMATIC_DIAGRAM.png)

#### Output Waveform
![Output Waveform](https://raw.githubusercontent.com/nawazhussainhs/Marvel_level_0_images/refs/heads/main/waveforms.jpeg)

### Practical Understanding
Through this task, I learned how the 555 timer IC works in astable mode and how the values of resistors and capacitors affect the frequency and duty cycle of the output waveform. I also learned how to observe and analyze signals using an oscilloscope.

---

## Task 13 – K-Map & Deriving Logic Gates

### Objective
The objective of this task was to understand Karnaugh Maps (K-Maps) and use them to design a simple burglar alarm circuit using basic logic gates.

### Methodology
Two inputs were considered:

- **D (Door)**
  - 0 → Door Closed  
  - 1 → Door Open  

- **K (Key)**
  - 0 → Key Not Inserted  
  - 1 → Key Inserted  

The output **A** represents the alarm state:

- 0 → Alarm OFF  
- 1 → Alarm ON  

The alarm should activate when the **door opens without inserting the key**, which represents an unauthorized entry.

### Truth Table

![Truth Table](https://raw.githubusercontent.com/nawazhussainhs/Marvel_level_0_images/refs/heads/main/Truth_Table.png)

### Karnaugh Map
The truth table values were placed into a Karnaugh Map to simplify the logic expression.

![K Map](https://raw.githubusercontent.com/nawazhussainhs/Marvel_level_0_images/refs/heads/main/K_Map.png)

Another example showing the simplification process:

![K Map Simplification](https://raw.githubusercontent.com/nawazhussainhs/Marvel_level_0_images/refs/heads/main/kmaps.jpeg)

From the K-map, the simplified Boolean expression is :  
A = D · K'

This means the alarm activates only when **D = 1 (door open)** and **K = 0 (key not inserted)**.

### Practical Understanding
Through this task, I learned how to convert a truth table into a Karnaugh Map and simplify Boolean expressions to design logic circuits using basic gates.

---

## Task 14 – Datasheet Report  
### L293D Motor Driver IC

### Objective
The objective of this task was to study the datasheet of the **L293D motor driver IC** and understand its **pin configuration, internal architecture, H-bridge motor control, and PWM-based speed control** used for driving DC motors using microcontrollers such as Arduino.

### Introduction
The **L293D** is a motor driver integrated circuit used to control **DC motors and stepper motors** in embedded systems and robotics. Microcontrollers cannot directly drive motors because motors require higher current. The L293D acts as an interface between the microcontroller and the motor by amplifying the current and controlling motor direction.

The IC contains **four high-current driver circuits arranged as two H-bridge configurations**, allowing the control of **two DC motors independently**.

### Key Features
- Motor supply voltage: **4.5 V to 36 V**  
- Logic supply voltage: **5 V**  
- Output current: **600 mA per channel**  
- Peak output current: **1.2 A**  
- Built-in clamp diodes for protection  
- Controls **two DC motors or one stepper motor**  
- **16-pin Dual Inline Package (DIP)**  

### Pin Configuration
The **L293D IC contains 16 pins** used for controlling motors and supplying power to the IC.

![L293D Pin Diagram](https://raw.githubusercontent.com/nawazhussainhs/Marvel_level_0_images/refs/heads/main/pindiagram.png)

| Pin Number | Name | Function |
|------------|------|----------|
| 1 | Enable 1,2 | Enables motor driver 1 and 2 |
| 2 | Input 1 | Control input |
| 3 | Output 1 | Connects to motor terminal |
| 4,5 | GND | Ground |
| 6 | Output 2 | Motor output |
| 7 | Input 2 | Control input |
| 8 | Vcc2 | Motor power supply |
| 9 | Enable 3,4 | Enables motor driver 3 and 4 |
| 10 | Input 3 | Control input |
| 11 | Output 3 | Motor output |
| 12,13 | GND | Ground |
| 14 | Output 4 | Motor output |
| 15 | Input 4 | Control input |
| 16 | Vcc1 | Logic supply voltage |

### Internal Architecture / Functional Block Diagram
The **L293D contains four driver circuits internally**, arranged as **two H-bridge circuits**. Each H-bridge allows the motor to rotate in both directions by reversing the current flow.

![Functional Block Diagram](https://raw.githubusercontent.com/nawazhussainhs/Marvel_level_0_images/refs/heads/main/functionalblockdiagram.png)

### Working Principle
The **L293D receives control signals from the microcontroller** through input pins. These signals switch internal transistors that form the H-bridge circuit.

Motor direction depends on the input combination:

| Input 1 | Input 2 | Motor Action |
|--------|--------|--------------|
| 0 | 0 | Motor stops |
| 1 | 0 | Motor rotates forward |
| 0 | 1 | Motor rotates reverse |
| 1 | 1 | Motor stops |

The **Enable pin must be HIGH** for the motor to operate.

### H-Bridge Motor Control
An **H-bridge circuit** allows the polarity of voltage applied to a motor to be reversed. This enables the motor to rotate **clockwise or counter-clockwise**.

The L293D contains **two H-bridge circuits internally**, each capable of controlling one motor.

![H Bridge Diagram](https://raw.githubusercontent.com/nawazhussainhs/Marvel_level_0_images/refs/heads/main/layoutexample.png)

### PWM Speed Control
**Pulse Width Modulation (PWM)** is used to control the speed of a motor.

PWM works by rapidly switching the motor supply ON and OFF. The percentage of ON time (duty cycle) determines motor speed.

- **Higher duty cycle → higher speed**
- **Lower duty cycle → lower speed**

PWM signals are usually applied to the **Enable pin of the L293D**.

### Electrical Characteristics

| Parameter | Value |
|-----------|-------|
| Motor supply voltage | 4.5 V – 36 V |
| Logic voltage | 5 V |
| Output current | 600 mA per channel |
| Peak current | 1.2 A |
| Operating temperature | 0°C – 70°C |

### Applications
- Robotics  
- Automated machines  
- DC motor control circuits  
- Stepper motor control  
- Arduino-based projects  
- Industrial automation  

### Conclusion
The **L293D motor driver IC** is widely used in robotics and embedded systems to control DC motors and stepper motors. It simplifies motor control by integrating **H-bridge circuits within a single chip**. With features like **bidirectional control and PWM compatibility**, the L293D provides an efficient solution for motor driving applications.

### References
1. Texas Instruments – L293D Motor Driver Datasheet  
2. Embedded Systems Motor Driver Applications

---

## Task 15 – Introduction to Virtual Reality (VR)

### Objective
To understand the basic concept of Virtual Reality and experience how immersive environments work.

### Introduction
Virtual Reality (VR) is a technology that creates a simulated 3D environment where users can interact using devices such as VR headsets. In this task, a VR game was experienced to observe how virtual environments respond to user movements.

### Practical Understanding
Through this task, I learned how VR systems create immersive environments and how user actions such as head movement and controller input are detected to interact with objects in the virtual world.

---

## Task 16 – Sad Servers

### Objective
The objective of this task was to practice Linux troubleshooting skills using the Sad Servers platform by identifying and solving a server issue using basic Linux commands.

### Introduction
Sad Servers is an online platform that provides real-world Linux troubleshooting challenges. In this task, the problem was solved by navigating through directories, reading files, and using command-line tools to find the required information.

### Commands Used

```bash
cd /home/admin/clmystery
ls
cat instructions
grep -A 5 "L337" vehicles
cat vehicles
```
### Screenshot
![solution](https://raw.githubusercontent.com/nawazhussainhs/Marvel_level_0_images/refs/heads/main/sad_server.png)

---

## Task 17 – Active Participation

### Objective
To participate in a technical event and apply problem-solving skills using AI tools.

### Description
In this task, I participated in **Impetus 26.0** under the event **CTRL + Z**, which focused on **reverse prompt engineering**. The challenge involved analyzing AI-generated outputs and designing prompts to reproduce similar results. This activity helped in understanding how prompt structure influences AI responses and improved my practical prompt engineering skills.

---

## Closing Note

Thank you for taking the time to review my report.  
Working on these tasks helped me learn many new concepts and gain hands-on experience in different technical areas.