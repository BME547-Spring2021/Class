### Functions
def input_info() :
    first_name=input("enter your name: ")
    print("your name is " + first_name)

    my_age=input("enter your age: ")
    my_age=int(my_age)
    print("your age is {} ".format(my_age))
    return my_age

def age_next_year(current_age) :
    next_year=current_age+1
    print("your age next year will be {}".format(next_year))
    
def age_classification(my_age) :
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

print("Running program...")
age=input_info()
age_next_year(age)
age_classification(age)
print("Finished program...")

