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
from datetime import date
from datetime import datetime

currenttime=datetime.now().strftime("%Ihr:%Mmin:%Ssec %p")
today = date.today()
def inputs():
  Name=input("enter your name :")
  Age=input("enter your Age :")
  City=input("enter your City :")
  Profession=input("enter your Profession :")
  Hobby=input("enter your Hobby :")
  return Name,Age,City,Profession,Hobby

Name, Age, City, Profession, Hobby = inputs()

decoration = "*" * 80
double_decoration = f"{decoration}\n{decoration}"

# Use f-string for proper formatting
Paragraph = f"Hello! My name is {Name}.\nI'm {Age} years old and live in {City}.\nI work as a {Profession} and I absolutely enjoy {Hobby} in my free time. Nice to meet you!\nlogged on:{today} ,{currenttime}"

# Print with decoration
print(double_decoration)
print(Paragraph)
print(double_decoration)
