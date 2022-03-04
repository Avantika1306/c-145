from tkinter import *
root=Tk()
root.title("Driving License")
root.geometry("500x500")
root.configure(bg="white")
canvas=Canvas(root,width=400,height=250)
canvas.create_image(0,0,anchor=NW)
canvas.create_rectangle(0, 0, 400, 45, fill="#F6091E")


label_heading = canvas.create_text(200,20, font=('Times', '24', 'bold italic') ,text="Driving License", fill = "white")
label_id_tag = canvas.create_text(25,60, font=('Times', '14', 'bold') ,text="ID :")
label_name_tag = canvas.create_text(30,100, font=('Times', '12', 'bold') ,text="Name :")
label_dob_tag = canvas.create_text(52,120, font=('Times', '12', 'bold') ,text="Date of birth :")
label_pin_tag = canvas.create_text(32,140, font=('Times', '12', 'bold') ,text="Pin no. :")
label_address_tag = canvas.create_text(36,160, font=('Times', '12', 'bold') ,text="Address :")
label_vehicle_type_tag = canvas.create_text(155,180, font=('Times', '12', 'bold') ,text="Authorisation to drive the following vehicles :")

label_id=Label(root)
label_name=Label(root)
label_address=Label(root)
label_dob=Label(root)
label_pin=Label(root)
label_vehicle_type=Label(root)


def showdrivinglicense():
    id=6013
    print(type(id))
    name="avantika khanna"
    print(type(name))
    address="mangal disha 601"
    print(type(address))
    DOB="13/06/10"
    
    print(type(DOB))
    pin=400052
    print(type(pin))
    Vehicle_Type=["two wheeler","four wheeler"]
    print(type(Vehicle_Type))
    label_id["text"]=id
    label_name["text"]=name
    label_address["text"]=address
    label_dob["text"]=DOB
    label_pin["text"]=pin
    label_vehicle_type["text"]=Vehicle_Type

button1=Button(root,text="show my driving license", command=showdrivinglicense)
button1.configure(width = 20 , activebackground = "#9EC6EE", relief= FLAT)
button1_window = canvas.create_window(200, 235, anchor=CENTER, window=button1)
label_id_window = canvas.create_window(80, 60, anchor=CENTER, window=label_id)
label_name_window = canvas.create_window(100, 100, anchor=CENTER, window=label_name)
label_dob_window = canvas.create_window(140, 120, anchor=CENTER, window=label_dob)
label_pin_window = canvas.create_window(85, 140, anchor=CENTER, window=label_pin)
label_address_window = canvas.create_window(130, 160, anchor=CENTER, window=label_address)
label_vehicle_type_window = canvas.create_window(335, 180, anchor=CENTER, window=label_vehicle_type)
canvas.pack()
root.mainloop()