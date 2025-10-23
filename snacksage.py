#!/usr/bin/env python3
"""
SnackSage - Your Wise Snacking Oracle
A fun CLI app that helps you decide what to snack on based on your mood!
"""

import random
import sys


class SnackSage:
    """The all-knowing sage of snacking wisdom"""

    SNACKS = {
        "sweet": [
            "Dark chocolate squares",
            "Fresh berries with honey",
            "Greek yogurt with granola",
            "Apple slices with peanut butter",
            "Trail mix with dried fruit",
            "Banana bread",
            "Chocolate chip cookies (you deserve it!)",
            "Frozen grapes",
            "Dates stuffed with almond butter",
            "Fruit smoothie"
        ],
        "savory": [
            "Popcorn with herbs",
            "Cheese and crackers",
            "Hummus with veggies",
            "Pretzels",
            "Roasted chickpeas",
            "String cheese",
            "Pickle spears",
            "Olives and feta",
            "Salted almonds",
            "Crispy seaweed snacks"
        ],
        "healthy": [
            "Carrot sticks with hummus",
            "Celery with almond butter",
            "Mixed nuts (unsalted)",
            "Rice cakes with avocado",
            "Cherry tomatoes",
            "Cucumber slices",
            "Edamame",
            "Bell pepper strips",
            "Apple slices",
            "Blueberries"
        ],
        "indulgent": [
            "Ice cream sundae",
            "Nachos with all the toppings",
            "Pizza rolls",
            "Chocolate lava cake",
            "Loaded fries",
            "Brownie with ice cream",
            "Cheesecake",
            "Donut (or two!)",
            "Milkshake",
            "Fried mozzarella sticks"
        ],
        "energizing": [
            "Protein bar",
            "Peanut butter toast",
            "Hard-boiled eggs",
            "Energy balls",
            "Nut butter with banana",
            "Beef jerky",
            "Overnight oats",
            "Protein smoothie",
            "Cottage cheese with fruit",
            "Granola bar"
        ]
    }

    MOODS = {
        "stressed": ["sweet", "indulgent"],
        "tired": ["energizing", "sweet"],
        "bored": ["savory", "indulgent"],
        "healthy": ["healthy", "energizing"],
        "celebration": ["indulgent", "sweet"],
        "focused": ["healthy", "savory"],
        "adventurous": ["savory", "indulgent"]
    }

    WISDOM = [
        "A wise snacker knows their cravings.",
        "In the pursuit of snacks, balance is key.",
        "Listen to your hunger, not just your cravings.",
        "Every snack is an opportunity for joy.",
        "The best snack is the one enjoyed mindfully.",
        "Sometimes the soul needs chocolate, and that's okay.",
        "Hydrate before you snackate!",
        "A snack shared is a snack doubled in joy."
    ]

    def __init__(self):
        self.ascii_art = """
    🧙‍♂️  SnackSage  🧙‍♂️
    ╔══════════════════╗
    ║  Wise Snacking   ║
    ║     Oracle       ║
    ╚══════════════════╝
        """

    def display_welcome(self):
        """Display welcome message"""
        print("\n" + "="*50)
        print(self.ascii_art)
        print("="*50)
        print("\nWelcome, seeker of snacking wisdom!")
        print(f"\n💭 {random.choice(self.WISDOM)}\n")

    def get_mood_suggestion(self):
        """Get snack suggestion based on mood"""
        print("\n🎭 How are you feeling right now?")
        print()
        moods = list(self.MOODS.keys())
        for i, mood in enumerate(moods, 1):
            print(f"  {i}. {mood.capitalize()}")
        print(f"  {len(moods) + 1}. Surprise me!")
        print()

        try:
            choice = input("Enter number (or 'q' to quit): ").strip()
            if choice.lower() == 'q':
                return None

            choice_num = int(choice)

            if choice_num == len(moods) + 1:
                # Random category
                category = random.choice(list(self.SNACKS.keys()))
            elif 1 <= choice_num <= len(moods):
                mood = moods[choice_num - 1]
                category = random.choice(self.MOODS[mood])
            else:
                print("❌ Invalid choice!")
                return self.get_mood_suggestion()

            snack = random.choice(self.SNACKS[category])
            print(f"\n✨ The SnackSage suggests: {snack}")
            print(f"   Category: {category.capitalize()}")
            print()

            return True

        except (ValueError, IndexError):
            print("❌ Please enter a valid number!")
            return self.get_mood_suggestion()

    def browse_by_category(self):
        """Browse snacks by category"""
        print("\n📚 Browse by category:")
        print()
        categories = list(self.SNACKS.keys())
        for i, cat in enumerate(categories, 1):
            print(f"  {i}. {cat.capitalize()} ({len(self.SNACKS[cat])} options)")
        print()

        try:
            choice = input("Enter number (or 'q' to quit): ").strip()
            if choice.lower() == 'q':
                return None

            choice_num = int(choice)

            if 1 <= choice_num <= len(categories):
                category = categories[choice_num - 1]
                print(f"\n🍽️  {category.capitalize()} Snacks:")
                print()
                for snack in self.SNACKS[category]:
                    print(f"   • {snack}")
                print()

                # Offer to pick one randomly
                pick = input("Pick one randomly from this list? (y/n): ").strip().lower()
                if pick == 'y':
                    snack = random.choice(self.SNACKS[category])
                    print(f"\n✨ The SnackSage suggests: {snack}\n")

                return True
            else:
                print("❌ Invalid choice!")
                return self.browse_by_category()

        except (ValueError, IndexError):
            print("❌ Please enter a valid number!")
            return self.browse_by_category()

    def random_snack(self):
        """Get a completely random snack"""
        category = random.choice(list(self.SNACKS.keys()))
        snack = random.choice(self.SNACKS[category])
        print(f"\n🎲 Random snack: {snack}")
        print(f"   Category: {category.capitalize()}")
        print()

    def run(self):
        """Main application loop"""
        self.display_welcome()

        while True:
            print("\n" + "─"*50)
            print("What would you like to do?")
            print()
            print("  1. Get suggestion based on my mood")
            print("  2. Browse snacks by category")
            print("  3. Give me a random snack")
            print("  4. Share wisdom")
            print("  5. Quit")
            print()

            choice = input("Enter number: ").strip()

            if choice == '1':
                result = self.get_mood_suggestion()
                if result is None:
                    break
            elif choice == '2':
                result = self.browse_by_category()
                if result is None:
                    break
            elif choice == '3':
                self.random_snack()
            elif choice == '4':
                print(f"\n💭 {random.choice(self.WISDOM)}\n")
            elif choice == '5' or choice.lower() == 'q':
                break
            else:
                print("\n❌ Please enter a valid option (1-5)")

        print("\n" + "="*50)
        print("🙏 May your snacks be ever satisfying!")
        print("   The SnackSage bids you farewell.")
        print("="*50 + "\n")


def main():
    """Entry point for the application"""
    try:
        sage = SnackSage()
        sage.run()
    except KeyboardInterrupt:
        print("\n\n🙏 The SnackSage bids you farewell!\n")
        sys.exit(0)


if __name__ == "__main__":
    main()
