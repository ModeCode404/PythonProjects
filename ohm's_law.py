#Simple Ohm's law calculator script, made in python to help you understand Ohm's law better
#This calculator have 4 functions and works in terminal
#Made by ModeCode404 for the community!
print("What do you want to calculate?")
option=input("Vatts(V),Amps(A),Resistance(R) or Watts(W): ")
if option=="V" or option=="v": #Checking if input is "V/v" to calculate volts using Ohm's law
    a=float(input("Input the apmerage: "))
    r=float(input("Input the resistance: "))
    v=a*r
    w=v*a #Printing the watts for you so you dont lose time running the code again
    print(f"The voltage is {v} V")
    print(f"Which gives us {w} W")
elif option=="A" or option=="a": #Same for the Amps
    v=float(input("Input the voltage: "))
    r=float(input("Input the resistence: "))
    a=v/r
    w=v*a #Here also
    print(f"The amperage is {a} A")
    print(f"Which gives us {w} W")    
elif option=="R" or option=="r": #Here also for the resistance
    v=float(input("Input the voltage: "))
    a=float(input("Input the amperage: ")) 
    r=v/a
    print(f"The resistance is {r} ohm")
elif option=="W" or option=="w": #And here i added the Watts so you don't have to do it manually
    v=float(input("Input the voltage: "))
    a=float(input("Input the amperage: "))
    w=v*a #And ofc here
    print(f"The power is {w} W")    
else: #And here for the wrong inputs, for the ones who didn't read it propperly
    print("Invalid input!, input these 4 only.")   
#And thats it for this file 
#Working on updating and making new versions so stay tuned :) 
