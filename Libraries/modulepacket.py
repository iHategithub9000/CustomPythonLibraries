# modulepacket.py

import os
import time

def SetupDependencies():
    print("Setup: warning, pip is required to call this function")
    time.sleep(1)
    os.system("pip install pygame")
    os.system("pip install pynput")

def modules():
    print('\n\nTo get modules marked with an *, you must install them first using "modulepacket.SetupDependencies()"\n\n')
    print("Module name ---------------- How to import ------------------------ Not preinstalled\n")
    print("sys       ------------------ from modulepacket import sys")
    print("os        ------------------ from modulepacket import os")
    print("time      ------------------ from modulepacket import time")
    print("random    ------------------ from modulepacket import random")
    print("tkinter   ------------------ from modulepacket import tk")
    print("tkinter.ttk ---------------- from modulepacket import ttk")
    print("tkinter.messagebox --------- from modulepacket import messagebox")
    print("tkinter.filedialog --------- from modulepacket import filedialog")
    print("pygame    ------------------ from modulepacket import pygame ------ *")
    print("turtle    ------------------ from modulepacket import turtle")
    print("threading ------------------ from modulepacket import threading")
    print("pynput    ------------------ from modulepacket import pynput ------ *")
import pygame
import turtle
import threading
import pynput
import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import sys
if __name__ == "__main__":
    modules()
    time.sleep(10)