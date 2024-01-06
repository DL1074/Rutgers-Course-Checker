import ftc 



a1 = input("What Class? Please enter full id following xx:xxx:xxx pattern: ") # 01:198:111 example
b1 = input("What Section ID's are you looking for, put a comma between each, if all sections leave blank: ")# sections [65,66,67]
d11 = input("What Year (YYYY): ") # 2024
d2 = input("Spring or Fall: ").lower() #
import tkinter as tk

import subprocess

def open_browser(url):
    subprocess.Popen(['start', url], shell=True)

def read_finals():
    with open('finals.txt', 'r') as file:
        lines = file.readlines()
        return lines

def check_finals(a1, b1, d11, d2):
    import time
    while True:
        ftc.doall(a1,b1,d11,d2)
        time.sleep(10)
        lines = read_finals()

        if not lines:
            print("Nothing Retrying...")
            time.sleep(300)  # Wait for 5 min before checking again
            continue

        first_line = lines[0].strip().split()
        link = first_line[1]

        open_browser(link)
        break

# Example usage:
check_finals(a1, b1, d11, d2)
