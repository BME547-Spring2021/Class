### Python Basics:
##Personal info
##written by arlette geller

### Intro

first_name=input("enter your name: ")
print("your name is " + first_name)

#my_age=input("enter your age: ")
#print("your age is "+ my_age)
#input dunction return string
#cannot add string + number
#next_year=my_age+1
#convert string to int
my_age=input("enter your age: ")
my_age=int(my_age)
#next_year=my_age+1
#print("your age next year will be "+next_year)
#not working
#prefered format for python
#Using a format place holder
next_year=my_age+1
print("your age is {} ".format(my_age))
print("your age next year will be {}".format(next_year))

## If statements and Code Blocks
if my_age <18:
   print("You are a minor.")
   print("get your parents permission") 
elif my_age>=65:
    print("you are a senior.")
elif my_age==21:
    print("you are turning 21")
else:
    print("You are an adult.")
print("done")