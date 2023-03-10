import random

body = False
head1 = False
head2 = False
antennae1 = 0
antennae2 = 0
eyes1 = 0
eyes2 = 0
mouth1 = 0
mouth2 = 0
legs = 0
mutant = False  # Initialize mutant to False

# Initialize the summary counts
total_rolls = 0
head_rolls = 0
mutant_beetles = 0


def play_beetle():
    global body, head1, head2, antennae1, antennae2, eyes1, eyes2, mouth1, mouth2, legs, mutant, total_rolls, head_rolls, mutant_beetles

    print("Welcome to Beetle!\n")

    # Play the game until all the body parts are collected
    parts_collected = 0
    while parts_collected < 11:

        roll = random.randint(1, 10)

        # Check for the Beetle body
        if roll == 1:
            if not body:
                body = True
                parts_collected += 1
                print("You rolled a 1! You got a Beetle body.")
            else:
                print("You already have a Beetle body.")

        # Check for the Beetle head 1
        elif roll == 2:
            if not head1 and body:
                head1 = True
                parts_collected += 1
                print("You rolled a 2! You got a Beetle head 1.")
            elif not body:
                print("You need a Beetle body before you can get a head.")
            else:
                print("You already have a Beetle head 1.")

        # Check for the Beetle head 2
        elif roll == 3:
            if not head2 and body:
                head2 = True
                parts_collected += 1
                print("You rolled a 3! You got a Beetle head 2.")
            elif not body:
                print("You need a Beetle body before you can get a head.")
            else:
                print("You already have a Beetle head 2.")

        # Check for the Beetle antennae 1
        elif roll == 4:
            if head1 and antennae1 < 2:
                antennae1 += 1
                parts_collected += 1
                print("You rolled a 4! You got a Beetle antenna 1.")
            elif not head1:
                print("You need a Beetle head 1 before you can get antennae.")
            else:
                print("You already have two Beetle antennae 1.")

        # Check for the Beetle antennae 2
        elif roll == 5:
            if head2 and antennae2 < 2:
                antennae2 += 1
                parts_collected += 1
                print("You rolled a 5! You got a Beetle antenna 2.")
            elif not head2:
                print("You need a Beetle head 2 before you can get antennae.")
            else:
                print("You already have two Beetle antennae 2.")

        # Check for the Beetle eyes 1
        elif roll == 6:
            if head1 and eyes1 < 2:
                eyes1 += 1
                parts_collected += 1
                print("You rolled a 6! You got a Beetle eye 1.")
            elif not head1:
                print("You need a Beetle head 1 before you can get eyes.")
            else:
                print("You already have two Beetle eyes 1.")

        # Check for the Beetle eyes 2
        elif roll == 7:
            if head2 and eyes2 < 2:
                eyes2 += 1
                parts_collected += 1
                print("You rolled a 7! You got a Beetle eye 2.")
            elif not head1:
                print("You need a Beetle head 1 before you can get eyes.")
            else:
                print("You already have two Beetle eyes 1.")

        # Check for the Beetle mouth 1
        elif roll == 8:
            if head1 and not mouth1:
                mouth1 = 1
                parts_collected += 1
                print("You rolled an 8! You got a Beetle mouth 1.")
            elif not head1:
                print("You need a Beetle head 1 before you can get a mouth.")
            else:
                print("You already have a Beetle mouth 1.")
        # Check for the Beetle mouth 2
        elif roll == 9:
            if head2 and not mouth2:
                mouth2 = 1
                parts_collected += 1
                print("You rolled a 9! You got a Beetle mouth 2.")
            elif not head2:
                print("You need a Beetle head 2 before you can get a mouth.")
            else:
                print("You already have a Beetle mouth 2.")

        # Check for the Beetle legs
        elif roll == 10:
            if body and legs < 6:
                legs += 1
                parts_collected += 1
                print("You rolled a 10! You got a Beetle leg.")
            elif not body:
                print("You need a Beetle body before you can get legs.")
            else:
                print("You already have six Beetle legs.")

        print("body:", body, "head1:", head1, "head2:", head2, "antennae1:", antennae1, "antennae2:",
              antennae2, "eyes1:", eyes1, "eyes2:", eyes2, "mouth1:", mouth1, "mouth2:", mouth2, "legs:", legs)
        # Print the current status of body parts
        print("\nCurrent Beetle status:")
        print("Body: ", "Complete" if body else "Incomplete")
        print("Head 1: ", "Complete" if head1 else "Incomplete")
        print("Head 2: ", "Complete" if head2 else "Incomplete")
        print("Antennae 1: ", antennae1, "/2")
        print("Antennae 2: ", antennae2, "/2")
        print("Eyes 1: ", eyes1, "/2")
        print("Eyes 2: ", eyes2, "/2")
        print("Mouth 1: ", "Complete" if mouth1 else "Incomplete")
        print("Mouth 2: ", "Complete" if mouth2 else "Incomplete")
        print("Legs: ", legs, "/6\n")

    # Print the final message when all body parts are collected
    if body and head1 and head2 and antennae1 == 2 and antennae2 == 2 and eyes1 == 2 and eyes2 == 2 and mouth1 == 1 and mouth2 == 1 and legs == 6:
        print("Congratulations! You have assembled a complete Mutant Beetle with two heads!")
        print("It took you", total_rolls, "rolls to collect all the body parts.")
        print("It took you", head_rolls, "rolls to collect all the body parts.")
    if mutant:
        print("You created a mutant Beetle!")
        mutant_beetles += 1
    else:
        print("You created a normal Beetle.")

# Now run the game
play_beetle()
