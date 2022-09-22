import pyautogui as pag
pag.keyDown("command") 
pag.press("tab")
pag.keyUp("command")
pag.sleep(1.5)  
pag.moveTo(162, 100)
pag.leftClick()
pag.press("delete")