from tkinter import *
from task_creator import *
from month import *
from customtkinter import *

root = CTk()
root.geometry("800x500")
root.title("CheckTasks")

set_appearance_mode("dark")

# main frame pour tout les widgets
main_frame = CTkFrame(root, width=700)
main_frame.pack(pady=50, padx=50)

#titulo da apps
title_label = CTkLabel(main_frame, text="CheckTasks", font=("Arial", 20))
title_label.pack(pady=10, padx=10, fill=BOTH)

# frame para  os botoes para ir no criador de tarefas
button_frame = CTkFrame(main_frame, height=70,corner_radius=10 )
button_frame.pack_propagate(False)
button_frame.pack(pady=10, padx=10, fill=BOTH)

date_task = months(main_frame)
# botao para ir ao criador de tarefas
button_create_task = CTkButton(button_frame, text="Create Task", font=("Arial",16), corner_radius=10, command=lambda: create_tasks(date_task.get()))
button_create_task.pack(pady=10, padx=10, side=RIGHT, fill=BOTH, expand=True)

button_view_task = CTkButton(button_frame, text="View Task", font=("Arial",16), corner_radius=10)
button_view_task.pack(pady=10, padx=10, side=RIGHT, fill=BOTH, expand=True)

months(main_frame)

root.mainloop()
