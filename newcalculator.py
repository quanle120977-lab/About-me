def div(a, b):
    if b == 0:
        return 0
    else:
        return a / b

#def sum(a, b):
    return a + b

#def sub(a, b):
    return a - b

#def times(a, b):
    return a * b

#def eo(a):
    if a%2 == 1:
        result = f"{a} is odd"
        print(result)
        return result 
    else:
        result = f"{a} is even" 
        print(result)
        return result

def caculator(num1, num2, choice):
                                                                                                                                                                                                                                                                                                                                                                                                                                      
    #print("enter a caculation 1,2,3")  
    #print("1. Add")
    #print("2. Subtract")
    #print("3. Multiply")
    #print("4. Divide")
    #print("5. Even or Odd")
    #print("6. Add two numbers then multiply the result with first number")
    #print("7. Multiply two numbers then subtract the result with second number")

    #choice = input("Enter choice(1/2/3/4/5/6/7): ")

    if choice in ['1', '2', '3', '4', '5','6','7']:
        #num1 = float(input("Enter first number: "))
        #num2 = float(input("Enter second number: "))
        
        if choice == '1':
            result = sum(num1, num2)
            print(f"Result: {result}")
            return result
        elif choice == '2':
            result = sub(num1, num2)
            print(f"Result: {result}")
            return result
        elif choice == '3':
            result = times(num1, num2)
            print(f"Result: {result}")
            return result
        elif choice == '4':
            result = div(num1, num2)
            print(f"Result: {result}")
            return result
        elif choice == '5':
            result1 = eo(num1)
            result2 = eo(num2)
            return result1 +" " +result2
        elif choice == '6':
            s=sum(num1, num2)
            result=times(s, num1)
            print(f"result is {result}")
            return result
        elif choice =='7':
            t=times(num1,num2)
            result=sub(t,num2)
            print(f"result is {result}")
            return result

    else:
        print(f"sorry bruhv still under construction {choice}")
        return None
                
#caculator()
from tkinter import*
from tkinter import ttk

#root.title("calculator")
#root.geometry("500x500")


root = Tk()

frm = Frame(root)

("display = Entry(frm")


def button_click(char):
    current = display.get() # Get what's already there
    display.delete(0, END)  # Clear the box
    display.insert(0, current + str(char)) # Put it back with the new number

def calculate():
    try:
        # eval() takes the text like "1+2" and does the math
        result = eval(display.get())
        display.delete(0, END)
        display.insert(0, str(result))
    except:
        display.delete(0, END)
        display.insert(0, "Error")


def clear():
    display.delete(0, END)

for i in range(4):
    frm.columnconfigure(i, weight=1)
for i in range(1, 6):
    frm.rowconfigure(i, weight=1)

    
root = Tk()
root.title = ("calculator")
root.geometry("750x750")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frm.grid(sticky="nsew")

for i in range(4):
    frm.columnconfigure(i, weight=1)


root.resizable(True, True)

frm = Frame(root,bg="#465263", padx=10, pady=10)
frm.grid()

# Variables
num1 = 0
num2 = 0

def set_num(num):
    global num1
    num1 = num


display = Entry(frm, font=('Arial', 24), borderwidth=5, relief="flat", justify='right')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")


# The list of buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+',
    '(',')',]
row_idx = 1
col_idx = 0


for char in buttons:
    # 1. Define what happens for specific buttons
    if char == '=':
        action = calculate 
    elif char == 'C':
        action = clear 
    else:
        
        action = lambda x=char: button_click(x)

    Button(frm, text=char, width=5, height=2, font=('Arial', 18), command=action).grid(
        row=row_idx, column=col_idx, padx=5, pady=5)

    col_idx += 1
    if col_idx > 3:
        col_idx = 0
        row_idx += 1

root.mainloop() 


