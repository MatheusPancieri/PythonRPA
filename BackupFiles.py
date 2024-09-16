# Importanto as bibliotecas
import pyautogui
import time

# Alerta de começo
pyautogui.alert("O Código vai começar")
pyautogui.PAUSE = 0.5

# Abrir o Google
pyautogui.press('winleft')
pyautogui.write('google')
pyautogui.press('enter')

# Entrar no drive
time.sleep(1)
pyautogui.write("https://drive.google.com/drive")
pyautogui.press('enter')

# Entrar na Aréa de trabalho
pyautogui.hotkey('winleft', 'd')

# Arrastar o arquivo
pyautogui.moveTo(911, 170)
pyautogui.mouseDown()
pyautogui.moveTo(1088, 866)

# Soltar no Drive
pyautogui.hotkey('alt', 'tab')
pyautogui.mouseUp()
time.sleep(5)

# Aviso para Finalização
pyautogui.alert("Terminou!")

#pyautogui.KEYBOARD_KEYS // Mostra todas as keybinds de press para o teclado