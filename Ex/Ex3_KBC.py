kbc_questions_and_answers = ["What is the capital of India?", "Delhi", "What is the largest ocean on Earth?",
                             "Pacific Ocean", "What is the currency of Japan?", "yen",
                             "What is the tallest mountain in the world?", "Mount Everest",
                             "What is the largest mammal on Earth?", "Blue whale",
                             "What is the main ingredient in a traditional Greek moussaka?", "Eggplant",
                             "What is the boiling point of water in Celsius?", "100",
                             "What is the chemical symbol for gold?", "Au",
                             "What is the national bird of the United States?",
                             "Bald eagle""What is the largest planet in our solar system?", "Jupiter",
                             "Who painted the Mona Lisa?", "Leonardo da Vinci",
                             "What is the freezing point of water in Fahrenheit?", "32",
                             "What is the capital of France?", "Paris", "What is the world's largest desert?", "Sahara",
                             "What is the largest species of shark?", "Whale shark",
                             "Who is the author of the Harry Potter book series?", "J.K. Rowling",
                             "What is the largest continent by land area?", "Asia",
                             "What is the national flower of Japan?", "Cherry blossom",
                             "What is the speed of light in a vacuum?", "299,792 kilometers per second",
                             "What is the currency of Brazil?", "Brazilian real",
                             "What is the smallest planet in our solar system?", "Mercury",
                             "What is the world's longest river?", "Nile",
                             "Who is the first person to set foot on the moon?", "Neil Armstrong",
                             "What is the national animal of India?", "Bengal tiger",
                             "What is the highest grossing movie of all time?", "Avengers: Endgame",
                             "What is the largest waterfall by volume?", "Victoria Falls",
                             "Who is known as the 'Father of Evolution'?", "Charles Darwin",
                             "What is the world's tallest tree species?", "Coast redwood",
                             "What is the national sport of Canada?", "Ice hockey", "What is the largest land animal?",
                             "African elephant", "What is the smallest bone in the human body?", "Stapes (in the ear)",
                             "What is the world's highest mountain range?", "Himalayas",
                             "What is the national flower of the United States?", "Rose",
                             "What is the currency of China?", "Chinese yuan",
                             "What is the largest moon in our solar system?", "Ganymede",
                             "Who is the first woman to win a Nobel Prize?", "Marie Curie",
                             "What is the melting point of iron in Celsius?", "1538",
                             "What is the national bird of India?", "Indian peacock",
                             "What is the largest bird of prey?", "Andean condor",
                             "What is the world's largest coral reef system?", "Great Barrier Reef",
                             "Who is the artist of the famous painting 'The Starry Night'?", "Vincent van Gogh",
                             "What is the main component of air?", "Nitrogen",
                             "What is the world's largest hot desert?", "Sahara", "What is the capital of China?",
                             "Beijing", "What is the largest moon of Saturn?", "Titan",
                             "What is the fastest land animal?", "Cheetah", ]

question = kbc_questions_and_answers[0:len(kbc_questions_and_answers):2]
answer = kbc_questions_and_answers[1:len(kbc_questions_and_answers):2]
point = 0
for i in range(len(question)):
    print(question[i])
    ans = input("Answer please:")
    ans = ans.lower()
    answer[i] = answer[i].lower()
    if ans == answer[i]:
        point += 1
    else:
        print("Wrong Answer")
        break
print("Amount of money you bought is:", point * 1000, "$")
