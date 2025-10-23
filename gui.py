from tkinter import *
from tkinter import ttk
import tkinter as tk

#обработчик кнопки ввода имени игрока
def start_game():
    player_name = ''
    # Получаем текст из поля ввода
    player_name = pname_entry.get()
    if player_name == '':
        pname_label_welcome.config(text=f'Привет, username и поехали')
        player_name = 'username'
        main_game_screen(player_name)
    else:
        pname_label_welcome.config(text=f'Привет, {player_name[0:8]} и поехали')
        main_game_screen(player_name)

'''
далее прямо тут вызываем интерфейс игры и функции игрового движка(движок вынесем в отдельный файл engine.py)
только не забудь объявить переменные интерфейса в основном блоке программы
'''
def main_game_screen(player_name):
    clear_window()
    counter_steps = 0
    elapsed_time = 0
    player_name_lbl_dec = tk.Label(master = window, text = 'Имя игрока:', font=('Arial', 12, 'bold'), bg='#FFDAB9')
    player_name_lbl_dec.pack(pady = 5)
    player_name_lbl_main = tk.Label(master = window, text = player_name, font=('Arial', 12, 'bold'), bg='#FFDAB9')
    player_name_lbl_main.pack(pady = 5)
    count_steps_dec = tk.Label(master = window, text = 'Сделано ходов', font=('Arial', 12, 'bold'), bg='#FFDAB9')
    count_steps_dec.pack(pady = 5)
    count_steps_main =  tk.Label(master = window, text = str(counter_steps), font=('Arial', 12, 'bold'), bg='#FFDAB9')
    count_steps_main.pack(pady = 5)
    elapsed_time_dec = tk.Label(master = window, text = 'Прошло времени', font=('Arial', 12, 'bold'), bg='#FFDAB9')
    elapsed_time_dec.pack(pady = 5)
    elapsed_time_main = tk.Label(master = window, text = str(elapsed_time), font=('Arial', 12, 'bold'), bg='#FFDAB9')
    elapsed_time_main.pack(pady = 5)
    button_help = Button(master = window, width = 20, text="Помощь", font=('Arial', 18, 'bold'))
    button_help.pack(pady = 5)
    button_exit = Button(master = window, width = 20, text="Выход", command=back, font=('Arial', 18, 'bold'))
    button_exit.pack(pady = 5)

def back():
    clear_window()
    init()
    

#обработчик окна рекордов
def show_records():
    clear_window()
    lbl_title = tk.Label(master = window, text = 'Рекорды:', font=('Arial', 24, 'bold'), bg='#FFDAB9')
    lbl_title.pack()

    text_widget = tk.Text(window,bg='#EEE8AA',font=('Arial', 10, 'bold'))

    f = open('records.txt', encoding = 'utf-8')
    for line in f:
        text_widget.insert('end',line)

    f.close()
    text_widget.pack()
    text_widget.configure(state="disabled")
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
    lbl_title = tk.Label(master = window, text = 'Крестики - нолики', font=('Arial', 24, 'bold'),bg='#FFDAB9')
    lbl_title.pack()

    global lbl_pname
    lbl_pname = tk.Label(master = window, text = 'Имя игрока(не более 8 символов):', font=('Arial', 18, 'bold'),bg='#FFDAB9')
    lbl_pname.pack()
    #поле ввода имени игрока
    global pname_entry
    pname_entry = ttk.Entry(master = window, width = 20, font = ('Arial', 18, 'bold'))
    pname_entry.pack(pady=10)

    global pname_label_welcome
    pname_label_welcome = tk.Label(master = window, width = 50, font = ('Arial', 18, 'bold'),bg='#FFDAB9')


    # Создаем кнопку для получения текста из поля ввода имени игрока
    global start_button
    start_button = Button(master = window, width = 20, text="Начать игру", command=start_game, font=('Arial', 18, 'bold'))
    start_button.pack(pady = 10)

    # Создаем кнопку для вызова экрана рекордов
    global records_button
    records_button = Button(master = window, width = 20, text="Рекорды", command=show_records, font=('Arial', 18, 'bold'))
    records_button.pack(pady = 10)

    pname_label_welcome.pack(pady=10, padx = 70)
    
    

window = Tk()

window.title("Крестики - нолики")
window.geometry("500x700")
window.resizable(False, False)
window.config(bg='#FFDAB9')
#объявляем кнопки и метки для главного экрана(нужно при переходе с экрана на экран)
lbl_title = ''
lbl_pname = ''
pname_entry = ''
start_button = ''
records_button = ''
pname_label_welcome = ''
#вызываем отрисовку главного экрана
init()

#объявляем элементы интерфейса для экрана игры
player_name_lbl_dec = ''
player_name_lbl_main = ''
count_steps_dec = ''
count_steps_main = ''
elapsed_time_dec = ''
elapsed_time_dec = ''
button_help = ''
button_exit = ''




window.mainloop()
