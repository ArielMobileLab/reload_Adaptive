#@Directed by A.W

from cognata_api.web_api.cognata_demo import CognataRequests as cog_api
import time
import os
import threading
import queue
import timeit
import signal
from contextlib import contextmanager
import sys
import json
import keyboard
import rospy
import tkinter as tk
from tkinter import messagebox
from geometry_msgs.msg import Point
from std_msgs.msg import Float64
from sensor_msgs.msg import NavSatFix

root = tk.Tk()
def funOne(x):
	repeat = 1
	while (repeat == 1):
		os.system(x)
		if 'kill -9 $(ps -e | grep SimCloud | head -c 6)':
			repeat = messagebox.askyesno("Warning", "Repeat?")
		if repeat  == 0:
			break


funOne("python3 adaptiveTraining.py train CarControl_0_0 allocentric-rear")
funOne("python3 adaptiveTraining.py load1_cube CarControl_100_0 allocentric-rear")
root.mainloop()





#OnLy GoD cAn judGe mE

