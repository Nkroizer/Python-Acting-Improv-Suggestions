from acting_improv_suggestion_generator import generate_improv_suggestion, Actor
from tkinter import *
from tkinter import ttk, messagebox

root = Tk()
root.geometry("500x500")
main_actor = StringVar()
interactee = StringVar()
sex = IntVar()
main_actor_obj = Actor("", "")
interactees = []


def on_click():
    messagebox.showerror("Missing Info Error", "Make Sure that you fill all fields")


def add_main_actor_name():
    main_actor_obj.name = main_actor.get()
    return True


def add_interactee():
    interactees.append(interactee.get())
    other_actors_list.insert(END, interactee.get())
    other_actors_list.pack(side=LEFT, fill=BOTH)
    scrollbar.config(command=other_actors_list.yview)
    interactee.set("")
    return True


def generate():
    sex_var = sex.get()
    if sex_var == 1:
        main_actor_obj.pronoun = "He"
    else:
        main_actor_obj.pronoun = "She"

    if (
        main_actor_obj.name == ""
        or main_actor_obj.pronoun == ""
        or len(interactees) < 1
    ):
        on_click()
    print(generate_improv_suggestion(main_actor_obj, interactees))


# ------------------Frame main actor------------------#
frame_main_actor = Frame(root, background="lightgreen", padx=10, pady=10)
frame_main_actor.pack()
Label(frame_main_actor, text="Name", width=15).grid(row=0, column=0)
e = Entry(
    frame_main_actor,
    textvariable=main_actor,
    validate="focusout",
    validatecommand=add_main_actor_name,
)
e.grid(row=0, column=1)

# ------------------Frame sex------------------#
frame_sex = Frame(root, background="lightgreen", padx=10, pady=10)
frame_sex.pack()
Radiobutton(frame_sex, text="Male", width=15, variable=sex, value=1).pack(anchor=W)
Radiobutton(frame_sex, text="Female", width=15, variable=sex, value=2).pack(anchor=W)

# ------------------Frame other actors------------------#
frame_other_actors = Frame(root, background="lightgreen", padx=10, pady=10)
frame_other_actors.pack()
Label(frame_other_actors, text="Add Another Player", width=15).grid(row=0, column=0)
e = Entry(frame_other_actors, textvariable=interactee, width=15)
e.grid(row=0, column=1)
ttk.Button(
    frame_other_actors, text="Add Another", width=15, command=add_interactee
).grid(row=1, column=0)

# ------------------Frame interactees_list------------------#
frame_interactees_list = Frame(root, background="lightgreen", padx=10, pady=10)
frame_interactees_list.pack()
scrollbar = Scrollbar(frame_interactees_list)
scrollbar.pack(side=RIGHT, fill=Y)
other_actors_list = Listbox(frame_interactees_list, yscrollcommand=scrollbar.set)

# ------------------Frame generate------------------#
frame_generate = Frame(root, background="lightgreen", padx=10, pady=10)
frame_generate.pack()
ttk.Button(frame_generate, text="Generate", width=15, command=generate).grid(
    row=1, column=0
)

root.mainloop()
