'''
menu = {
    'Pizza' : 50,
    'Burger' : 100,
    'cola' : 60,
    'pasta' : 40,
    'nachos' : 55
}

Total_Bill = 0

print("Welcome to Harsh's Cafe ")
print("Select the item from our menu below")
print("Pizza : 50\n Burger : 100\n cola : 60\n pasta : 60\n nachos : 55")

item_1 = input("Enter the item you want to order : ")
if item_1 in menu:
    print(f"{item_1} has been added to your list")
    Total_Bill += menu[item_1]

else : 
    print(f"{item_1} is not available in our cafe")
    
another_order = input("Do you want to order something else (Yes/No) :  ")
if another_order == "Yes" :
    item_2 = input("Enter your second item :  ")
    if item_2 in menu :
        print(f"{item_2} is added in your list")
        Total_Bill += menu[item_2]
        
    else: 
        print(f"{item_2} is not available in our cafe")
        
else:
    print("Thank you for your order")
    
print(f"Your Total Bill is {Total_Bill}")

'''

import PySimpleGUI as sg

menu = {
    'Pizza' : 50,
    'Burger' : 100,
    'Cola' : 60,
    'Pasta' : 40,
    'Nachos' : 55
}

Total_Bill = 0

sg.theme('LightBlue1')

layout = [
    [sg.Text("Welcome to Harsh's Cafe")],
    [sg.Text("Select the item from our menu below")],
    [sg.Text("Pizza: 50\n    Burger: 100\n    Cola: 60\n    Pasta: 40\n    Nachos: 55")],
    [sg.Text("Enter the item you want to order: "), sg.InputText(key='-ITEM-')],
    [sg.Button('Order'), sg.Button('Exit')]
]

window = sg.Window('Cafe Order', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    elif event == 'Order':
        item = values['-ITEM-']
        if item in menu:
            sg.popup(f"{item} has been added to your list")
            Total_Bill += menu[item]
        else:
            sg.popup(f"{item} is not available in our cafe")
        another_order = sg.popup_yes_no("Do you want to order something else?")
        if another_order == 'No':
            break

window.close()

sg.popup(f"Thank you for your order. Your Total Bill is {Total_Bill}")
