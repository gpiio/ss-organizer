#!/usr/bin/env python3
import os
import shutil
import time

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
screenshots_folder = ('/Users/gp2times/Desktop/Screenshots-dir')

if not os.path.exists(screenshots_folder):
    os.makedirs(screenshots_folder)

while True:
    for file in os.listdir(desktop_path):
        if file.endswith(".png") or file.endswith(".jpg"):
            file_path = os.path.join(desktop_path, file)
            file_time = os.path.getmtime(file_path)
            file_year = time.strftime("%Y", time.localtime(file_time))
            file_month = time.strftime("%m %B", time.localtime(file_time))
            month_folder = os.path.join(screenshots_folder, file_year, file_month)
            if not os.path.exists(month_folder):
                os.makedirs(month_folder)
            shutil.move(file_path, os.path.join(month_folder, file))
    time.sleep(60)