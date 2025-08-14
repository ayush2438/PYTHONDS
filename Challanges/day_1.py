"""
 Challenge: Self-Intro Script Generator

Create a Python script that interacts with the user and generates a personalized self-introduction.

Your program should:
1. Ask the user for their name, age, city, profession, and favorite hobby.
2. Format this data into a warm, friendly paragraph of self-introduction.
3. Print the final paragraph in a clean and readable format.

Example:
If the user inputs:
  Name: Priya
  Age: 22
  City: Jaipur
  Profession: Software Developer
  Hobby: playing guitar

Your script might output:
  "Hello! My name is Priya. I'm 22 years old and live in Jaipur. I work as a Software Developer and I absolutely enjoy playing guitar in my free time. Nice to meet you!"

Bonus:
- Add the current date to the end of the paragraph like: "Logged on: 2025-06-14"
- Wrap the printed message with a decorative border of stars (*)
"""

import datetime
def ask():
    name = input("What is your name? ")
    age = input("How old are you? ")
    city = input("Which city do you live in? ")
    profession = input("What is your profession? ")
    hobby = input("What is your favorite hobby? ")
    
    return name, age, city, profession, hobby

def generate_paragraph(name, age, city, profession, hobby):
    return f"Hello! My name is {name}.\n I'm {age} years old and live in {city}.\n I work as a {profession} and I absolutely enjoy {hobby} in my free time.\n Nice to meet you! "

