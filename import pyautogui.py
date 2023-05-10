import pyautogui

# Set the coordinates of the click
x = 500
y = 500

# Click the mouse at the specified coordinates
# wait for 2 minutes before clicking and run it in a loop
n = 0
while n < 10:
    pyautogui.PAUSE = 120
    pyautogui.click(x, y)
