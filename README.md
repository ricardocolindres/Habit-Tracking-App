# Ness-Habit-Tracker

## About The Project

This project was created as a comprehensive solution for people in need of a tool for improving their habits. Ness is a habit tracking app with powerful data analysis modules and user-friendly habit management panels that will help the user track and extract valuable information from habits. Ness is a strong cross-platform application that enables users to track and analyze their habits as a mean to improving their overall life quality.

## Built With
Ness has been built with as few dependencies as possible to secure cross platform compatibility. The entire application is programmed on Python 3.9 and only makes use of standard libraries included in the standard Python installation package. The following standard libraries has been utilized:
•	datetime
•	json
•	re
•	tkinter
•	system

## Getting Started
To run Ness, Python 3.7 or greater must be installed. For more information on installing and updating Python please refer to its official website at https://www.python.org/downloads/ and download the latest version available. Instructions for the installation procedure are available in https://www.python.org/downloads/ as well. Ness should run with no issues for versions of Python 3.7 and greater. However, as of today (April 23, 2021), it has only been tested in Python 3.9 on macOS Big Sur and Windows 10.

Ness can run on MacOS, Windows or Linux. It can easily be compiled into a standalone version for better distribution using  libraries like py2app or pyexe.

**_To access the default account (i.e., an account with preloaded data from over 7 weeks of tracking different habits) use the following credentials:_**

**Email / Username: ricardocolindres@me.com**

**Password: ness29**

**IMPORTANT:** The predefined account (ricardocolindres@me.com) comes with data from seven (7) weeks of tracking five (5) habits. However, the application is tightly integrated with time so by the time anyone downloads these files, all streaks associated with all habits will be lost since the application will register that the user has not completed the habits since the day I last marked them completed (the day files were uploaded) until the day the application is downloaded and run by anyone. Other insights can still be observed in the “My Stats” module.

## Prerequisites
Please install Python 3.7 or greater (preferably Python 3.9). The Tkinter library is part of Python’s standard installation package since Python 3.7, so there is no need to install any external libraries. 

The application’s database is locally managed by two simple JSON files contained in the “data” folder so there is no need for establishing connections with online servers. It’s important to mention that all credentials have no encryption or follow any security protocols whatsoever as this application was not built for commercial distribution but rather for academic purposes. However, having said this, it would be easy modified the database module to implement a more robust database and security protocols.

## Installation 
1.	Download the Ness Folder
2.	Open your preferred Command Line Console
3.	From the Ness Folder, run the main.py file.

Procedures on how to run the script from the command line may vary from system to system. However, there are many great resources online. If Idle (the default IDE installed with the python standard installation package) is installed, you can just doble click the main.py file contained in the Ness Folder and from the “Run” drop down menu you can hit “Run Module” and it will open the application. Any other IDE that has the python interpreter integrated can be used to run the script.
If you have trouble, please email me at: ricardocolindres@me.com and I would be happy to share a standalone version for simple installation. 

## Usage
<img width="952" alt="login" src="https://user-images.githubusercontent.com/83890387/119277475-2e118a00-bbdd-11eb-946c-3fd64110fcf4.png">

<img width="949" alt="mainmodule" src="https://user-images.githubusercontent.com/83890387/119277538-98c2c580-bbdd-11eb-93ce-82a78cb5ea9b.png">

<img width="759" alt="stats" src="https://user-images.githubusercontent.com/83890387/119277685-4d5ce700-bbde-11eb-8c90-8e58e4b18096.png">

**Log In / Sign Up**

This window allows the user log in into his or her account. New users can create an account by clicking on the “New? Sign Up!” button. Follow instructions displayed to properly create a new user. 

**To access the default account (i.e., an account with preloaded data from over 7 weeks of tracking different habits) use the following credentials:**

**Email / Username: ricardocolindres@me.com**

**Password: ness29***

**My Habits Panel**

This panel displays the habits pending for every specific day of the week the user is using the app. Clicking on the “Done” button will register one completion cycle for the habit. Each specific habit needs to be completed as many times in a day as the pre-defined daily goal. Once the user has hit the daily goal for any specific habit, the “Done” button for that habit will change to “Completed” and will be disabled. To visualize the data and insights gathered click the “H STAST!” button.

**Manage My Habits Panel**

This panel displays the ALL habits defined by the user. The user can check all parameters for every single active habit. The parameter displayed are: Time, Habit Name, Daily Goal, and Frequency. Each habit listed has a “Delete” button. If clicked, the user will permanently delete all data associated with the selected habit.

**Clocked Habits Panel**

This panel is used to track habits within a timed session. The user can user the “Set Habit” button to define new clocked habits. To start a session, click on the “Start Session” button. Ness will push a notification every time the stopwatch hits the targeted frequency for each active habit. To user can then select to either skip the habit or mark it as completed. To end the session, click the “End Session” button. To visualize the data gathered from the last 10 sessions, click the “C STAST!” button.

**New Habits Panel**

This panel allows the user to interactively define and create a new habit. The user must enter the habit’s name, its targeted daily frequency (i.e., the number of times the habits should be done on a daily base), the days of the week the user wishes to do the habit, and a general time frame for completion (i.e., morning, afternoon, evening, all time). Once all parameters are defined, the user can proceed to press the “Add” button and the habit will be added to the database.

## Roadmap
No known issues. Please report any issue to ricardocolindres@me.com. 

## License
Distributed under the MIT License. See LICENSE for more information.

## Contact
Ricardo Josue Colindres - @richy2993 - ricardocolindres@me.com
Project Link: https://github.com/ricardocolindres/Ness-Habit-Tracker-



