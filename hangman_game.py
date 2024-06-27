import random

# Categories and words
categories = {
    "Countries": ['AMERICA', 'SWITZERLAND', 'AUSTRALIA', 'CANADA', 'GERMANY', 'INDIA', 'JAPAN', 'SOUTH KOREA', 'UNITED KINGDOM'],
    "Continents": ['AFRICA', 'ASIA', 'EUROPE', 'NORTH AMERICA', 'SOUTH AMERICA', 'ANTARCTICA', 'AUSTRALIA'],
    "Fruits": ['APPLE', 'BANANA', 'CHERRY', 'DATE', 'FIG', 'GRAPE', 'LEMON', 'MANGO', 'ORANGE', 'PEACH'],
    "Animals": ['LION', 'TIGER', 'ELEPHANT', 'GIRAFFE', 'ZEBRA', 'KANGAROO', 'PANDA', 'MONKEY', 'CROCODILE', 'DOLPHIN']
}

# Display categories to the user
print("Select a category:")
for i, category in enumerate(categories.keys()):
    print(f"{i + 1}. {category}")

# Get user's choice
category_choice = int(input("Enter the number corresponding to your choice: ")) - 1
selected_category = list(categories.keys())[category_choice]

# Select a random word from the chosen category
chosen_word = random.choice(categories[selected_category])
display = ["_" for _ in range(len(chosen_word))]
print(display)

chances = 6
s = set([])
k = 0
l2 = 0

while chances > 0:
    l1 = 0
    guessed_letter = input("Guess a letter: ").upper()
    for i in range(len(chosen_word)):
        if i not in s and guessed_letter == chosen_word[i]:
            display[i] = guessed_letter
            s.add(i)
            l1 = 1
            break
    if l1 == 0:
        chances -= 1
    k += 1
    if k - (6 - chances) == len(chosen_word):
        l2 = 1
        break
    print(display, chances)

if l2 == 0:
    print("GAME OVER")
    print("THE WORD WAS:", chosen_word)
else:
    print("YOU WON")
    print("THE WORD WAS:", chosen_word)
