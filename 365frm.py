import os
import pyautogui
import time
from pynput import keyboard
from pynput.keyboard import Controller
import threading

pyautogui.FAILSAFE=False


merkasako=0
full=0

# Obtener las dimensiones de la pantalla
screen_width, screen_height = pyautogui.size()

# Definir los límites del área de búsqueda para la mitad de la pantalla hacia abajo
abajo_region = (0, screen_height // 2, screen_width, screen_height // 2)

# Definir los límites del área de búsqueda para la mitad de la pantalla hacia arriba
arriba_region = (0, 0, screen_width, screen_height // 2)

agotado = {
    "agotado": os.path.join("imgs_programa","agotado.jpeg"),
}
min_20 = {
    "min_20": os.path.join("imgs_programa","min_20.jpeg"),
}
min_40 = {
    "min_40": os.path.join("imgs_programa","min_40.jpeg"),
}
min_100 = {
    "min_100": os.path.join("imgs_programa","min_100.jpeg"),
}
pesc_20 = {
    "pesc_20": os.path.join("imgs_programa","pesc_20.jpeg"),
}
pesc_40 = {
    "pesc_40": os.path.join("imgs_programa","pesc_40.jpeg"),
}
pescar = {
    "pescar": os.path.join("imgs_programa","pescar.jpeg"),
}
recolectar = {
    "recolectar": os.path.join("imgs_programa","recolectar.jpeg"),
}
x = {
    "x": os.path.join("imgs_programa","x.jpeg"),
}
bank_way_1 = {
    "bank_way_1": os.path.join("imgs_programa","bank_way_1.jpeg"),
    "bank_way_11": os.path.join("imgs_programa","bank_way_11.jpeg")
}
bank_way_2 = {
    "bank_way_2": os.path.join("imgs_programa","bank_way_2.jpeg"),
    "bank_way_22": os.path.join("imgs_programa","bank_way_22.jpeg")
}
bank_way_3 = {
    "bank_way_3": os.path.join("imgs_programa","bank_way_3.jpeg"),
    "bank_way_33": os.path.join("imgs_programa","bank_way_33.jpeg")
}
bank_way_4 = {
    "bank_way_4": os.path.join("imgs_programa","bank_way_4.jpeg"),
    "bank_way_44": os.path.join("imgs_programa","bank_way_44.jpeg")
}
bank_way_5 = {
    "bank_way_5": os.path.join("imgs_programa","bank_way_5.jpeg"),
    "bank_way_55": os.path.join("imgs_programa","bank_way_55.jpeg")
}
bank_way_6 = {
    "bank_way_6": os.path.join("imgs_programa","bank_way_6.jpeg"),
    "bank_way_66": os.path.join("imgs_programa","bank_way_66.jpeg")
}

print("7 segundos, vaya a la ventana")
time.sleep(7)  # Esperar

#////////////////////////
def map_uno():
    ######
    pyautogui.moveTo(264, 454)
    time.sleep(1)  # Esperar
    for _, image_path in recolectar.items(): # Buscar
        encontrado = pyautogui.locateOnScreen(image_path, confidence=0.9)
        if encontrado:
            pyautogui.click(264, 454)
            time.sleep(6.5)  # Esperar
        else:
            break
    ######
    pyautogui.moveTo(328, 492)
    time.sleep(1)  # Esperar
    for _, image_path in recolectar.items(): # Buscar
        encontrado = pyautogui.locateOnScreen(image_path, confidence=0.9)
        if encontrado:
            pyautogui.click(328, 492)
            time.sleep(6.4)  # Esperar
        else:
            break
    ######
    pyautogui.moveTo(456, 371)
    time.sleep(1)  # Esperar
    for _, image_path in recolectar.items(): # Buscar 
        encontrado = pyautogui.locateOnScreen(image_path, confidence=0.9)
        if encontrado:
            pyautogui.click(456, 371)
            time.sleep(6)  # Esperar
        else:
            break
    ######
    pyautogui.moveTo(488, 347)
    time.sleep(1)  # Esperar
    for _, image_path in recolectar.items(): # Buscar 
        encontrado = pyautogui.locateOnScreen(image_path, confidence=0.9)
        if encontrado:
            pyautogui.click(488, 347)
            time.sleep(6.2)  # Esperar
        else:
            break
    ######
    pyautogui.moveTo(693, 280)
    time.sleep(1)  # Esperar
    for _, image_path in recolectar.items(): # Buscar 
        encontrado = pyautogui.locateOnScreen(image_path, confidence=0.9)
        if encontrado:
            pyautogui.click(693, 280)
            time.sleep(6.1)  # Esperar
        else:
            break
    ######
    pyautogui.moveTo(728, 266)
    time.sleep(1)  # Esperar
    for _, image_path in recolectar.items(): # Buscar 
        encontrado = pyautogui.locateOnScreen(image_path, confidence=0.9)
        if encontrado:
            pyautogui.click(728, 266)
            time.sleep(6)  # Esperar
        else:
            break
    ######
    pyautogui.moveTo(809, 210)
    time.sleep(1)  # Esperar
    for _, image_path in recolectar.items(): # Buscar 
        encontrado = pyautogui.locateOnScreen(image_path, confidence=0.9)
        if encontrado:
            pyautogui.click(809, 210)
            time.sleep(5.9)  # Esperar
        else:
            break
    ######
    pyautogui.moveTo(935, 305)
    time.sleep(1)  # Esperar
    for _, image_path in recolectar.items(): # Buscar 
        encontrado = pyautogui.locateOnScreen(image_path, confidence=0.9)
        if encontrado:
            pyautogui.click(935, 305)
            time.sleep(6)  # Esperar
        else:
            break
    pyautogui.moveTo(1079, 180)
    time.sleep(0.5)
    pyautogui.click(1079, 180)
    time.sleep(4)

#////////////////////////
def map_dos():
    ######
    pyautogui.moveTo(311, 349)
    time.sleep(1)  # Esperar
    for _, image_path in recolectar.items(): # Buscar 
        encontrado = pyautogui.locateOnScreen(image_path, confidence=0.9)
        if encontrado:
            pyautogui.click(311, 349)
            time.sleep(5)  # Esperar
        else:
            break
    ######
    pyautogui.moveTo(352, 329)
    time.sleep(1)  # Esperar
    for _, image_path in recolectar.items(): # Buscar 
        encontrado = pyautogui.locateOnScreen(image_path, confidence=0.9)
        if encontrado:
            pyautogui.click(352, 329)
            time.sleep(4.5)  # Esperar
        else:
            break
    ######
    pyautogui.moveTo(408, 296)
    time.sleep(1)  # Esperar
    for _, image_path in recolectar.items(): # Buscar 
        encontrado = pyautogui.locateOnScreen(image_path, confidence=0.9)
        if encontrado:
            pyautogui.click(408, 296)
            time.sleep(6.1)  # Esperar
        else:
            break
    ######
    pyautogui.moveTo(452, 280)
    time.sleep(1)  # Esperar
    for _, image_path in recolectar.items(): # Buscar 
        encontrado = pyautogui.locateOnScreen(image_path, confidence=0.9)
        if encontrado:
            pyautogui.click(452, 280)
            time.sleep(6.3)  # Esperar
        else:
            break
    ######
    pyautogui.moveTo(660, 167)
    time.sleep(1)  # Esperar
    for _, image_path in recolectar.items(): # Buscar 
        encontrado = pyautogui.locateOnScreen(image_path, confidence=0.9)
        if encontrado:
            pyautogui.click(660, 167)
            time.sleep(6.8)  # Esperar
        else:
            break
    ######
    pyautogui.moveTo(845, 158)
    time.sleep(1)  # Esperar
    for _, image_path in recolectar.items(): # Buscar 
        encontrado = pyautogui.locateOnScreen(image_path, confidence=0.9)
        if encontrado:
            pyautogui.click(845, 158)
            time.sleep(7)  # Esperar
        else:
            break
    ######
    pyautogui.moveTo(912, 146)
    time.sleep(1)  # Esperar
    for _, image_path in recolectar.items(): # Buscar 
        encontrado = pyautogui.locateOnScreen(image_path, confidence=0.9)
        if encontrado:
            pyautogui.click(912, 146)
            time.sleep(7.3)  # Esperar
        else:
            break
    ######
    pyautogui.moveTo(981, 163)
    time.sleep(1)  # Esperar
    for _, image_path in recolectar.items(): # Buscar 
        encontrado = pyautogui.locateOnScreen(image_path, confidence=0.9)
        if encontrado:
            pyautogui.click(981, 163)
            time.sleep(7.3)  # Esperar
        else:
            break
    ######
    pyautogui.moveTo(781, 361)
    time.sleep(1)  # Esperar
    for _, image_path in recolectar.items(): # Buscar 
        encontrado = pyautogui.locateOnScreen(image_path, confidence=0.9)
        if encontrado:
            pyautogui.click(781, 361)
            time.sleep(7)  # Esperar
        else:
            break
    ######
    pyautogui.moveTo(830, 337)
    time.sleep(1)  # Esperar
    for _, image_path in recolectar.items(): # Buscar 
        encontrado = pyautogui.locateOnScreen(image_path, confidence=0.9)
        if encontrado:
            pyautogui.click(830, 337)
            time.sleep(7)  # Esperar
        else:
            break
    ######
    pyautogui.moveTo(1022, 203)
    time.sleep(1)  # Esperar
    for _, image_path in recolectar.items(): # Buscar 
        encontrado = pyautogui.locateOnScreen(image_path, confidence=0.9)
        if encontrado:
            pyautogui.click(1022, 203)
            time.sleep(7)  # Esperar
        else:
            break
    pyautogui.moveTo(1101, 421)
    time.sleep(0.5)
    pyautogui.click(1101, 421)
    time.sleep(5.5)

#////////////////////////
def map_tres():
    ######
    pyautogui.moveTo(572, 159)
    time.sleep(1)  # Esperar
    for _, image_path in recolectar.items(): # Buscar 
        encontrado = pyautogui.locateOnScreen(image_path, confidence=0.9)
        if encontrado:
            pyautogui.click(572, 159)
            time.sleep(5.5)  # Esperar
        else:
            break
    ######
    pyautogui.moveTo(719, 116)
    time.sleep(1)  # Esperar
    for _, image_path in recolectar.items(): # Buscar 
        encontrado = pyautogui.locateOnScreen(image_path, confidence=0.9)
        if encontrado:
            pyautogui.click(719, 116)
            time.sleep(5.8)  # Esperar
        else:
            break
    ######
    pyautogui.moveTo(753, 139)
    time.sleep(1)  # Esperar
    for _, image_path in recolectar.items(): # Buscar 
        encontrado = pyautogui.locateOnScreen(image_path, confidence=0.9)
        if encontrado:
            pyautogui.click(753, 139)
            time.sleep(6)  # Esperar
        else:
            break
    ######
    pyautogui.moveTo(655, 308)
    time.sleep(1)  # Esperar
    for _, image_path in recolectar.items(): # Buscar 
        encontrado = pyautogui.locateOnScreen(image_path, confidence=0.9)
        if encontrado:
            pyautogui.click(655, 308)
            time.sleep(5.7)  # Esperar
        else:
            break
    ######
    pyautogui.moveTo(482, 357)
    time.sleep(1)  # Esperar
    for _, image_path in recolectar.items(): # Buscar 
        encontrado = pyautogui.locateOnScreen(image_path, confidence=0.9)
        if encontrado:
            pyautogui.click(482, 357)
            time.sleep(5.9)  # Esperar
        else:
            break
    ######
    pyautogui.moveTo(917, 253)
    time.sleep(1)  # Esperar
    for _, image_path in recolectar.items(): # Buscar 
        encontrado = pyautogui.locateOnScreen(image_path, confidence=0.9)
        if encontrado:
            pyautogui.click(917, 253)
            time.sleep(6.2)  # Esperar
        else:
            break
    
    pyautogui.moveTo(826, 510)
    time.sleep(0.5)
    pyautogui.click(826, 510)
    time.sleep(5.2)

#////////////////////////
def map_cuatro():
    ###### el 1 al lado del puente
    pyautogui.moveTo(665, 337)
    time.sleep(0.8)  # Esperar
    for _, image_path in pescar.items(): # Buscar 
        encontrado = pyautogui.locateOnScreen(image_path, confidence=0.9)
        if encontrado:
            pyautogui.click(665, 337)
            time.sleep(5)  # Esperar
        else:
            break
    ###### al otro lado donde hay 4 normalmente, el primero de la esquina
    pyautogui.moveTo(1091, 390)
    time.sleep(0.8)  # Esperar
    for _, image_path in pescar.items(): # Buscar 
        encontrado = pyautogui.locateOnScreen(image_path, confidence=0.9)
        if encontrado:
            pyautogui.click(1091, 390)
            time.sleep(5.5)  # Esperar
        else:
            break
    ###### el que le sigue (2)
    pyautogui.moveTo(1028, 421)
    time.sleep(0.8)  # Esperar
    for _, image_path in pescar.items(): # Buscar 
        encontrado = pyautogui.locateOnScreen(image_path, confidence=0.9)
        if encontrado:
            pyautogui.click(1028, 421)
            time.sleep(5.5)  # Esperar
        else:
            break
    ###### 3
    pyautogui.moveTo(894, 455)
    time.sleep(0.8)  # Esperar
    for _, image_path in pescar.items(): # Buscar 
        encontrado = pyautogui.locateOnScreen(image_path, confidence=0.9)
        if encontrado:
            pyautogui.click(894, 455)
            time.sleep(5.6)  # Esperar
        else:
            break
    ######
    pyautogui.moveTo(665, 605)
    time.sleep(0.8)  # Esperar
    for _, image_path in pescar.items(): # Buscar 
        encontrado = pyautogui.locateOnScreen(image_path, confidence=0.9)
        if encontrado:
            pyautogui.click(665, 605)
            time.sleep(5.7)  # Esperar
        else:
            break
    ######
    pyautogui.moveTo(566, 455)
    time.sleep(0.8)  # Esperar
    for _, image_path in pescar.items(): # Buscar 
        encontrado = pyautogui.locateOnScreen(image_path, confidence=0.9)
        if encontrado:
            pyautogui.click(566, 455)
            time.sleep(5.9)  # Esperar
        else:
            break
    ######
    pyautogui.moveTo(534, 472)
    time.sleep(0.8)  # Esperar
    for _, image_path in pescar.items(): # Buscar 
        encontrado = pyautogui.locateOnScreen(image_path, confidence=0.9)
        if encontrado:
            pyautogui.click(534, 472)
            time.sleep(6.3)  # Esperar
        else:
            break
    ######
    pyautogui.moveTo(432, 455)
    time.sleep(0.8)  # Esperar
    for _, image_path in pescar.items(): # Buscar 
        encontrado = pyautogui.locateOnScreen(image_path, confidence=0.9)
        if encontrado:
            pyautogui.click(894, 455)
            time.sleep(6.6)  # Esperar
        else:
            break
    
    
    
    
    #pyautogui.moveTo(826, 510)
    #time.sleep(0.5)
    #pyautogui.click(826, 510)
    #time.sleep(5.2)


#////////////////////////
def map_cinco():
    ######
    pyautogui.moveTo(264, 454)





def bank_way():
    pyautogui.moveTo(275, 605)
    time.sleep(0.2)
    pyautogui.click(275, 605)
    time.sleep(5)
    ######
    pyautogui.moveTo(763, 6)
    time.sleep(0.5)  # Esperar
    buscando=True
    while buscando:
        for _, image_path in bank_way_1.items(): # Buscar 
            encontrado = pyautogui.locateOnScreen(image_path, confidence=0.9)
            if encontrado:
                buscando=False
                time.sleep(1)  # Esperar
                pyautogui.click(763, 6)
                break
    buscando=True
    while buscando:
        for _, image_path in bank_way_2.items(): # Buscar 
            encontrado = pyautogui.locateOnScreen(image_path, confidence=0.9)
            if encontrado:
                buscando=False
                time.sleep(1)  # Esperar
                pyautogui.click(1308, 395)
                break
    buscando=True
    while buscando:
        for _, image_path in bank_way_3.items(): # Buscar 
            encontrado = pyautogui.locateOnScreen(image_path, confidence=0.9)
            if encontrado:
                buscando=False
                time.sleep(1)  # Esperar
                pyautogui.click(1308, 395)
                break
    buscando=True
    while buscando:
        for _, image_path in bank_way_4.items(): # Buscar 
            encontrado = pyautogui.locateOnScreen(image_path, confidence=0.9)
            if encontrado:
                buscando=False
                time.sleep(1)  # Esperar
                pyautogui.click(1308, 395)
                break
    buscando=True
    while buscando:
        for _, image_path in bank_way_5.items(): # Buscar 
            encontrado = pyautogui.locateOnScreen(image_path, confidence=0.9)
            if encontrado:
                buscando=False
                time.sleep(1)  # Esperar
                pyautogui.click(813, 270) # Bank door
                break
    buscando=True
    while buscando:
        for _, image_path in bank_way_6.items(): # Buscar 
            encontrado = pyautogui.locateOnScreen(image_path, confidence=0.9)
            if encontrado:
                buscando=False
                time.sleep(1)  # Esperar
                pyautogui.click(799, 320) # NPC Bank
                break

    time.sleep(1.5)
    pyautogui.click(627, 553) # Chat option
    time.sleep(1.9)
    pyautogui.click(1061, 96) # Resources
    time.sleep(0.4)
    pyautogui.click(914, 94) # Transferencia avanzada
    time.sleep(0.4)
    pyautogui.click(976, 125) # Visibles
    time.sleep(0.7)
    pyautogui.click(1136, 67) # X
    time.sleep(0.7)
    pyautogui.click(494, 510) # Out
    time.sleep(0.7)
    
    # Go back Farm Zone
    buscando=True
    while buscando:
        for _, image_path in bank_way_5.items(): # Buscar 
            encontrado = pyautogui.locateOnScreen(image_path, confidence=0.9)
            if encontrado:
                buscando=False
                time.sleep(1)  # Esperar
                pyautogui.click(130, 343)
                break
    # Go back Farm Zone
    buscando=True
    while buscando:
        for _, image_path in bank_way_4.items(): # Buscar 
            encontrado = pyautogui.locateOnScreen(image_path, confidence=0.9)
            if encontrado:
                buscando=False
                time.sleep(1)  # Esperar
                pyautogui.click(130, 343)
                break
    # Go back Farm Zone
    buscando=True
    while buscando:
        for _, image_path in bank_way_3.items(): # Buscar 
            encontrado = pyautogui.locateOnScreen(image_path, confidence=0.9)
            if encontrado:
                buscando=False
                time.sleep(1)  # Esperar
                pyautogui.click(130, 343)
                break
    # Go back Farm Zone
    buscando=True
    while buscando:
        for _, image_path in bank_way_2.items(): # Buscar 
            encontrado = pyautogui.locateOnScreen(image_path, confidence=0.9)
            if encontrado:
                buscando=False
                time.sleep(1)  # Esperar
                pyautogui.click(796, 676)
                break
    # Go back Farm Zone
    buscando=True
    while buscando:
        for _, image_path in bank_way_1.items(): # Buscar 
            encontrado = pyautogui.locateOnScreen(image_path, confidence=0.9)
            if encontrado:
                buscando=False
                time.sleep(1)  # Esperar
                pyautogui.click(825, 455)
                break
    time.sleep(8)
    pyautogui.click(1078, 177)
    time.sleep(2)
    pyautogui.click(212, 564)
    time.sleep(2)

def devolverse():
    #Desde map 4
    ######
    pyautogui.moveTo(640, 132)
    time.sleep(0.2)
    pyautogui.click(640, 132)
    time.sleep(5.6)
    ######
    pyautogui.moveTo(354, 185)
    time.sleep(0.2)
    pyautogui.click(354, 185)
    time.sleep(4.4)
    ######
    pyautogui.moveTo(229, 569)
    time.sleep(0.2)
    pyautogui.click(229, 569)
    time.sleep(5.1)

def parar_programa():
    global running
    running = False

def on_press(key):
    global timer
    if key == keyboard.Key.ctrl_l:
        print("Ctrl presionado")

def on_release(key):
    global timer
    key_to_hours = {keyboard.KeyCode.from_char(str(i)): i for i in range(1, 10)} # Hasta 9 horas

    if key == keyboard.Key.ctrl_l:
        print("Ctrl liberado")
    elif key in key_to_hours and timer is None:
        hours = key_to_hours[key]
        print(f"Detener el programa en {hours} horas")
        timer = threading.Timer(hours * 3600, parar_programa)
        timer.start()

def press_h():
    keyboard = Controller()
    keyboard.press('h')
    keyboard.release('h')
    
def map_merkasako():
    time.sleep(3)
    pyautogui.click(730, 291)
    time.sleep(2.3)
    pyautogui.click(1061, 96)
    time.sleep(0.4)
    pyautogui.click(914, 94)
    time.sleep(0.4)
    pyautogui.click(976, 125)
    time.sleep(0.7)
    pyautogui.click(1136, 67)
    time.sleep(0.7)
    press_h()

def buscar_x():
    for _, image_path in x.items(): # Buscar 
        encontrado = pyautogui.locateOnScreen(image_path, confidence=0.9)
        if encontrado:
            center = pyautogui.center(encontrado)
            pyautogui.click(center)
        else:
            break

running = True
timer = None

try:
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        while running:
            if merkasako > 20:
                press_h()
                map_merkasako()
                merkasako=0
                full+=1
            map_uno()
            buscar_x()
            map_dos()
            buscar_x()
            map_tres()
            buscar_x()
            map_cuatro()
            buscar_x()
            map_cinco()
            buscar_x()
            devolverse()
            if full>1:
                bank_way()
                full=0
            merkasako += 1
        
except FileNotFoundError as e:
    print(f"Error de archivo no encontrado: {e}")
except ValueError as e:
    print(f"Error de valor: {e}")
except Exception as e:
    print(f"Se produjo un error: {e}")
finally:
    input("Presione cualquier tecla para cerrar...")