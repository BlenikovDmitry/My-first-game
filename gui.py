from tkinter import *
from tkinter import ttk
import time
import records as rc

#обработчик кнопки ввода имени игрока
def start_game():
    player_name = ''
    # Получаем текст из поля ввода
    player_name = pname_entry.get()
    if player_name == '':
        pname_label_welcome.config(text=f'Привет, username и поехали')
    else:
        pname_label_welcome.config(text=f'Привет, {player_name[0:8]} и поехали')


def back():
    clear_window()
    init()
    

#обработчик окна рекордов
def show_records():
    clear_window()
    lbl_title = ttk.Label(master = window, text = 'Рекорды:', font=('Arial', 24, 'bold'))
    lbl_title.pack()
    # Создаем кнопку для получения текста из поля ввода имени игрока
    records_button = Button(master = window, width = 20, text="Вернуться на главный", command=back, font=('Arial', 18, 'bold'))
    records_button.pack(pady = 10)
        
def clear_window():
    # Удалить все объекты из окна
    for widget in window.slaves():
        widget.destroy()

def init():
    #надпись главного меню
    global lbl_title
    lbl_title = ttk.Label(master = window, text = 'Крестики - нолики', font=('Arial', 24, 'bold'))
    lbl_title.pack()

    global lbl_pname
    lbl_pname = ttk.Label(master = window, text = 'Имя игрока(не более 8 символов):', font=('Arial', 18, 'bold'))
    lbl_pname.pack()
    #поле ввода имени игрока
    global pname_entry
    pname_entry = ttk.Entry(master = window, width = 20, font = ('Arial', 18, 'bold'))
    pname_entry.pack(pady=10)

    global pname_label_welcome
    pname_label_welcome = ttk.Label(master = window, width = 50, font = ('Arial', 18, 'bold'))


    # Создаем кнопку для получения текста из поля ввода имени игрока
    global start_button
    start_button = Button(master = window, width = 20, text="Начать игру", command=start_game, font=('Arial', 18, 'bold'))
    start_button.pack(pady = 10)

    # Создаем кнопку для получения текста из поля ввода имени игрока
    global records_button
    records_button = Button(master = window, width = 20, text="Рекорды", command=show_records, font=('Arial', 18, 'bold'))
    records_button.pack(pady = 10)

    pname_label_welcome.pack(pady=10, padx = 70)
    
    

window = Tk()

window.title("Крестики - нолики")
window.geometry("500x500")
window.resizable(False, False)
#объявляем кнопки и метки для главного экрана(нужно при переходе с экрана на экран)
lbl_title = ''
lbl_pname = ''
pname_entry = ''
start_button = ''
records_button = ''
pname_label_welcome = ''
#вызываем отрисовку главного экрана
init()



window.mainloop()
