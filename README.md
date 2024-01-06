Course Checker:  
Outline:  
  >ftc.py (Find the class): Library of functions and including the main one that runs the entire process  
  >main.py: Checks finals.txt for available classes, asks for classes and sections, picks top one to directly open up a tab in a Google Chrome.  
  >finals.txt: Courses that ftc.py will write in depending on user choice, main.py will take those choices and choose the top one to execute a open tab for registration  
  
Usage Instructions:  
  >Download this to a IDE of your choosing  
  >Download or make sure you have libraries for BeautifulSoup, Selenium, re, sys, tkinter, and subprocess  
  >Run it and it will ask you for the following:  
    >>Course code in XX:XXX:XXX format  
    >>Section ID's you prefer with comma between each or leave blank if no specific choice  
    >>Current Year e.g. 2024 or later  
    >>Semester: Spring or Fall  
  >It runs until it finds a suitable match, or else it checks every 5 minutes.  
