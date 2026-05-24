def div(a, b):
    if b == 0:
        return 0
    else:
        return a / b

def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def times(a, b):
    return a * b

def eo(a):
    if a%2 == 1:
        result = f"{a} is odd"
        print(result)
        return result 
    else:
        result = f"{a} is even" 
        print(result)
        return result

def caculator(num1, num2, choice):
                                                                                                                                                                                                                                                                                                                                                                                                                                      
    print("enter a caculation 1,2,3")  
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Even or Odd")
    print("6. Add two numbers then multiply the result with first number")
    print("7. Multiply two numbers then subtract the result with second number")

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


#1.create the main window
#root = Tk()

#2.costomize the window(set title and size)
#root.title("calculator")
#root.geometry("500x500")


#root.mainloop()

def on_click(entry1, entry2, entry3, label):
    # Get the value from the Entry passed as parameter
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    choice = entry3.get()
    result = caculator(num1, num2, choice)
    label.config(text=f"The result is: {result}")


root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

label= ttk.Label(frm, text="Hello World!")
label.grid(column=0, row=0)
m1="enter a caculation 1,2,3\n"
m2="1. Add\n"
m3="2. Subtract\n"
m4="3. Multiply\n"
m5="4. Divide\n"
m6="5. Even or Odd\n"
m7="6. Add two numbers then multiply the result with first number\n"
m8="7. Multiply two numbers then subtract the result with second number\n"
menu=m1+m2+m3+m4+m5+m6+m7+m8
label2= ttk.Label(frm, text=f"{menu}")
label2.grid(column=0, row=3)

# First text box - first number
entry1 = ttk.Entry(frm, width=20)
entry1.grid(column=0, row=1, padx=5, pady=5)

# Second text box - second number
entry2 = ttk.Entry(frm, width=20)
entry2.grid(column=1, row=1, padx=5, pady=5)


# Choice text box
entry3 = ttk.Entry(frm, width=20)
entry3.grid(column=0, row=2, padx=5, pady=5)

label = ttk.Label(root, text="selecttion above!")
label.grid()  # or use .grid

ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
ttk.Button(frm, text="Calculate", command=lambda: on_click(entry1, entry2, entry3, label)).grid(column=1, row=2)
root.mainloop()

