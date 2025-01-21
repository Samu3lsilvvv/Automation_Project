import pyautogui
import time 

pyautogui.PAUSE = 2

pyautogui.hotkey("command", "space", interval = 0.5)   
pyautogui.write("safari")
pyautogui.press("enter")  

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(1.5)

pyautogui.click(x=663, y=274)   
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") 
pyautogui.write("sua senha")
pyautogui.click(x=730, y=392) 
pyautogui.press("enter")  
time.sleep(1.5)

import pandas as pd

table = pd.read_csv(r"produtos.csv")

print(table)


for line in table.index:
    pyautogui.click(x=523, y=214)
    codigo = (str(table.loc[line, "codigo"]))
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "custo"]))
    pyautogui.press("tab")
    obs = table.loc[line, "obs"]
    
    if not pd.isna(obs):
        pyautogui.write(str(table.loc[line, "obs"]))
        
    pyautogui.press("tab")
    pyautogui.press("enter") 
    pyautogui.scroll(5000)
