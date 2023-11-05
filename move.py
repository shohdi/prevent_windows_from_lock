import pyautogui
import time
import ctypes
import signal
import readchar


def handler(signum, frame):
    msg = "Ctrl-c was pressed. Do you really want to exit? y/n "
    print(msg, end="", flush=True)
    res = readchar.readchar()
    if res == 'y':
        print("")
        # set back to normal
        ctypes.windll.kernel32.SetThreadExecutionState(0x80000000)
        exit(1)
    else:
        print("", end="\r", flush=True)
        print(" " * len(msg), end="", flush=True) # clear the printed line
        print("    ", end="\r", flush=True)

if __name__ == "__main__":
    pyautogui.FAILSAFE = False
    # prevent
    ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)
    signal.signal(signal.SIGINT, handler)
    while True:
        try :
            time.sleep(60)
            width = pyautogui.size().width
            height = pyautogui.size().height
            height = height / 2
            print(height)
            #pyautogui.moveTo(x=10,y=height)
            #pyautogui.moveTo(x=width-10,y=height)
            

            
        except Exception as err:
            print("exception happen : ")
            print(f"Unexpected {err=}, {type(err)=}")
           
        



