from tkcalendar import Calendar
from datetime import datetime
from tkinter import *

def months(main_frame):

    date_calendar = StringVar()
    # Callback para obter a data selecionada no calendário
    def get_date_calender(event=None):
        date_calendar.set(calendar.get_date())
    # Obtém a data atual
    current_date = datetime.now()

    # Adiciona o calendário à janela
    calendar = Calendar(
        main_frame,
        selectmode='day',
        year=current_date.year,
        month=current_date.month,
        day=current_date.day,
        font=("Arial", 18),
        date_pattern="dd/mm/yyyy",
    )
    calendar.pack(pady=20, fill=BOTH)

    # Vincula o evento de seleção do calendário
    calendar.bind("<<CalendarSelected>>", get_date_calender)

    # Exibe a data inicial no terminal
    print(f"Data inicial: {calendar.get_date()}")

    # Retorna o widget do calendário (se necessário)
    return date_calendar