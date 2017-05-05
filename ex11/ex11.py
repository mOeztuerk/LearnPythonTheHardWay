print("How old are you?")
age = input()
print("How tall are you?")
height = input()
print("How much do you weigh?")
weight = input()

print("So, you're {} old, {} tall and {} heavy.".format(age, height, weight))


city = input("Liste? ")
print(city)

population = eval(input("Städte und Einwohner: "))
print(population)


print("Fangen wir an. Ja oder Nein?", end=" ")
antwort = input()
print("Deine Antwort war {}".format(antwort))
print("Was machst du?", end=" ")
mache = input()

print(type(mache))
