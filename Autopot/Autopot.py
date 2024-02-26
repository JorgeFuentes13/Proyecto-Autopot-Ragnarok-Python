from ReadWriteMemory import ReadWriteMemory
import pyautogui
import time
import win32gui, win32ui, win32con


rwm = ReadWriteMemory()

process = rwm.get_process_by_name('xRO.exe')   #Lee el cliente del Ro , EXE
process.open()

hpcurrent = process.get_pointer(17681936)     #Toma el punto de memoria
hpmax = process.get_pointer(17681936+4)
spcurrent = process.get_pointer(17681936+8)
spmax = process.get_pointer(17681936+12)
status = process.get_pointer(17681936+1140)


health_current = process.read(hpcurrent)     #Lee la memoria de hpcurrent
health_max = process.read(hpmax)
sp_current = process.read(spcurrent)
sp_max = process.read(spmax)
status1 = process.read(status)

print({'hpcurrent': health_current, 'hpmax': health_max, 'spcurrent': sp_current, 'spmax': sp_max, 'status' : status1})
# helth_current hp current muestra la hp en el juego
# health_max hp maximo muestra la hp maxima
# sp_current sp current muestra la sp en el juego
# sp_max  sp max muestra la sp en el juego


while 2>1:

    swn= 400
    index = 0
    status_array = []

    # for i  in range(swn,0,-1):
    #     print (i)  
    for i in range(0,401,1):
        statusro = process.read(status + i * 4 )
        if statusro == 4294967295:
            break
        status_array.append(statusro)
        print(statusro)
    
#     health_current = process.read(hpcurrent) 
#     health_max = process.read(hpmax)
#     if health_current < health_max:
#         pyautogui.press("F7")
        
        
#     sp_current = process.read(spcurrent)
#     sp_max = process.read(spmax)
#     if sp_current < sp_max:
#         pyautogui.press("F6")
  
    
    # if 181 not in status_array and health_current > 2: #estoy vivo y muy vivo
    #     pyautogui.press("2") # me tiro Preserve

    # if 181 not in status_array: #estoy vivo y muy vivo
    #     pyautogui.press("2")

time.sleep(0.01)   



