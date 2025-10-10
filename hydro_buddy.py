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

import sys

# Greeting
name = input("Hi, I'm HydroBuddy! What's your name? ")
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

# Special case: one ounce to reach goal
leftover = goal - intake
while leftover == 1:
    print(f"\nYou're right there, {name}! Only one ounce of water left to reach your goal!")
    sys.exit()

# All other cases (percentage towards goal)
if intake >= goal:
    print(f"\nGreat job {name}, you met your goal of {goal} ounces of water!")
elif intake >= goal*.7:
    print(f"\nKeep going. You're almost there, {name}! Only {goal - intake} ounces of water left to reach your goal!")
elif intake >= goal*.6:
    print(f"\nGood job {name}. Only {goal - intake} ounces of water left to reach your goal!")
elif intake == goal*.5:
    print(f"\nYou're halfway there {name}! Only {goal - intake} ounces of water to go!")
# Special case: no water intake
elif intake == 0:
    print(f"\nLet's get going, {name}. Drink some water!")
else:
    print(f"\nI know you can do it {name}! Keep drinking so you can reach your goal of {goal} ounces of water.")

# WHAT I LEARNED
# Convert digits with string data types to integers with int()
# .isdigit() checks if input contains only digits before converting.
# use break to exit a loop completely.
# use continue to skip to the next loop iteration.
# import sys then use sys.exit() to stop the entire program immediately.
# while True loops run until break or sys.exit() is executed.
# order of conditions matters — Python checks from top to bottom.