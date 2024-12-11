from tkinter import ttk
import tkinter as tk 
import random
from PIL import Image, ImageTk #bo photoImage nie oferuje zmiany rozmiaru 


def slot_value():
    #losowanie obraka 
    slot_value = random.choice(slot_images)
    return slot_value

def spin(): 
    for i in range(3):
       slot_labels[i].config(image=slot_value())
        
    # Sprawdzanie, czy wszystkie obrazki są takie same - jesli tak to zwracamy komunikat o wygranej 
    if slot_labels[0].cget('image') == slot_labels[1].cget('image') == slot_labels[2].cget('image'):
        result_label.config(text="Gratuluje poprawiasz ten przedmtiot! Lepiej zacznij się uczyć!", foreground="green")

    else: 
       result_label.config(text="Spróbuj ponownie", foreground="red")


#GUI
root =tk.Tk()
root.title("slots!")
root.configure(bg='mintcream')

label = tk.Label(root, text="Zakreć jaki przedmiot będziesz poprawiał!",font=("Arial", 16), background="mintcream", fg="black")
label.grid(row=0, column=0, columnspan=3, pady=10)

slots_frame= tk.Frame(master=root, height=200, width=400, bg='mintcream')
slots_frame.grid(row=1, column=0, columnspan=3)


#pobieranie i dostosowywanie obrazków
slots_elements = ["Zestaw10/algebra.png", "Zestaw10/logika.png", "Zestaw10/metody.png", "Zestaw10/java.png", "Zestaw10/analiza.png"]
slot_images = []
for image_path in slots_elements:
    image = Image.open(image_path)
    image = image.resize((150,50))
    slot_images.append(ImageTk.PhotoImage(image)) 

slot_labels=[]
for _ in range(3):
    slot_label = ttk.Label(master=slots_frame, image=None,  width=10, anchor="center")
    slot_label.pack(side="left", padx=10)
    slot_labels.append(slot_label)


#wyniki
result_label = tk.Label(master=root, text="", font=("Arial", 14), background="mintcream")
result_label.grid(row=2, column=0, columnspan=3, pady=5)

#przycisk do krecenia 
button_frame = tk.Frame(master=root, width=100, height=100)
button_frame.grid(row=3, column=0, columnspan=3, pady=5)
button = tk.Button(button_frame, text="spin", width=10, height=2, command=spin)
button.grid()



root.mainloop()






