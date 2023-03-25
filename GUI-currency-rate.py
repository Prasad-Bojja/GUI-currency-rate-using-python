import tkinter as tk
from forex_python.converter import CurrencyRates
import datetime
from tkinter import*
import tkinter as tk
from PIL import ImageTk,Image
# Create a new root
root = tk.Tk()
# Set the title of the root
root.title("Currency Converter")
root.configure(bg='white')
root.geometry('900x900')
img= ImageTk.PhotoImage(Image.open("currency1.png"))
Ibi=tk.Label(root,image=img).pack()
hd=Label(root,text='Currency Converter', font='sans 14', bg='yellow', fg='blue').pack(fill='both')

# Create a label widget
label1 = tk.Label(root, font='sans 12',text="Enter amount in INR:")
label2 = tk.Label(root, font='sans 12',text="Select target currency:")
label3 = tk.Label(root, font='sans 12',text="Converted amount:")

# Create an entry widget to accept user input for source currency amount
entry1 = tk.Entry(root)

# Create a drop-down menu to select target currency
options = ['USD','CNY','AUD','NZD','GBP','BTC','ETH','EUR','JPY']
var = tk.StringVar()
var.set(options[0])
option_menu = tk.OptionMenu(root, var, *options)

# Create a label widget to display the converted amount
label4 = tk.Label(root,font='sans 16', text="")

# Add the widgets to the root
label1.pack()
entry1.pack()
label2.pack()
option_menu.pack()
label3.pack()
label4.pack()

# Define a function to convert the currency and update the label
def convert_currency():
    amount = float(entry1.get())
    target_currency = var.get()
    converted_amount = c.convert('INR', target_currency, amount, dt)
    label4.config(text=str(converted_amount) + ' ' + target_currency + 's')

# Create a button widget to trigger the conversion
button = tk.Button(root, text="Convert", command=convert_currency)
button.pack()

# Create an instance of the CurrencyRates class and specify the date
c = CurrencyRates()
dt = datetime.datetime(2023, 3, 20)

# Run the event loop

root.mainloop()
