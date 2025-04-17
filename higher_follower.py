import random

# 🎮 Welcome Message
print("🎉 Welcome to the Instagram Follower Battle Game!")
print("Can you guess who has more followers on Instagram? 🤔")
print("Keep guessing and climb the scoreboard! 🧠🔥\n")

# 📊 Instagram accounts data
ig_acc = [
    {"name": "Cristiano Ronaldo", "followers": 651, "profession": "Footballer", "country": "Portugal"},
    {"name": "Lionel Messi", "followers": 505, "profession": "Footballer", "country": "Argentina"},
    {"name": "Selena Gomez", "followers": 421, "profession": "Musician and Actress", "country": "United States"},
    {"name": "Kylie Jenner", "followers": 394, "profession": "Media Personality and Businesswoman", "country": "United States"},
    {"name": "Dwayne Johnson", "followers": 394, "profession": "Actor and Wrestler", "country": "United States"},
    {"name": "Ariana Grande", "followers": 376, "profession": "Musician and Actress", "country": "United States"},
    {"name": "Kim Kardashian", "followers": 357, "profession": "Media Personality", "country": "United States"},
    {"name": "Beyoncé", "followers": 312, "profession": "Musician and Actress", "country": "United States"},
    {"name": "Khloé Kardashian", "followers": 303, "profession": "Media Personality", "country": "United States"},
    {"name": "Nike", "followers": 301, "profession": "Sportswear Brand", "country": "United States"},
    {"name": "Justin Bieber", "followers": 294, "profession": "Musician", "country": "Canada"},
    {"name": "Kendall Jenner", "followers": 288, "profession": "Media Personality", "country": "United States"},
    {"name": "Taylor Swift", "followers": 282, "profession": "Musician", "country": "United States"},
    {"name": "National Geographic", "followers": 279, "profession": "Magazine", "country": "United States"},
    {"name": "Virat Kohli", "followers": 271, "profession": "Cricketer", "country": "India"},
    {"name": "Jennifer Lopez", "followers": 249, "profession": "Musician and Actress", "country": "United States"},
    {"name": "Neymar", "followers": 229, "profession": "Footballer", "country": "Brazil"},
    {"name": "Nicki Minaj", "followers": 226, "profession": "Musician", "country": "Trinidad and Tobago"},
    {"name": "Kourtney Kardashian", "followers": 219, "profession": "Media Personality", "country": "United States"},
    {"name": "Miley Cyrus", "followers": 213, "profession": "Musician and Actress", "country": "United States"},
    {"name": "Katy Perry", "followers": 204, "profession": "Musician", "country": "United States"},
    {"name": "Zendaya", "followers": 179, "profession": "Actress and Singer", "country": "United States"},
    {"name": "Kevin Hart", "followers": 177, "profession": "Comedian and Actor", "country": "United States"},
    {"name": "Real Madrid CF", "followers": 173, "profession": "Football Club", "country": "Spain"},
    {"name": "Cardi B", "followers": 164, "profession": "Musician and Actress", "country": "United States"},
    {"name": "LeBron James", "followers": 159, "profession": "Basketball Player", "country": "United States"},
    {"name": "Demi Lovato", "followers": 153, "profession": "Musician and Actress", "country": "United States"},
    {"name": "Rihanna", "followers": 149, "profession": "Musician", "country": "Barbados"},
    {"name": "Chris Brown", "followers": 144, "profession": "Musician", "country": "United States"},
    {"name": "Drake", "followers": 143, "profession": "Musician", "country": "Canada"},
    {"name": "Ellen DeGeneres", "followers": 136, "profession": "Comedian and Television Host", "country": "United States"},
    {"name": "FC Barcelona", "followers": 136.9, "profession": "Football Club", "country": "Spain"},
    {"name": "Kylian Mbappé", "followers": 123, "profession": "Footballer", "country": "France"},
    {"name": "Billie Eilish", "followers": 123.8, "profession": "Musician", "country": "United States"},
    {"name": "UEFA Champions League", "followers": 120, "profession": "Club Football Competition", "country": "Europe"},
    {"name": "Gal Gadot", "followers": 108, "profession": "Actress", "country": "Israel"},
    {"name": "Lisa", "followers": 105, "profession": "Musician", "country": "Thailand"},
    {"name": "Vin Diesel", "followers": 103, "profession": "Actor", "country": "United States"},
    {"name": "NASA", "followers": 96, "profession": "Space Agency", "country": "United States"},
    {"name": "Shraddha Kapoor", "followers": 94, "profession": "Actress", "country": "India"}
]

# 🔍 Function to compare followers and update score
def compare(acc_a, acc_b, guess, score):
    if guess == 'A':
        if acc_a["followers"] > acc_b["followers"]:
            print("🎯 Correct!")
            score += 1
            return acc_a, score
        else:
            print("❌ Wrong!")
            return None, score

    elif guess == 'B':
        if acc_b["followers"] > acc_a["followers"]:
            print("🎯 Correct!")
            score += 1
            return acc_b, score
        else:
            print("❌ Wrong!")
            return None, score

    print("⚠️ Invalid input.")
    return None, score

# 🎮 Game loop
score = 0
acc_a = random.choice(ig_acc)

while True:
    acc_b = random.choice(ig_acc)
    # Avoid same account being selected
    while acc_b == acc_a:
        acc_b = random.choice(ig_acc)

    # Display Account A
    print("\n🔵 Account A:")
    print(f"👤 Name: {acc_a['name']}")
    print(f"💼 Profession: {acc_a['profession']}")
    print(f"🌍 Country: {acc_a['country']}")

    print("\n⚔️  VS\n")

    # Display Account B
    print("🟢 Account B:")
    print(f"👤 Name: {acc_b['name']}")
    print(f"💼 Profession: {acc_b['profession']}")
    print(f"🌍 Country: {acc_b['country']}")

    # User's guess
    guess = input("\n🤔 Who has more followers? Type 'A' or 'B': ").upper()

    # Compare and get result
    winner_acc, score = compare(acc_a, acc_b, guess, score)

    if winner_acc is None:
        print(f"\n💀 Game Over! Your final score is {score} 🏁")
        break

    acc_a = winner_acc  # Winner becomes next A
    print(f"🔥 You're on fire! Current Score: {score}")
