# Internet-Speed-Check-using-Python-with-GUI
Internet Speed Test using Python & Tkinter

A simple desktop application built with **Python** and **Tkinter** to check **Internet Download and Upload Speed** in real time using the `speedtest-cli` library.

---
Features:

Check **Download Speed** (Mbps)
Check **Upload Speed** (Mbps)
Simple and clean **GUI using Tkinter**
One-click speed test
Beginner-friendly Python project

---
Technologies Used:

- **Python 3**
- **Tkinter** (GUI)
- **speedtest-cli** (Internet speed measurement)

---
Project Structure:
Internet-Speed-Test/
│
├── speed_check.py # Main Python file
├── README.md # Project documentation

---
1> Installation & Setup:
Make sure Python 3 is installed
'''bash
python --version

2> Install Required Library
pip install speedtest-cli

HOW IT WORKS :
Click the "Check Speed" button.
The application connects to the nearest speed test server.
It measures:
Download Speed
Upload Speed
Results are displayed in Mbps on the GUI.

Functionality Explanation :
Speed_Check() Function
  Creates a Speedtest object
  Fetches available servers
  Calculates:
    Download speed
    Upload speed
  Updates the GUI labels dynamically
