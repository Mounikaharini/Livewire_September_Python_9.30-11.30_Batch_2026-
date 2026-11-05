'''
import os
cwd = os.getcwd() # Returns current working directory
print(cwd)
print(os.makedirs("data/logs", exist_ok=True)) # Recursively creates directory paths
entries = os.listdir(".") # Returns list of entry names in path
print(entries)
full_path = os.path.join(cwd, "data/logs") # Joins path components with separators
print(full_path)
exists = os.path.exists(full_path) # Checks if path refers to existing file/path
print(exists)
env_var = os.environ.get("PATH") # Accesses system environment variables
print(env_var)
#os.remove("data/logs/file.txt") # Deletes specified file
#os.rmdir("data/logs") # Removes empty directory

import sys
cli_args = sys.argv # Command line arguments list
print(cli_args)
module_paths = sys.path # Search paths for imported modules
print(module_paths)
obj_size = sys.getsizeof(["a", "b"]) # Size of an object in bytes
print(obj_size)
sys.stdout.write("Standard output stream\n")# Writes to standard output buffer
#sys.exit(0) # Exits script with optional exit code

import math
val_sqrt = math.sqrt(64) # Square root calculation
print(val_sqrt)
val_pow = math.pow(2, 5) # Computes x raised to power y
print(val_pow)
ceil_val = math.ceil(4.1) # Rounds up to nearest integer
print(ceil_val)
floor_val = math.floor(4.9) # Rounds down to nearest integer
print(floor_val)
sin_val = math.sin(math.pi / 2) # Trigonometric sine (in radians)
print(sin_val)
cos_val = math.cos(0) # Trigonometric cosine
print(cos_val)
tan_val = math.tan(math.pi / 4) # Trigonometric tangent
print(tan_val)
fact = math.factorial(6) # Returns n factorial
print(fact)
gcd_val = math.gcd(48, 18) # Greatest common divisor
print(gcd_val)


from datetime import datetime
now = datetime.now() # Current local date and time
print(now)
formatted = now.strftime("%Y-%m-%d %H:%M") # Formats datetime object to string
print(formatted)


import time
ts = time.time() # Floating point epoch timestamp in seconds
print(ts)
t1 = time.perf_counter() # High-resolution performance clock counter
print(t1)
time.sleep(2) # Suspends execution for given duration
t2 = time.perf_counter()
print(t2)
struct_time = time.localtime(ts) # Converts epoch seconds to local struct_time
print(struct_time)
str_time = time.asctime(struct_time)
print(str_time)


import calendar
cal_str = calendar.month(2026, 11) # Formatted multi-line monthly calendar
print(cal_str)
is_leap = calendar.isleap(2028) # Returns True if year is a leap year
print(is_leap)
w_day = calendar.weekday(2026, 11, 4) # Weekday index (0=Monday) for date
print(w_day)
start_day, total_days = calendar.monthrange(2026, 11) # Starting weekday and total days
print(start_day, total_days)
'''

import pywhatkit as pwk
#pwk.sendwhatmsg("+1234567890", "Hello", 15, 30) # Schedules WhatsApp message at hr, min
#pwk.sendwhatmsg_instantly("+1234567890", "Fast") # Instantaneous WhatsApp dispatch
#pwk.playonyt("Python Programming") # Searches YouTube & plays top video
pwk.search("Python documentation") # Executes instant Google web query
#pwk.text_to_handwriting("Sample Text", "out.png")
# Converts raw text into handwritten image

pwk.text_to_handwriting("hi")




