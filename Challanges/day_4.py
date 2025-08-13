"""
 Challenge: Minutes Alive Calculator

Write a Python script that calculates approximately how many minutes old a person is, based on their age in years.

Your program should:
1. Ask the user for their age in years (accept float values too).
2. Convert that age into:
   - Total days
   - Total hours
   - Total minutes
3. Display the result in a readable format.

Assumptions:
- You can use 365.25 days/year to account for leap years.
- You don't need to handle time zones or exact birthdates in this version.

Example:
Input:
  Age: 25

Output:
  You are approximately:
    - 9,131 days old
    - 219,144 hours old
    - 13,148,640 minutes old

Bonus:
- Add comma formatting for large numbers
- Let the user try again without restarting the program
"""
def minutes_alive():
  age= float(input("Enter your age in years: "))

  days = age * 365.25
  hours = days * 24
  minutes = hours * 60

  print(f"You are approximately:\n"
        f"- {days:,} days old\n"
        f"- {hours:,} hours old\n"
        f"- {minutes:,} minutes old")

while True:
  minutes_alive()
  try_again = input("Do you want to try again? (y/n): ")
  if try_again.lower() != 'y':
    break
  
  print("\n")


























