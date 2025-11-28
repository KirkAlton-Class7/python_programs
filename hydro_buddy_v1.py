# ----------------------------------------------------------
# Python Practice: Water Intake Tracker
# ----------------------------------------------------------

# Build a simple program that motivates users to stay hydrated.
#
# Details:
# - The user will set a daily water intake goal (in number of glasses).
# - The user will then enter how many glasses of water they drank today.
# - The program will respond with a motivational or congratulatory message based on their progress.

# Your program should:
# 1. Greet the user with a friendly welcome message.
# 2. Ask the user to enter their daily water goal (number of glasses they aim to drink).
# 3. Ask how many glasses of water they have had today.
# 4. Compare their progress to the goal and respond:
#    - If they are below half their goal, encourage them to drink more.
#    - If they are close to their goal, compliment their progress.
#    - If they met or exceeded their goal, congratulate them for great hydration.
# 5. End with a positive message to motivate them to keep going.

# ----------------------------------------------------------
# HydroBuddy V1
# ----------------------------------------------------------

# Greeting
name = input("Hi, I'm HydroBuddy! What's your name? ")
def greet(name):
    print(f"\nHi {name}!")

# Input Goal

while True:
    goal = input(f"\nWhat's your hydration goal? (Enter number of ounces as a whole number) " )

    # Special case: goal = 0
    if goal == "0":
        print(f"\nCome on {name}, you can do better than that!")
        continue # loop back and re-ask
    # Check if the input string is all digits
    if goal.isdigit():
        goal = int(goal)
        print("\nThanks for sharing your goal")
        break # exit loop when valid

# Input water intake
while True:
    intake = input(f"\nHow much water have you drank today? (Enter a whole number in ounces) ")

    if intake.isdigit():
        intake = int(intake)
        break # exit loop when valid

# Motivation (based on percentage towards goal)
if intake >= goal:
    print(f"\nCongratulations {name}! You met your goal of {goal} ounces of water!")
# Special case: one unit until goal
if goal - intake == 1:
    print(f"\nYou're right there {name}! Only one ounce of water left to reach your goal!")
elif intake >= goal*.7 and intake < goal:
    print(f"\nYou're almost there {name}! Only {goal - intake} ounces of water left to reach your goal!")
elif intake >= goal*.6 and intake < goal:
    print(f"\nGood job {name}. Only {goal - intake} ounces of water left to reach your goal!")
elif intake == goal*.5 and intake < goal:
    print(f"\nYou're halfway there {name}! Only {goal - intake} ounces of water to go!")
# Special case: no water intake
elif intake == 0:
    print(f"\nLet's get going {name}. Drink some water!")
else:
    print(f"\nI know you can do it {name}! Keep drinking so you can reach your goal of {goal} ounces of water.")

# WHAT I LEARNED
# Keep your code DRY. DON'T REPEAT YOURSELF!
# Convert digits with string data types to integers with int()
# .isdigit() checks if input contains only digits before converting.
# use break to exit a loop completely.
# use continue to skip to the next loop iteration.
# import sys then use sys.exit() to stop the entire program immediately.
# while True loops run until break or sys.exit() is executed.
# order of conditions matters — Python checks from top to bottom.

# IMPROVEMENTS TO MAKE
# 1. I think you commented out the if goal.isdigit() line in the goal input loop.
# 2. what if the intake input is anything but a positive integer? Also why wouldn’t a float be acceptable input?
# 3. Concerning best practices: you don’t need the final while loop, why not add this output to the if-else statement?
# 4. This would also allow you to avoid using the sys.exit function and module entirely (which isn’t really a good practice).
# 5. Take it to the next level and break it up into functions that return the user input.
# 6. You already have what should be a function identified based on the comments
# 7. Incorporate unit tests to test your code.