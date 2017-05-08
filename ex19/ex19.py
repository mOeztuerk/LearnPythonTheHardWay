# define the function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have {} cheeses!".format(cheese_count))
    print("You have {} boxes of crackers".format(boxes_of_crackers))
    print("Man that is enough for a party")
    print("Get a blanket.\n")

# give arguments as numbers
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# give arguments as variables
print("or we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)
# do math with the arguments
print("we can even do math inside too:")
cheese_and_crackers(10+20, 5+6)
# combine math and variables
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


def second_func(arg1, arg2, arg3):
    print("this is arg1", arg1)
    print("this is arg2", arg2)
    print("this is arg3", arg3)
    print("\n")

second_func(1, 1, 1)
second_func(3+2+1, 3+2+2+2, 3+23)
second_func(max(3, 2), min(2, 1), len("oc"))
second_func("this", "nervt", "übel")
