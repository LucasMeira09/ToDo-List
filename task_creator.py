from tkinter import *
from customtkinter import *
from month import months

def create_tasks(date_task):

    root = CTk()
    root.geometry("550x400")
    root.title("Tasks creators") 
 
    #main_frame para melhor organisacao
    main_frame = CTkFrame(root, corner_radius=10)
    main_frame.pack(pady=10, padx=10)

    #aparencia escuro
    set_appearance_mode("dark")

    # dictionar para organisar todas as informacoes por data
    organisation_dictionary = {}
     # lista dos descriptione e note e lissat
    description_list = []
    note_list = []  
    task_list = [] 

    # funcao para adicionar as tarefas na lista
    def add_task():
        task = task_entry.get()
        description = description_entry.get()
        note = note_text.get(1.0, END)
        if task:
            list_box.insert(END, task)
            task_entry.delete(0,END)
        task_list.append(task)
        description_list.append(description)
        note_list.append(note)

        description_entry.delete(0,END)
        note_text.delete(1.0, END)
        
        # para por cada list dentro de um dicionario organisado por data - date_task, mas se for a mesma data vai adicionar os valores na mesma lista que ja esta atribuida a data
        organisation_dictionary.setdefault(date_task, []).append(task_list[-1])
        organisation_dictionary.setdefault(date_task, []).append(description_list[-1])
        organisation_dictionary.setdefault(date_task, []).append(note_list[-1])
        date_task_remplace = date_task+" task:"
        organisation_dictionary[date_task_remplace+str(len(task_list))] = organisation_dictionary.pop(date_task)
        print(organisation_dictionary)
        

    #funcao para selecionar um elemento na lista
    def select_function(event):
        try:
            index = list_box.curselection()[0]
            item = list_box.get(index)

            task_entry.delete(0, END)
            task_entry.insert(0, item)
        
            description_entry.delete(0, END)
            description_entry.insert(0, description_list[index])

            note_text.delete(1.0, END)
            note_text.insert(1.0, note_list[index])

            global selected_index
            selected_index = index

        except IndexError:
            pass

    # funcao para salvar as alteracoes
    def save_modifications():
        if selected_index != None:
            list_box.delete(selected_index)
            list_box.insert(selected_index, task_entry.get())
            task_entry.delete(0,END)
            description_list[selected_index] = description_entry.get()
            description_entry.delete(0,END)
            note_list[selected_index] = note_text.get(1.0, END)
            note_text.delete(1.0, END)

    # funcao para completar as tarefas
    def complete_task():
        list_box.delete(selected_index)
        description_list.pop(selected_index)
        note_list.pop(selected_index)

        task_entry.delete(0,END)
        description_entry.delete(0,END)
        note_text.delete(1.0, END)

    # funcao para limpar as entradas
    def clear():
        task_entry.delete(0,END)
        description_entry.delete(0,END)
        note_text.delete(1.0, END)

    task_frame = CTkFrame(main_frame,corner_radius=10,width= 500, height=225)
    task_frame.pack_propagate(False)
    task_frame.pack(pady=10, padx=5, fill=BOTH,expand=True)

    task_entry_frame = CTkFrame(task_frame, corner_radius=10)
    task_entry_frame.pack(pady=5, padx=10, fill=BOTH)

    # Label e Entry para entrada de tarefa
    task_label = CTkLabel(task_entry_frame, text="Task", font=("Arial", 10))
    task_label.pack(pady=5, padx=10, side=LEFT)  # Label no topo

    # Primeiro Entry para tarefa
    task_entry = CTkEntry(task_entry_frame)
    task_entry.pack(pady=5, padx=10, side=RIGHT, fill=BOTH, expand=True)

    #frame para organizar a descricao
    description_frame = CTkFrame(task_frame, corner_radius=10)
    description_frame.pack(pady=5, padx=5, fill=BOTH)

    # label e entry para descricao
    description_label = CTkLabel(description_frame, text="Description", font=("Arial", 10))
    description_label.pack(pady=5, padx=10, side=LEFT)

    # Segundo Entry para descrição, abaixo do primeiro
    description_entry = CTkEntry(description_frame, width=100)
    description_entry.pack(pady=5, padx=10, side=RIGHT, fill=BOTH, expand=True)

    # frame para organizar nota
    note_frame = CTkFrame(task_frame, corner_radius=10)
    note_frame.pack(pady=5, padx=5)
    # label nota
    note_label = CTkLabel(note_frame, text="Notes", font=("Arial", 10))
    note_label.pack(pady= 5, padx=10, side=LEFT)
    # text para nota
    note_text = Text(note_frame, width=100, height=5, font=("Arial", 10))
    note_text.pack(pady=5, padx=10, side=RIGHT)
    
    #Date frame
    date_frame = CTkFrame(task_frame, corner_radius=10)
    date_frame.pack(pady=5, padx=5, fill=BOTH, expand=True)
    #label para data
    date_label = CTkLabel(date_frame, text="Date", font=("Arial", 10))
    date_label.pack(pady=5, padx=10, side=LEFT)
    # date entrada
    day_label = CTkLabel(date_frame, text=date_task, font=("Arial", 10))
    day_label.pack(pady=5, padx=10)

    # frame para os butoes
    button_frame = CTkFrame(main_frame,corner_radius=10, width=500, height=40)
    button_frame.pack_propagate(False)
    button_frame.pack( pady=5, padx=5, fill=BOTH, expand=True)

    # botao para salvar tarefas
    save_button = CTkButton(button_frame, text="Save", font=("Arial", 10),corner_radius=10, command=save_modifications)
    save_button.pack(pady=5, padx=2, side=LEFT)

    # botao para completar as tarefas
    complete_task_button = CTkButton(button_frame, text="Complete Task", font=("Arial", 10),corner_radius=10 ,command=complete_task)
    complete_task_button.pack(pady=5, padx=2, side=LEFT)

    # botao para adicionar tarefa
    add_task_button = CTkButton(button_frame, text="Add Task", font=("Arial", 10),corner_radius=10, command=add_task)
    add_task_button.pack(pady=5, padx=2, side=RIGHT)

    #botao para limpar os entry
    clear_task_button = CTkButton(button_frame, text="Clean", font=("Arial", 10),corner_radius=10, command=clear)
    clear_task_button.pack(pady=5, padx=2, side=RIGHT)

    # frmae para a lista de tarefas
    list_frame = CTkFrame(main_frame,corner_radius=10, width= 500, height=150)
    list_frame.pack_propagate(False)
    list_frame.pack(pady=5, padx=5, fill=BOTH, expand=True)

    # lista com as tarefas
    list_box = Listbox(list_frame, width= 100)
    list_box.pack(pady=5, padx=10)

    # funcao para selecionar um elemento com mouse na lista
    list_box.bind("<<ListboxSelect>>", select_function)

    root.mainloop()
