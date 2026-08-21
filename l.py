import random
name = input("Type Proper Noun(Person's Name):")
adjective1 = input("Type Adjective:")
color = input("Type Color:")
animal = input("Type Animal:")
place = input("Type Place:")
adjective2 = input ("Type Adjective:")
magical1 = input("Type Magical Creature (Plural):")
adjective3 = input("Type Adjective:")
magical2 = input("Type Magical Creature(Plural):")
room = input("Type Room in a House:")
noun1 = input("Type Noun:")
noun2 = input(" Type Noun:")
noun3 = input("Type Noun(Plural):")
adjective4 = input("Type Adjective:")
noun4 = input("Type Noun(Plural):")
number = input("Type Number:")
time = input("Type Measure of time:")
verb = input("Type Verb (ending in ing):")
adjective5 = input("Type AAdjective:")
noun5 = input("Type Noun:")
story = f"""Dear {name}, I am writing to you from a {adjective1} castle in an enchanted forest.
I found myelf here one day after going for a ride on a {color} {animal} in {place}. There are {adjective2} {magical1}
and {adjective3} {magical2} here! In the {room} there is a pool full
of {noun1}. I fall asleep each night on a {noun2} of {noun3} and dream of {adjective4} {noun4}. it
feels as though I have lived here for {number} {time}. I hope one day you can visit, although the only way to get here now is {verb} on a {adjective5} {noun5}!!"""
openings = ["Dear", "Castle", "Dream"]
header = random.choice(openings)
print("\n" + header)
print(story)