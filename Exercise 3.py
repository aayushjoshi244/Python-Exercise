while True:
    import random
    a = input("Enter your Name:- ")
    print(f"Welcome {a} to KBC (Kaun Banega Crorepati)")
    print(f"So the basic rules are:-\n1. One incorrect answer will lead to discollify\n2. For the first 4 questions, there is no time limit but after that there is 30 sec time limit")
    b = input("Should we start the game(Y/N):-")
    if b == "Y" or b == "y":

        question = {
            1: "What is the capital of Bhutan?",
            2: "Under what IPC a person couldn be arrested for public property disruption?",
            3: "Who was the 1st Indian education minister?",
            4: "Which movie got the 1st Oscar award?",
            5: "Who introduced the first financial plan for India?",
            6: "What was the name of Louis XVI's father?",
            7: "When did Hitler fight his first battle?"
        }

        a1 = ["Paro", "Thimpu", "Jhakar", "Ha"]
        a2 = ["Section 298", "Section 303", "Section 438", "Section 278"]
        a3 = ["Subhash Chandra Bose", "Jawaharlal Nehru", "Sawarkar Sahab", "Uddham Singh"]
        a4 = ["Wings", "Sunrise", "Mother India", "Slum Dog"]
        a5 = ["Sir M. Visvesvaraya", "Mahatma Gandhi", "Dadabhai Naoroji", "Jawaharlal Nehru"]
        a6 = ["Charles IX", "Louis XV", "Louis XVIII", "Francis"]
        a7 = ["October 1914", "August 1914", "September 1914", "October 1914"]

        for i in range(1, 8):
            random_number = random.randint(1, 7)
            print(question[random_number])
            options = locals()[f'a{random_number}']
            for idx, option in enumerate(options, 1):
                print(f"{idx}. {option}")

            user_input = int(input("Enter the option number: "))
            correct_option = 0
            if random_number == 1:
                correct_option = 2
            elif random_number == 2:
                correct_option = 4
            elif random_number == 3:
                correct_option = 2
            elif random_number == 4:
                correct_option = 1
            elif random_number == 5:
                correct_option = 4
            elif random_number == 6:
                correct_option = 2
            elif random_number == 7:
                correct_option = 2
            if user_input == correct_option:
                print("Correct! Proceeding to the next question.")
            else:
                print("Incorrect! You lose.")
                break  # Game over if the answer is wrong
        else:
            print("Congratulations! You've answered all questions correctly!")

    elif b =="N" or b =="n":
        print("Agli baar mt aa jaio yha")
    else:
        print("Khelna hai khel bakchodi mt kr ")