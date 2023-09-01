# Multiprocessing
from multiprocessing import Process, Pipe

# Excel-related
import xlsxwriter
import pandas as pd

# Web scraping
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests

# Warning and system-related
import warnings
import subprocess
import sys
import time

# Decimal manipulation
from decimal import Decimal

# GUI
import tkinter as tk

# Firefox-related
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager

# Chrome-related
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


# Other
import codecs
import re
import requests


import mysql.connector
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

import multiprocessing
from multiprocessing import Process, Pipe


#from app.scripts.scraping_scripts import scraping1, scraping2, scraping3, scraping4, scraping5, scraping6, scraping7, scraping8, scraping9, scraping10, scraping11

'''
def main_scraping_function():
    t2_start = time.perf_counter()

    conn1, parent_conn1 = multiprocessing.Pipe()
    conn2, parent_conn2 = multiprocessing.Pipe()
    conn3, parent_conn3 = multiprocessing.Pipe()
    conn4, parent_conn4 = multiprocessing.Pipe()
    conn5, parent_conn5 = multiprocessing.Pipe()
    conn6, parent_conn6 = multiprocessing.Pipe()
    conn7, parent_conn7 = multiprocessing.Pipe()
    conn8, parent_conn8 = multiprocessing.Pipe()
    conn9, parent_conn9 = multiprocessing.Pipe()
    conn10, parent_conn10 = multiprocessing.Pipe()
    conn11, parent_conn11 = multiprocessing.Pipe()

    p1 = multiprocessing.Process(
        target=scraping1.get_currency_conversions1, args=(parent_conn1,))
    p2 = multiprocessing.Process(
        target=scraping2.get_currency_conversions2, args=(parent_conn2,))
    p3 = multiprocessing.Process(
        target=scraping3.get_currency_conversions3, args=(parent_conn3,))
    p4 = multiprocessing.Process(
        target=scraping4.get_currency_conversions4, args=(parent_conn4,))
    p5 = multiprocessing.Process(
        target=scraping5.get_currency_conversions5, args=(parent_conn5,))
    p6 = multiprocessing.Process(
        target=scraping6.get_currency_conversions6, args=(parent_conn6,))
    p7 = multiprocessing.Process(
        target=scraping7.get_currency_conversions7, args=(parent_conn7,))
    p8 = multiprocessing.Process(
        target=scraping8.get_currency_conversions8, args=(parent_conn8,))
    p9 = multiprocessing.Process(
        target=scraping9.get_currency_conversions9, args=(parent_conn9,))
    p10 = multiprocessing.Process(
        target=scraping10.get_currency_conversions10, args=(parent_conn10,))
    p11 = multiprocessing.Process(
        target=scraping11.get_currency_conversions11, args=(parent_conn11,))

    p8.start()
    p7.start()
    p9.start()
    p10.start()
    p11.start()
    p5.start()
    p6.start()
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    
    h = conn8.recv()
    g = conn7.recv()
    i = conn9.recv()
    j = conn10.recv()
    k = conn11.recv()
    e = conn5.recv()
    f = conn6.recv()
    a = conn1.recv()
    b = conn2.recv()
    c = conn3.recv()
    d = conn4.recv()
    

    p8.join()
    p7.join()
    p9.join()
    p10.join()
    p11.join()
    p5.join()
    p6.join()
    p1.join()
    p2.join()
    p3.join()
    p4.join()

    t2_stop = time.perf_counter()

    time12 = "runtime: " + "%2.2f" % float(t2_stop - t2_start) + " Seconds"

    return time12
'''