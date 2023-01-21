import os
import shutil
import pyautogui

# | os.getcwd() |: saber ubicacion

# obtener la ubicacion de trabajo actual
# print(os.getcwd())
# --------------------------------------------------------------------------------------------
# | os.mkdir() |: crear carpetas

# crear carpetas
# os.mkdir("caperta-test")

# path del desktop y crear una carpeta en 
# desktop = os.path.join(os.path.expanduser("~"), "Desktop")
# os.mkdir(f"{desktop}\\New Folder")
# --------------------------------------------------------------------------------------------
# | os.listdir() |: listar archivos

# list = os.listdir()

# print(list)
# --------------------------------------------------------------------------------------------
# SHUTIL (COPIAR Y PERGAR ARCHIVOS)

# copiar un archivo
# shutil.copy2("script.py", "script_copy.py")

# GUSANO QUE COLAPSE EL PC
# print("archivos creados")

# i = 0

# while i <= 50:
#     shutil.copy2("script.py", f"script_gusano{i}.py")
#     i += 1

# print("Eliminado archivos.....")

# import time
# time.sleep(5)

# for file in os.listdir():
#     if file.startswith("script_gusano") == True:
#         os.remove(file)

# --------------------------------------------------------------------------------------------
# | os.system() |: ordenar que se ejecuten comandos

# os.system("python -m http.server 5000")
# --------------------------------------------------------------------------------------------
# PYAUTOGUI

pyautogui.press("win")

pyautogui.typewrite("bloc de notas\n", interval=0.12)

pyautogui.typewrite("! HACKEADO !", interval=0.12)

pyautogui.hotkey("ctrl", "shift", "escape")
# --------------------------------------------------------------------------------------------
# LEER UN DOCUMENTO

# doc = open("text.txt", "r")

# content = doc.read()

# print(content)