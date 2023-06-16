"""
print("david is back")

print("*" * 10)


name = "Rotimi Shola"
age = 30
is_new = True


#INPUT FUNCTION

name = input("What is your name? ")
favourite_colour = input("What is your favourite colour? ")
print(name  + " likes " + favourite_colour)


name = input("what is your name? ")
school = input("what is the name of your school? ")
print(name + " attends " + school)

print("eden and mithelle are great people.")


name = input("what is your name?")
age = input("how old are your")
print(name + " is " + age + " Years old ")


name = input("what is your name? ")
age = input("how old are you?")
Class = input("what is the name of your class?")
School = input("what is the name of your school?")
Home_town = input("what is the name of your home town?")
Local_Government = input("what is the name of your local government?")
State_of_orgin = input("what is the name of your state of orgin?")
Home_Address = input("what is the name of your home_address?")
Email_Address = input("what is the of your email address?") 
print(name + " is a clever student")


#INDEXING

course = "Python new course"



name = "Umunna"
print(name[1:5])



first = "David"
last = "Umunna"
message = (f"{first} {last}  is a boy")
print(message)



name = "Wealth"
age = 20
message = (f"{name} is {age} years old")
print(message)



name = "Mary"
school = "Island Secondary School"
message = (f"{name} is in {school}")
print(message)



name = "John"
weight_lbs = input("What is your weight? ")
weight_kg = int(weight_lbs) * 0.45
message = (f"{name} weighs {weight_kg}kg")
print(message)



name = "David"
weight_lbs = input("what is your weight? ")
weight_kg = int(weight_lbs) * 0.45
message = (f"{name} weighs {weight_kg}kg")
print(message)



name = "Wealth"
school = "mafin school"
sport = "olymplic"
company = "og"
state = "island"
company_master = "d.e.o"
weight_lbs = input("what is your weight? ")
weight_kg = int(weight_lbs) * 0.45
message = (f"{name} weighs {weight_kg}kg in the {sport} of {company} in {state} from {company_master}. ")
print(message)



print(2+5)
print(5-2)
print(2*5)
print(9/3)
print(8//3)
print (5%2)
print(10**3)

print(25+2-4*5)
print(6*7/2**2)
print(7-3+3+3)



a = [1, 2, 3, 4,]
a [-1] = 20
b = a
print(b)
print(len(a))



course ="python new course"
print(course.upper())



name = "david"
weight_lbs = input("what is your weight? ")
weight_kg = int(weight_lbs) * 0.45
message =(f"{name} weighs {weight_kg}kg.")
print(message)



a ={'id':98, 'name':"Ade", 'project':[1,2,3,4]}
print(a.get('name'))



course = 'python new course'
print(course.replace('new','brandnew'))
print('python' in course)



x = 10
x = x + 3
print(x) 

x = 10
x = x - 3
print(x)

x = 10
x = x / 2
print(x)

x = 10
x = x*3
print(x)



course = 'davido'
print(course.replace('new','brandnew'))
print('david' in course)



is_hot = True
is_cold = False

if is_hot:
    print("it's a hot day")
    print("drink plenty of water")
elif is_cold:
    print("it's a cold day")
    print("wear warm clothes")
else:
    print("it's a lovelY day")
print("enjoy your day")



price = 1000000
has_good_credit = False

if has_good_credit:
    down_payment = 0.1 * price 
else:
    down_payment = 0.2 * price
print(f"Down Payment: ${down_payment}")



has_high_income = True
has_good_credit = False

if has_high_income and has_good_credit:
    print("eligible for loan")

else:
    print("Not Eligible for loan") 



has_high_income = False
has_good_credit = True

if has_high_income or has_good_credit:
    print("eligible for loan")

has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print("eligible for loan")



has_scored_more_than_250_in_jamb = True
has_scored_5_credit_in_waec = True

if scored_above_250_in_jamb and scored_5_credit_in_waec:
    print("eligible for addimssion")

else:
    print("Not Eligible For Addimssion")



has_the_worker_as_meet_annual_target = True
has_innovative_input_of_that_worker_in_the_comany = True

if has_the_worker_as_meet_annual_target or has_innovative_input_of_that_worker_in_the_comany:
        print("eligible for increment of salary")



temperature = 9

if temperature > 30:
    print("it's a hot day")
elif temperature < 10:
    print("it's a cold day")
else:
    print("it's neither hot nor cold")


temperature = int(input("Input number: "))

if temperature > 30:
    print("it's a hot day")
elif temperature < 10:
    print("it's a cold day")
else:
    print("it's neither hot nor cold")



admission_age = int(input("Input number: "))

if admission_age > 16:
    print("eligible for addimission")
elif admission_age < 16:
    print("not eligible for adimission")
else:
    print("eligible for addimission")    



work_time = int(input("input number: "))

if work_time > 9:
    print("not early to work")
elif work_time < 9:
    print(" early to work")
else:
    print("early to work")


admission_mark = int(input("input number: "))

if admission_mark > 240:
    print("eligible for adimission")
elif admission_mark < 240:
    print("not eligible for adimission")
else:
    print("eligible for adimission")   


fish = int(input("input number: "))

if fish > 30:
    print("eligible for sale")
elif fish < 30:
    print("not eligible for sale")
else:
    print("eligiblr for sale")      


meat = int(input("input number:"))

if meat > 10:
    print("eligible for sale")
elif meat < 10:
    print("not eligible for sale")
else:
    print("eligible for sale")
"""            

"""
Auth: David
"""
name = "David"
weight_lbs = input("what is your weight? ")
weight_kg = int(weight_lbs) * 0.45
message =(f"{name} weighs {weight_kg}kg.")
print(message) 