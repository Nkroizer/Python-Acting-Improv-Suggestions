from acting_improv_suggestion_generator import generate_improv_suggestion, Actor
from tkinter import *
from tkinter import ttk

root = Tk()
main_actor = StringVar()
interactee = StringVar()
sex = IntVar()
main_actor_obj = Actor("", "")
interactees = []


def add_main_actor_name():
    main_actor_obj.name = main_actor.get()
    return True


def add_interactee():
    interactees.append(interactee.get())
    mylist.insert(END, interactee.get())
    mylist.pack(side=LEFT, fill=BOTH)
    scrollbar.config(command=mylist.yview)
    interactee.set("")
    return True


def generate():
    sex_var = sex.get()
    if sex_var == 1:
        main_actor_obj.pronoun = "He"
    else:
        main_actor_obj.pronoun = "She"
    print(generate_improv_suggestion(main_actor_obj, interactees))


frame = Frame(root)
frame.pack()
Label(frame, text="Name").grid(row=0, column=0)
e = Entry(
    frame,
    textvariable=main_actor,
    validate="focusout",
    validatecommand=add_main_actor_name,
)
e.grid(row=0, column=1)

frame4 = Frame(root)
frame4.pack()
Radiobutton(frame4, text="Male", variable=sex, value=1).pack(anchor=W)
Radiobutton(frame4, text="Female", variable=sex, value=2).pack(anchor=W)

# ------------------Frame 2------------------#
frame2 = Frame(root)
frame2.pack()
Label(frame2, text="Add Another Player").grid(row=0, column=0)
e = Entry(frame2, textvariable=interactee)
e.grid(row=0, column=1)
ttk.Button(frame2, text="Add Another", command=add_interactee).grid(row=1, column=0)


frame_interactees_list = Frame(root)
frame_interactees_list.pack()
scrollbar = Scrollbar(frame_interactees_list)
scrollbar.pack(side=RIGHT, fill=Y)
mylist = Listbox(frame_interactees_list, yscrollcommand=scrollbar.set)
# ------------------Frame 3------------------#
frame3 = Frame(root)
frame3.pack()
ttk.Button(frame3, text="Generate", command=generate).grid(row=1, column=0)


root.mainloop()
