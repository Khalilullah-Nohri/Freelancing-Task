# CPU Usage Monitor and Web Display

## Objective
This project aims to create a program that monitors CPU usage, sends the data to another program, and displays it in a web browser.

## Requirements
- The program is written in Python 3.x.
- It continuously monitors the CPU usage on the local machine.
- It sends the CPU usage data to another program/process on the same machine through inter-process communication or a simple socket connection.
- The data sent to the other program is displayed in real-time on a web page that shows the current CPU usage. The web page is accessible from a web browser and automatically updates without the need for manual refreshing.

## Task Description
1. A Python program monitors the CPU usage on the local machine using appropriate libraries or system calls to obtain the CPU usage percentage.
2. A data transfer mechanism is implemented to send the CPU usage data from the monitoring program to another Python program/process running on the same machine. This could be achieved using sockets or any other inter-process communication method.
3. A simple web application (using Flask, Django, or any other Python web framework) is developed that receives the CPU usage data from the monitoring program and updates a web page in real-time. The web page shows the current CPU usage percentage.
4. The entire system is tested by running both programs concurrently. It is ensured that the CPU usage data is accurately transferred from the monitoring program to the web application and displayed correctly in a web browser.

## Instructions to Run the Code
1. Install the required libraries: `psutil` and `flask` using pip:
    ```
    pip install psutil flask
    ```
2. Run the CPU usage monitor program in a terminal window.
3. Run the web server program in a separate terminal window.
4. Access the web page displaying the CPU usage at `http://localhost:5000`. The page will update every second without needing to be manually refreshed.
