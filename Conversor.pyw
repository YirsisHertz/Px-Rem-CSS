from tkinter import *

def main(px):

    if px == '':
        return str(0)

    return str(  float( float(px) / 16 ))

def ui():

    root = Tk()

    root.geometry("300x210")
    root.title("Conversor PX a REM")
    root.resizable(0, 0)
    root.config( bg="#333" )

    lb = Label(root, bg="#333").pack()

    label1 = Label(root, text="Valor PX: ")
    label1.config(justify=CENTER, font="Montserrat-bold 15", bg="#333", fg="snow" )
    label1.pack()

    text_px = Entry(root)
    text_px.config( justify=CENTER, font="Montserrat 15" )
    text_px.pack()

    label2 = Label(root, text="Valor REM: ")
    label2.config(justify=CENTER, font="Montserrat-bold 15", bg="#333", fg="snow" )
    label2.pack()
    text_rem = Entry(root)
    text_rem.config(justify=CENTER, font="Montserrat 15" )
    text_rem.pack()


    lb = Label(root, bg="#333").pack()

    def convert():
        text_rem.delete(0, END)
        text_rem.insert(0, main(text_px.get()))

    boton_convertir = Button(
            root, 
            text="Convertir", 
            justify=CENTER, 
            font="Montserrati-bold 15", 
            bg="#888", 
            fg="snow", 
            activebackground="#666", 
            activeforeground="snow", 
            highlightcolor="#777",
            command=lambda:convert()
            )
    boton_convertir.pack()

    root.mainloop()



if __name__ == "__main__":

    ui()

