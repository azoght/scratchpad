#firs_number = 2
#second_number = 20
#print (firs_number + second_number)


##### Definitions go here
# Addition
#def division():
    #first_number = 14
    #second_number =2
    #print(first_number / second_number)

#def multiply():
    #fn = 93.5
    #sn = 10.0
    #print (fn*sn)#


# Work goes here
#division()
#multiply()
dadname = raw_input("What is your dad's name?")
print("Your dad's name is" + dadname + "?")
print("Cool!")
year = int(raw_input("What year were you born in?"))
bornmonth = int(raw_input ("In which month?"))
currentyear = 2016
currentmonth = 6
ageInMonth = (currentyear-year)*12 + (currentmonth-bornmonth)
print("age is " + str(ageInMonth/12) + " years and " + str(ageInMonth%12) + " months")
