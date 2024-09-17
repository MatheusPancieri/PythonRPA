import pyautogui
import time

# Start Alert
pyautogui.alert("O Codigo vai começar!")
time.sleep(1)

# Abre o google
pyautogui.press('winleft')
time.sleep(0.5)
pyautogui.write('google')
pyautogui.press('enter')

# Abre o GitHub
time.sleep(1)
pyautogui.write('https://github.com/login')
pyautogui.press('enter')
time.sleep(3)

# Entrando na conta
pyautogui.write('exemplo@gmail.com')
pyautogui.press('tab')
pyautogui.write('********')
pyautogui.press('tab', presses=2)
pyautogui.press('enter')
time.sleep(3)

# Criando um novo repositorio
pyautogui.moveTo(359,267)
pyautogui.mouseDown()
pyautogui.mouseUp()
time.sleep(2)
pyautogui.moveTo(852, 460)
pyautogui.mouseDown()
pyautogui.mouseUp()
time.sleep(2)
pyautogui.write('NewRepository')
pyautogui.press('tab', presses=10)
time.sleep(1)
pyautogui.press('enter')
