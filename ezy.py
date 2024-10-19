# ezy calculator
import os
import winsound
from datetime import datetime
import time
import webbrowser

# some links for popular web pages
GOOGLE_PAGE_LINK = 'https://www.google.com/'
GITHUB_PAGE_LINK = 'https://github.com/'
LICHESS_PAGE_LINK = 'https://lichess.org/'
CHESS_COM_PAGE_LINK = 'https://www.chess.com/'
YOUTUBE_PAGE_LINK = 'https://www.youtube.com/'
THINGIVERSE_PAGE_LINK = 'https://www.thingiverse.com/'

# soem static mathimatick numbers
P = 3.1415926535897932
E = 2.7182818284590452
F = 1.618033988749895

# some RGB colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0,)

class calculator:
 """A class for simple arithmatick operations"""

 @staticmethod
 def add(a, b):
  """Ads 2 numbers, with error handling"""
  try:
   a = float(a)
   b = float(b)
   return a + b
  except:
   raise ValueError

 @staticmethod
 def subtract(a, b):
  """Subtracts 2 numbers, with error handling"""
  try:
   a = float(a)
   b = float(b)
   return a - b
  except:
   raise ValueError

 @staticmethod
 def multiply(a, b):
  """Multyplaise the first number with the second, with error handling"""
  try:
   a = float(a)
   b = float(b)
   return a * b
  except:
   raise ValueError

 @staticmethod
 def divide(a, b):
  """Devids 2 numbers, with error handling for zero devission error"""
  if b == 0:
   raise ZeroDivisionError("Cannot divide by zero")
  try:
   a = float(a)
   b = float(b)
   return a / b
  except:
   raise ValueError

 @staticmethod
 def floor_division(a, b):
  if b == 0:
   raise ZeroDivisionError("Cannot divide by zero")
  try:
   a = float(a)
   b = float(b)
   return a // b
  except:
   raise ValueError

 @staticmethod
 def modulus(a, b):
  if b == 0:
   raise ZeroDivisionError("Cannot divide by zero")
  try:
   a = float(a)
   b = float(b)
   return a % b
  except:
   raise ValueError

 @staticmethod
 def power(base, exponent):
  return base ** exponent

 @staticmethod
 def square_root(number):
  if number > 0:
   try:
    number = float(number)
    return number ** 0.5
   except:
    raise ValueError

class file_manager:

 @staticmethod
 def open_file(file_name, method, c=None):
  if method.lower() == 'r':
   with open(file_name, 'r') as file:
    content = file.read()
   return content
  elif method.lower() == 'w':
   if c is None:
    raise ValueError
   with open(file_name, 'w') as file:
    file.write(str(c))

 @staticmethod
 def Make_file(fn):
  try:
   os.makedirs(fn, exist_ok=True)
  except PermissionError:
   raise PermissionError
  except OSError:
   raise OSError
  except:
   raise

 @staticmethod
 def remove_file(File_directory):
  try:
   os.remove(File_directory)
  except PermissionError:
   raise PermissionError
  except FileNotFoundError:
   raise FileNotFoundError
  except:
   raise

class system:

 @staticmethod
 def Check_operation_system():
  global system_windows, system_unix_based
  if os.name == 'nt':
   system_windows = True
   system_unix_based = False
   return
  else:
   system_windows = False
   system_unix_based = True
   return

 @staticmethod
 def Clear_console():
  if os.name == 'nt':
   os.system('cls')
  else:
    os.system('clear')

class general:

 @staticmethod
 def Beep(Frequency=1000, Duration=2000):
  if os.name == 'nt':
   winsound.Beep(Frequency, Duration)
  else:
   return

 @staticmethod
 def show_dateTime(status):
  if status.lower() == "date":
   return datetime.now().date()
  elif status.lower() == "DateTime":
   return datetime.now()
  else:
   return "Wrong option. Type 'Date' for only date and 'DateTime' for date and time."

 @staticmethod
 def sleep(t):
  time.sleep(t)

 @staticmethod
 def Open_web_page(page_link):
  try:
   webbrowser.open(page_link)
  except:
   raise
  