print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0


answer = input("1. What does CPU stand for? ").lower()

if answer == "central processing unit":
    print("That's correct!!")
    score += 1
else:
    print("That is incorrect!")

answer = input("2. What converts an entire program into machine language? ").lower()

if answer == "compiler":
    print("That's correct!!")
    score += 1
else:
    print("That is incorrect!")

answer = input("3. What does DOS stand for? ").lower()

if answer == "disk operating system":
    print("That's correct!!")
    score += 1
else:
    print("That is incorrect!")

answer = input("4. Full form of LAN? ").lower()

if answer == "local area network":
    print("That's correct!!")
    score += 1
else:
    print("That is incorrect!")

answer = input("5. What are Light pen and joystick? ")

if answer == "input devices":
    print("That's correct!!")
    score += 1
else:
    print("That is incorrect!")

answer = input(" ")


print("You got " + str(score) + " questions correct!")
print("You got " + str((score/5) * 100) + "%")