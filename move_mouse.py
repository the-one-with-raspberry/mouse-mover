import pyautogui, time

print("Moving mouse... Press Ctrl+C to exit.")
while True:
    pyautogui.moveRel(0, 100)
    time.sleep(0.5)
    pyautogui.moveRel(-100, 0)
    time.sleep(0.5)
    pyautogui.moveRel(0, -100)
    time.sleep(0.5)
    pyautogui.moveRel(100, 0)
    time.sleep(0.5)