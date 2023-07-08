import pyautogui
import time
import keyboard
from datetime import datetime
import win32api, win32con

# TO DO, HACER QUE CAMBIE EL NIVEL DEL RSS SI DA QUE TIENE LEGIONES INACTIVAS > 5 VECES


#############################################
# FUNCIONES BASICAS
#############################################
def click(x, y):
    time.sleep(0.5)
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(0.5)


def press_key(key):
    time.sleep(0.5)
    pyautogui.keyDown(key)
    time.sleep(0.1)
    pyautogui.keyUp(key)
    time.sleep(0.5)


def check_is_white(x, y):
    if (
        pyautogui.pixel(x, y)[0] in range(250, 256)
        and pyautogui.pixel(x, y)[1] in range(250, 256)
        and pyautogui.pixel(x, y)[2] in range(250, 256)
    ):
        return True
    else:
        return False


def check_is_black(x, y):
    if (
        pyautogui.pixel(x, y)[0] == 0
        and pyautogui.pixel(x, y)[1] == 0
        and pyautogui.pixel(x, y)[2] == 0
    ):
        return True
    else:
        return False


#############################################
# MENU
#############################################
def menu():
    orden = []
    print(
        """Que queres farmear wachin?
    1) Oro
    2) Madera
    3) Piedra
    4) Mana
    """
    )
    for i in range(1, 6):
        while True:
            try:
                rss = int(input(f"Ingrese el recurso n° {i}: "))
                if rss in range(1, 5):
                    if rss == 1:
                        send = "oro"
                    elif rss == 2:
                        send = "madera"
                    elif rss == 3:
                        send = "piedra"
                    else:
                        send = "mana"
                    orden.append(send)
                    break
                else:
                    print("El numero debe ser del 1 al 4...")
            except:
                print("no ingreso un numero valido...")

    return orden


def set_timer():
    while True:
        try:
            timer = int(input("Check again every (in minutes): "))
            break
        except:
            print("Only insert numbers")

    timer_final = timer * 60
    return timer_final


#############################################
# FUNCIONES
#############################################


def esta_online():
    if pyautogui.pixel(960, 630)[0] != 0:
        print("STATUS = ONLINE")
        return True

    else:
        print("STATUS = OFFLINE")
        return False


def esta_en_city():
    press_key("b")
    # checkea que se abrio la pag de construir
    if check_is_black(600, 800):
        # sale de la pag de construir
        press_key("esc")
        # sale de la ciudad
        press_key("space")


def check_any_active():
    press_key("j")
    if check_is_white(1400, 900):
        return True
    else:
        return False


def check_active_legions():
    # hay alguna legion activa
    if check_any_active():
        # todas las legiones activas
        if not check_is_white(1625, 630):
            press_key("esc")
            return True

        else:
            press_key("esc")
            return False
    # ninguna legion activa
    else:
        return False


def select_rss(rss_x):
    # click en el recurso
    click(rss_x, 940)
    # click en buscar
    click(rss_x, 850)


def click_to_gather():
    # click en el recurso
    click(950, 535)
    # click en cosechar
    click(730, 660)


def select_legion():
    # click donde se selecciona agregar legion
    click(1550, 360)
    # sacar diputado
    click(953, 438)
    # click mandar a cosechar
    click(1320, 820)


def legion_send_farm(rss):
    rss_dict = {"oro": 770, "madera": 950, "piedra": 1140, "mana": 1320}
    press_key("f")
    select_rss(rss_dict[rss])
    click_to_gather()
    select_legion()


# def rotate_saves():
#     click(1470, 385)
#     click(1415, 375)
#     click(1365, 375)
#     click(1315, 375)
#     click(1265, 375)
#     click(1215, 375)


def salir_menu():
    press_key("esc")
    time.sleep(4)


def acomodar_profundidad():
    press_key("space")
    time.sleep(2)
    press_key("space")


def main():
    global ord_copy
    while True:
        # esta online
        if esta_online():
            salir_menu()
            esta_en_city()
            acomodar_profundidad()
            while True:
                # no hay legiones inactivas
                if check_active_legions():
                    print("TODO ACTIVO")
                    break
                # hay legiones inactivas
                else:
                    # si se cumplio todo el carrito, se vuelve a cargar de 0
                    if len(ord_copy) == 0:
                        ord_copy = ord.copy()

                    print(f"LEGION INACTIVA ==> {ord_copy[0]}")

                    # mando esta legion a farmear
                    legion_send_farm(ord_copy[0])
                    # saco recurso del carrito
                    ord_copy.remove(ord_copy[0])
            break
        else:
            # esta offline, click en conectarse
            click(945, 620)
            # espera 30 segundos para darle tiempo a conectarse
            time.sleep(30)


##############################################################################################

ord = menu()
timer = set_timer()
time.sleep(5)

ord_copy = ord.copy()

print("Iniciando farmeo...")
print("-------------------------------")
while True:
    print(f"inicio: {datetime.now().strftime('%H:%M:%S')}")
    main()
    print(f"fin: {datetime.now().strftime('%H:%M:%S')}")
    print("-------------------------------")
    time.sleep(timer - 60)
    print(datetime.now().strftime("%H:%M:%S"))
    print("Comienza en un minuto...")
    time.sleep(55)
    contador = (5, 4, 3, 2, 1)
    for x in contador:
        print(x)
        time.sleep(1)
    print("-------------------------------")
