# Shree Ganeshay namah 
questions = [
    ["Who is best batsman in the World?", "Sachine Tedulkar", "MS Dhoni", "Virat Kohli","Kane Williamson",  3],
    ["What is Variable", "A Box Where You Store Values", "a type of graphics", "Data type","a type of Maemory",  4],
    [ "Current Railway Minister of India is", "Mamta Banarjee", "Ram Vilash", "Ashwini Vaishnaw",
    "Piyush Goye;l",  3],
    ["What is Java","Snake","Gamming","Programming language","ok",4],
    [ "Which god is also known as ‘Gauri Nandan’?", "Agni", "Indra", "Hanuman",
    "Ganesha",  4],
    [ "What does not grow on tree according to a popular Hindi saying?", "Money", "Flowers", "Leaves","Fruits",
      1],
    ["Which `city` is known as Pink City in India?", "Banglore", "Maysore", "Jaipur","Kochi",
     3],
    ["Who wrote India's National Anthem?", "Rabindranath Tagore", "Lal Bahadur Shastri", "Chetan Bhagat","RK Narayan",
     1],
    [ "How many states are there in India?", "28", "33", "29","31",1],
    ["Which Department Your Favorate", "ECE", "COMPUTER", "IT","CIVIL",
     3],
]

money = 0
correct_answers = 0  # Track the number of correct answers
levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
try:
    for i in range(0, len(questions)):
        print(f"Your Question For {levels[i]}")
        print(questions[i][0])
        print(f"A. {questions[i][1]}        B. {questions[i][2]}")
        print(f"C. {questions[i][3]}        D. {questions[i][4]}")
        ans = int(input("Enter Answer in (1-4) Digit and 0 to quit: "))

        if ans == 0:
            print("Thanks For Participating!")
            break
        elif ans == questions[i][5]:
            print("YOU ARE CORRECT")
            print(f"You Won Rs {levels[i]}\n")
            correct_answers += 1  # Increment correct_answers count
            if correct_answers == 5:  # Check if 5 correct answers reached
                money = 10000
                print("Congratulations! You've won Rs 10,000!")
            elif correct_answers == 9:
                money = 320000
                print("Congratulations! You've won Rs 10,000!")
                # break
        else:
            print("You Entered the Wrong Answer")
            print(f"Your Final Money Value is {money}")
            break
except ValueError:
    print("Enter Answer is between 1 to 4 Digit ")
    print("You need to find Penelty Repeat All")

