import pyautogui
import time
import keyboard
import random
import win32api, win32con


time.sleep(2)

# tile 1 position: x=409 y=555
# tile 2 position: x=602 y=555
# tile 3 position: x=943 y=555
# tile 4 position: x=1210 y=555

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


iml2 = pyautogui.screenshot(region=(350, 300, 1400, 600))
# iml2.save(r"C:\Users\galha\Desktop\aimboosterBOT\savedimage22.png")
# Main loop: runs until 'q' is pressed
while not keyboard.is_pressed('q'):

    if(pyautogui.pixel(409, 555)[0] == 0):
        click(409, 555)
    if (pyautogui.pixel(602, 555)[0] == 0):
        click(602, 555)
    if (pyautogui.pixel(943, 555)[0] == 0):
        click(943, 555)
    if (pyautogui.pixel(1210, 555)[0] == 0):
        click(1210, 555)



