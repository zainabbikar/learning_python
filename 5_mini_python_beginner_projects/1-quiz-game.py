# https://www.youtube.com/watch?v=DLn3jOsNRVE

print("Welcome My Thermodynamics Quiz!")

playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
print("Okay, let's test your knowledge! :)")
score = 0

# Question 1
answer = input("Q1: Which law of thermodynamics states heat does not spontaneously flow from a colder body to a hotter one.? ")
if answer.lower() == "second law of thermodynamics":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
# Question 2
answer = input("Q2: Which thermodynamics processes occurs without a change in the internal energy? ")
if answer.lower() == "steady state process":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 3
answer = input("Q3: What is the value of the absolute thermodynamic temperature scale in Kelvin? ")
if answer.lower() == "zero":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 4
answer = input("Q4: What is the standard fixed point of thermometry? ")
if answer.lower() == "the triple point of water":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
# Question 5
answer = input("Q5: What state is chosen as the standard thermometric substance? ")
if answer.lower() == "gas":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

if 0 < score < 4:
    print("Unfortunately you got " + str(score) + " questions correct!")
    print("You got " + str(score/5*100) + " %. Keep Practicing!")
else:
    print("Congratulations! You got " + str(score) + " questions correct!")
    print("You got " + str(score/5*100) + " %. Keep Up The Good Work!")