print ("What kind of chocolate bar are you? Take this personality quiz to find out!\n")
score = 0
answer1 = input ("What is your ideal way to spend a weekend?\na) Going on an outdoor adventure\nb) Staying home watching a movie or reading a book\nc) Trying a new hobby\nd) Hanging out with family and friends\nEnter a, b, c, or d. ")
if answer1 == "a":
    score += 5
elif answer1 == "b":
    score += 2
elif answer1 == "c":
    score += 4
else:
    score += 3


answer2 = input ("\nWhat kind of movies do you enjoy most?\na) Action\nb) Romance\nc) Comedy\nd) Mystery\nEnter a, b, c, or d. ")
if answer1 == "a":
    score += 5
elif answer1 == "b":
    score += 2
elif answer1 == "c":
    score += 3
else:
    score += 4

answer3 = input ("\nHow do you handle stress?\na) Go for a run\nb) Take a nap or mediate\nc) Talk to friends and family about it\nd) Work on a new hobby or listen to music\n Enter a, b, c, or d. ")
if answer1 == "a":
    score += 5
elif answer1 == "b":
    score += 2
elif answer1 == "c":
    score += 3
else:
    score += 4

answer4 = input ("\nWhat is your go-to snack when you are craving something sweet?\na) Candy\nb) Cookies\nc) Fruit\nd) Ice cream/ milkshake\n Enter a, b, c, or d. ")
if answer1 == "a":
    score += 5
elif answer1 == "b":
    score += 3
elif answer1 == "c":
    score += 2
else:
        score += 4

answer5 = input ("\nWhich weather do you like best?\na) Warm and sunny\nb) Cool and cozy\nc) Breezy and mild\nd) Cloudy or rainy\n Enter a, b, c, or d. ")
if answer1 == "a":
    score += 5
elif answer1 == "b":
    score += 2
elif answer1 == "c":
    score += 3
else:
    score += 4

answer6 = input ("\nWhich word best describes you?\na) Energetic\nb) Calm\nc) Outgoing\nd) Creative\n Enter a, b, c, or d. ")
if answer1 == "a":
    score += 5
elif answer1 == "b":
    score += 2
elif answer1 == "c":
    score += 3
else:
    score += 4

if score >= 12 and score <= 18:
    print ("\nYou are a Hershey bar! You are classic, dependable, and sweet.")
elif score >= 19 and score <= 22:
    print ("\nYou are a KitKat! You are balanced, reliable, and know when to take a break.")
elif score >= 23 and score <= 25:
    print ("\nYou are a Twix! You are fun, creative, and full of surprises.")
else:
    print ("\nYou are a Snickers! You are energetic, adventurous, and always on the go.")

print()
print ("Thank you for taking this quiz!")
