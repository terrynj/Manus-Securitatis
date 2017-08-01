print("Hello and welcome to manus securitatis.")
Names=[]
#Displays a welcome message.
#Registration
g=open("Lengths.txt","a")
Username=input("Please enter your username.")
Names.append(Username)
Length1=float(input("Enter value one."))
Length2=float(input("Enter value two."))
Length3=float(input("Enter value three."))
Length4=float(input("Enter value four."))
Length5=float(input("Enter value five."))
#Asks for the user to enter the length of each finger.
g.write(Username)
g.write("\n")
g.write(Length1)
g.write("\n")
g.write(Length2)
g.write("\n")
g.write(Length3)
g.write("\n")
g.write(Length4)
g.write("\n")
g.write(Length5)
g.write("\n")
g.close()
#Writes to the file.
#Authentication
