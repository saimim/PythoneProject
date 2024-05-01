import customtkinter
from tkinter import *
from tkinter import messagebox
from datetime import date
from PIL import Image, ImageTk

app = customtkinter.CTk()
app.title('Cafe')
app.geometry("1000x400")
app.config(bg="#fafafa")
app.resizable(False, False)

font1 = ("Arial", 25, "bold")
font2 = ("Arial", 15, "bold")
font3 = ("Arial", 12, "bold")
price_list = [3, 5, 2]
total_price = 0

bill_frame = customtkinter.CTkFrame(app, width = 300, height=400, fg_color="#545457",corner_radius=0)
bill_frame.place(x=700, y=0)

menu_label = customtkinter.CTkLabel(app, text="DIU Cafe", font=font1, text_color="#2b1e1e", bg_color="#FFFFFF")
menu_label.place(x=230, y=5)

# Use PIL to open and convert images to GIF format
img1 = Image.open("dich5.jpg")
img1 = img1.convert("RGB")
img1 = ImageTk.PhotoImage(img1)

img2 = Image.open("dish2.jpg")
img2 = img2.convert("RGB")
img2 = ImageTk.PhotoImage(img2)

img3 = Image.open("dish3.jpg")
img3 = img3.convert("RGB")
img3 = ImageTk.PhotoImage(img3)

def pay():
    global total_price
    if(customer_entry.get() == ""):
        messagebox.showerror(title = "Error", message = "Please enter your name.")
    else:
        total_price = int(quntity1_combobox.get())*price_list[0]+int(quntity2_combobox.get())*price_list[1]+int(quntity3_combobox.get())*price_list[2]
        if(total_price ==0):
            messagebox.showwarning(title = "Error", message = "Please select some dishes.")
        else:
            name_label = customtkinter.CTkLabel(bill_frame, text = f"Customer Name: {customer_entry.get()}", font = font3, bg_color = "#fafafc", width = 320, anchor = W)
            name_label.place(x = 0, y = 100)
            price_label = customtkinter.CTkLabel(bill_frame, text = f"Total Price: {total_price} $", font = font3, bg_color = "#fafafc", width = 320, anchor = W)
            price_label.place(x = 0, y = 150)
            data_label = customtkinter.CTkLabel(bill_frame, text = f"Bill Date: {date.today()}",font = font3, bg_color = "#fafafc", width = 320, anchor = W)
            data_label.place(x = 0, y = 200)

def new():
    customer_entry.delete(0,END)
    quntity1_combobox.set(0)
    quntity2_combobox.set(0)
    quntity3_combobox.set(0)

def save():
    f = open(f"{customer_entry.get()} Bill" , "w")
    f.write(f"Customer Name: {customer_entry.get()}\n")
    f.write(f"Total price: {total_price} $\n")
    f.write(f"Bill Date: {date.today()}")
    messagebox.showinfo(title = "Saved", message = "Bill has been saved.")    

img1_label = customtkinter.CTkLabel(app, image=img1, text="Burger\nPrice: 3$", font=font2, text_color="#FFFFFF", fg_color="#090b17", width=100, height=100, corner_radius=20, compound=TOP, anchor=N)
img1_label.place(x=30, y=70)

img2_label = customtkinter.CTkLabel(app, image=img2, text="Pizza\nPrice: 5$", font=font2, text_color="#FFFFFF",fg_color="#090b17", width=100, height=100, corner_radius=20, compound=TOP,anchor=N)
img2_label.place(x=250, y=70)

img3_label = customtkinter.CTkLabel(app, image=img3, text="Seafood Pasta\nPrice: 2$", font=font2, text_color="#FFFFFF", fg_color="#090b17", width=100, height=100, corner_radius=20, compound=TOP, anchor=N)
img3_label.place(x=470, y=70)

quntity1_combobox = customtkinter.CTkComboBox(app,font=font3,text_color = "#000000",fg_color = "#FFFFFF", values = ("0","1","2","3"), state = "readonly")
quntity1_combobox.place(x = 23, y = 220)
quntity1_combobox.set(0)

quntity2_combobox = customtkinter.CTkComboBox(app,font=font3,text_color = "#000000",fg_color = "#FFFFFF", values = ("0","1","2","3"), state = "readonly")
quntity2_combobox.place(x = 250, y = 220)
quntity2_combobox.set(0)

quntity3_combobox = customtkinter.CTkComboBox(app,font=font3,text_color = "#000000",fg_color = "#FFFFFF", values = ("0","1","2","3"), state = "readonly")
quntity3_combobox.place(x = 470, y = 220)
quntity3_combobox.set(0)

customer_label = customtkinter.CTkLabel(app,text = "Customer Name:", font = font2, text_color = "#25283b",fg_color = "#FFFFFF")
customer_label.place(x = 40, y = 300)

customer_entry = customtkinter.CTkEntry(app,font = font2, fg_color = "#a19191", text_color = "#000000", border_color = "#FFFFFF", width = 200)
customer_entry.place(x = 200, y = 300)

pay_button = customtkinter.CTkButton(app,command = pay, text = "Pay Bill", font = font2, fg_color = "#ad0c78", hover_color = "ad0c78", corner_radius = 20, cursor = "hand2")
pay_button.place(x = 70, y = 350)

save_button = customtkinter.CTkRadioButton(app, command = save, text = "Save Bill", font = font2, fg_color = "#058007", hover_color = "#058007", corner_radius = 20, cursor = "hand2")
save_button.place(x = 250, y = 350)

new_button = customtkinter.CTkButton(app, command = new, text = "New Bill", font = font2, fg_color = "#c26406", hover_color = "#c26406", corner_radius = 20, cursor = "hand2")
new_button.place(x = 400, y =350)

app.mainloop()