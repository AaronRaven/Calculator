# Honestly Tkinter asmeniskai patinka labiau negu saitu kurimas su Django ar Flask.
import tkinter as tk

# from turtle import color

# MATH!
calculation = ""


# prideda skaicius i kalkuliatoriu
def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    interface.delete(1.0, "end")
    interface.insert(1.0, calculation)


# naudoja eval metoda matematiniams veiksmams atilikti
# taip pat naudoja try/exept, kad error handlinti
def evaluate():
    global calculation
    try:
        calculation = str(eval(calculation))
        interface.delete(1.0, "end")
        interface.insert(1.0, calculation)
    except ZeroDivisionError:
        clear_field()
        interface.insert(1.0, "Equal to infinity.!")
    except ValueError:
        clear_field()
        interface.insert(1.0, "VALUE ERROR,INSERT NUMBAH!!!")


# Isvalo lauka
def clear_field():
    global calculation
    calculation = ""
    interface.delete(1.0, "end")


# The user interface
# Root originally was named perkele
root = tk.Tk()
root.maxsize(width=550, height=550)
root.minsize(width=260, height=265)
root.title("Python Calculator")
root.configure(bg='grey')

# The basic user interface. Rodo kas vyksta
interface = tk.Text(root, height=2, width=16, font=("Times New Roman", 24))
interface.grid(columnspan=6)

# Knopkes, kad ivesti skaiciu ir veiksmus, ka daryti. Spurdo kalba
yksi = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 14))
yksi.grid(row=2, column=1)

kaksi = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial", 14))
kaksi.grid(row=2, column=2)

kolme = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Helvetica", 14))
kolme.grid(row=2, column=3)

nelja = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial", 14))
nelja.grid(row=3, column=1)

viisi = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial", 14))
viisi.grid(row=3, column=2)

kuusi = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial", 14))
kuusi.grid(row=3, column=3)

seitseman = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial", 14))
seitseman.grid(row=4, column=1)

kahdeksan = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial", 14))
kahdeksan.grid(row=4, column=2)

yhdeksan = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial", 14))
yhdeksan.grid(row=4, column=3)

nolla = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial", 14))
nolla.grid(row=5, column=2)

# Veiksmu miktukai, Italiano
inserisci = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 14))
inserisci.grid(row=2, column=4)

sottrarre = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 14))
sottrarre.grid(row=3, column=4)

moltiplicare = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, font=("Arial", 14))
moltiplicare.grid(row=4, column=4)

divisione = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Arial", 14))
divisione.grid(row=5, column=4)

aprire = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Arial", 14))
aprire.grid(row=5, column=1)

chiusa = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Arial", 14))
chiusa.grid(row=5, column=3)

uguale = tk.Button(root, text="=", command=evaluate, width=5, font=("Arial", 14), fg='white',bg='green')
uguale.grid(row=6, column=4)

period = tk.Button(root, text=".", command=lambda: add_to_calculation("."), width=5, font=("Arial", 14),)
period.grid(row=6, column=2)


cancellare = tk.Button(root, text="C", command=clear_field, width=5, font=("Arial", 14), fg='red',
                       bg='lightgrey')
cancellare.grid(row=6, column=1)

percento = cancellare = tk.Button(root, text="%", command=lambda: add_to_calculation("%"), width=5, font=("Arial", 14),fg='medium spring green')
percento.grid(row=6, column=3)


root.mainloop()