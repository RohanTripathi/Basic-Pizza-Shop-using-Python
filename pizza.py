import pymysql
from tkinter import *
from time import strftime
from tkinter import messagebox
from PIL import ImageTk, Image



window = Tk()
window.configure(background='red')
window.geometry("1000x700")
window.wm_title("Pizza Shop")

img = ImageTk.PhotoImage(Image.open("pizza.png"))
panel = Label(window, image = img,bg='light blue',height=120,width=200)
panel.place(x=10, y=10)


global total_p


pizza_var = 0
Largepizza_var = 0
cheesepizza_var = 0
nonvegpizza_var = 0
deluxeveggie_var= 0


total_p=0
p1=145
p2=170
p3=160              
p4=165
p5=180

#The time function
def time():

    string1 = strftime('%H:%M:%S %p')
    lbl.config(text = string1)
    lbl.after(1000, time)

lbl = Label(window, font = ('calibri', 20, 'bold'),background = 'blue',foreground = 'white')

lbl.place(x=350,y=80)

time()

def create_window():

    new_window = Toplevel(window)
    new_window.configure(background='light blue')

    customer_name=Label(new_window,font=15,text="Customer Name:  "+ str (e_name.get())).pack()
    customer_phone=Label(new_window,font=15,text="Customer Phone:  "+str (e_phone.get())).pack()
    tp=Label(new_window,font=15,text="Total Price:  "+ str(total_p)).pack()
    
    confirm=Button(new_window,text="Done",bg="green",fg="white",command=new_window.destroy,height=2,width=10).pack()
    new_window.geometry("500x150")




#headind

pizza_shop=Label(window,bg="light blue", text = 'Pizza Shop', font =('Verdana', 30))
pizza_shop.pack(side = TOP, pady = 10)

def quantity_1():
    global pizza_var

    pizza_var += 1
    e1['text'] = "Quantity: " + str(pizza_var )

def quantity_2():
    global Largepizza_var

    Largepizza_var += 1
    e2['text'] = "Quantity: " + str(Largepizza_var)

def quantity_3():
    global cheesepizza_var

    cheesepizza_var += 1
    e3['text'] = "Quantity: " + str(cheesepizza_var)

def quantity_4():
    global nonvegpizza_var

    nonvegpizza_var += 1
    e4['text'] = "Quantity: " + str(nonvegpizza_var)

def quantity_5():
    global deluxeveggie_var

    deluxeveggie_var += 1
    e5['text'] = "Quantity: " + str(deluxeveggie_var)       

def total_price():
    global total_p
    global p1
    global p2
    global p3
    global p4
    global p5
    p1=(p1*pizza_var)
    p2=(p2*Largepizza_var)
    p3=(p3*cheesepizza_var)
    p4=(p4*nonvegpizza_var)
    p5=(p5*deluxeveggie_var)
    total_p=(p1+p2+p3+p4+p5)
    etotal['text'] = "Total: " + str(total_p)
   

def insert():
    global total_p
    con=pymysql.connect(host="localhost",user="root",password="",database="pizza")
    cursor=con.cursor()

    cursor.execute('INSERT INTO `order1` VALUES (%s,%s,%s)', (e_name.get(),e_phone.get(),e_tol.get()))

    sucess=Label(text="Data Inserted Into the Database Successfully!",bg='light green')
    sucess.place(x=650,y=125)

    con.commit()
# Creating a photoimage object to use image
photo1 = PhotoImage(file = r"veg_pizza.png")
photo2 = PhotoImage(file = r"Large_pizza.png")
photo3 = PhotoImage(file = r"cheese_pizza.png")
photo4 = PhotoImage(file = r"non_pizza.png")
photo5 = PhotoImage(file = r"deluxe_veggie.png")
#Pizza images


veg_pizza_b1=Button(window,bg="light blue",image = photo1,height=180,width=200,bd=4,command=quantity_1,activeforeground = "blue",activebackground = "green",border="0")
veg_pizza_b1.place(x=10,y=150)

Large_pizza_b2=Button(window,bg="light blue", image = photo2,height=180,width=200,bd=4,command=quantity_2,activeforeground = "blue",activebackground = "blue",border="0")
Large_pizza_b2.place(x=400,y=150)

cheese_pizza_b3=Button(window,bg="light blue", image = photo3,height=180,width=200,bd=4,command=quantity_3,activeforeground = "blue",activebackground = "red",border="0")
cheese_pizza_b3.place(x=10,y=380)

non_pizza_b4=Button(window,bg="light blue", image = photo4,height=180,width=200,bd=4,command=quantity_4,activeforeground = "blue",activebackground = "yellow",border="0")
non_pizza_b4.place(x=400,y=380)

deluxe_veggie_b5=Button(window,bg="light blue", image = photo5,height=180,width=200,bd=4,command=quantity_5,activeforeground ="blue",activebackground ="green",border="0")
deluxe_veggie_b5.place(x=780,y=150)
#total Button
b_order=Button(window, text="Order",bg="blue",height=3,width=12,command=create_window,fg="white")
b_order.place(x=500,y=600)
b_close=Button(window, text="Close",height=3,width=12,command=window.destroy,bg="blue",fg="white")
b_close.place(x=650,y=600)
b_total=Button(window, text="Total",height=4,width=10,command=total_price,bg="blue",fg="white")
b_total.place(x=150,y=600)

#total amount displayed
etotal=Label(window,width=20,height=4)
etotal.place(x=270,y=600)


# Creating entries

e1=Label(window,width=15)
e1.place(x=230,y=210,height=50)

l1=Label(window,text="Price: 145",bg="yellow")
l1.place(x=270,y=280)

l2=Label(window,text="Veg Pizza",bg="yellow")
l2.place(x=270,y=310)

e2=Label(window,width=15)
e2.place(x=620,y=210,height=50)

l3=Label(window,text="Price: 170",bg="yellow")
l3.place(x=630,y=280)

l4=Label(window,text="Large Pizza",bg="yellow")
l4.place(x=630,y=310)

e3=Label(window,width=15)
e3.place(x=230,y=430,height=50)

l5=Label(window,text="Price: 160",bg="yellow")
l5.place(x=270,y=500)

l6=Label(window,text="cheese Pizza",bg="yellow")
l6.place(x=270,y=530)

e4=Label(window,width=15)
e4.place(x=620,y=430,height=50)

l7=Label(window,text="Price: 165",bg="yellow")
l7.place(x=630,y=500)

l8=Label(window,text="Non-Veg Pizza",bg="yellow")
l8.place(x=630,y=530)

e5=Label(window,width=15)
e5.place(x=820,y=350,height=50)

l9=Label(window,text="Price: 180",bg="yellow")
l9.place(x=820,y=410)

l10=Label(window,text="Deluxe veggie",bg="yellow")
l10.place(x=820,y=440)
#insert function

name=Label(window,text="Name:")
name.place(x=650,y=10)

e_name=Entry(window)
e_name.place(x=700,y=10)

phone=Label(window,text="Phone:")
phone.place(x=650,y=40)

e_phone=Entry(window)
e_phone.place(x=700,y=40)

total=Label(window,text="Total:")
total.place(x=650,y=70)

e_tol=Entry(window)
e_tol.place(x=700,y=70)

b_insert=Button(window,text="Submit",command=insert)
b_insert.place(x=720,y=95)

mainloop()
