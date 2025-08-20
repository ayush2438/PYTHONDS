"""
Challenge: Stylish Bio Generator for Instagram/Twitter

Create a Python utility that asks the user for a few key details and generates a short, stylish bio that could be used for social media profiles like Instagram or Twitter.

Your program should:
1. Prompt the user to enter their:
   - Name
   - Profession
   - One-liner passion or goal
   - Favorite emoji (optional)
   - Website or handle (optional)

2. Generate a stylish 2-3 line bio using the inputs. It should feel modern, concise, and catchy.

3. Add optional hashtags or emojis for flair.

Example:
Input:
  Name: Riya
  Profession: Designer
  Passion: Making things beautiful
  Emoji: 🎨
  Website: @riya.design

Output:
  🎨 Riya | Designer  
  💡 Making things beautiful  
  🔗 @riya.design

Bonus:
- Let the user pick from 2-3 different layout styles.
- Ask the user if they want to save the result into a `.txt` file.
"""
# Stylish Bio Generator for Instagram/Twitter
# Author: You
# Date: August 2025

def inputs():
    print("🔧 Let's build your stylish bio!")
    Name = input("Enter your name: ").strip()
    Profession = input("Enter your profession: ").strip()
    Passion = input("Enter your passion or goal (one line): ").strip()
    Favorite_emoji = input("Enter your favorite emoji (optional): ").strip() or "✨"
    Website = input("Enter your handle or website (optional): ").strip() or "N/A"
    return Name, Profession, Passion, Favorite_emoji, Website

# Get user input
Name, Profession, Passion, Favorite_emoji, Website = inputs()

# Basic bio format
base_format = f"{Favorite_emoji} {Name} | {Profession}\n💡 {Passion}\n🔗 {Website}"

# Layout options
l_one = f"🔥 {base_format} ☄️"
l_two = f"🌸 {base_format} 🎴"
l_three = f"🌌 {base_format} ✨"

# Layout menu
print("\n🎨 Choose a layout style:")
print("1. Flairy 🔥☄️")
print("2. Flowery 🌸🎴")
print("3. Stars 🌌✨")

# Normalize choice input
choose = input("Enter 1, 2, or 3: ").strip().lower()
layout_map = {
    "1": l_one,
    "flairy": l_one,
    "2": l_two,
    "flowery": l_two,
    "3": l_three,
    "stars": l_three
}

# Select layout
selected_bio = layout_map.get(choose, base_format)

print("\n✨ Your Stylish Bio:\n")
print(selected_bio)

# Ask if user wants to save
save = input("\n💾 Do you want to save this bio to a .txt file? (y/n): ").strip().lower()

if save == "y":
    file_name = Name.strip().replace(" ", "_") + "_bio.txt"
    with open(file_name, "w") as f:
        f.write(selected_bio + "\n")
        # Optional hashtags
        hashtags = f"#bio #{Profession.lower().replace(' ', '')} #passion"
        f.write(hashtags)
    print(f"\n✅ Bio saved to '{file_name}' with hashtags.")
else:
    print("\n👍 Bio not saved. You're all set!")
