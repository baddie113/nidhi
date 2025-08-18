import os
import platform

#checking
system = platform.system
system = platform.system()

def shutdown(input_str):
    if input_str == "Yes":
        return "shutting down"
        os.system("shutdown /s /t 1") # wait 1 sec berfore shutdown
    elif input_str == "no":
        return "abort shut down"
    else:
        return "sorry"
