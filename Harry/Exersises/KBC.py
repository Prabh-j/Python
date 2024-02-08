f = 0
a = 0
x = 1
questions = ['1. What is the capital city of France?\nA) Berlin\nB) London\nC) Paris\nD) Madrid', '2. Who wrote the play "Romeo and Juliet"?\nA) William Shakespeare\nB) Charles Dickens\nC) Jane Austen\nD) Leo Tolstoy',  '3. Which planet is known as the "Red Planet"?\nA) Venus\nB) Mars\nC) Jupiter\nD) Saturn', '4. What is the largest mammal in the world?\nA) Elephant\nB) Giraffe\nC) Blue Whale\nD) Polar Bear', '5. Who is the author of "To Kill a Mockingbird"?\nA) F. Scott Fitzgerald\nB) Harper Lee\nC) Mark Twain\nD) J.K. Rowling',  '6. Which gas do plants absorb from the atmosphere during photosynthesis?\nA) Oxygen\nB) Carbon dioxide\nC) Nitrogen\nD) Hydrogen', '7. Which country is known as the Land of the Rising Sun?\nA) China\nB) India\nC) Japan\nD) South Korea', '8. What is the chemical symbol for gold?\nA) Go\nB) Ag\nC) Gd\nD) Au', '9. Who is the current President of the United States?\nA) Joe Biden\nB) Donald Trump\nC) Barack Obama\nD) George W. Bush', '10. What is the largest ocean in the world?\nA) Indian Ocean\nB) Atlantic Ocean\nC) Pacific Ocean\nD) Arctic Ocean', '11. Which famous scientist formulated the laws of motion and universal\nA) Albert Einstein\nB) Galileo Galilei\nC) Isaac Newton\nD) Charles Darwin', '12. What is the smallest prime number?\nA) 0\nB) 1\nC) 2\nD) 3', '13. In which year did Christopher Columbus first voyage to the Americas?\nA) 1492\nB) 1520\nC) 1607\nD) 1776', "14. Which gas makes up the majority of Earth's atmosphere?\nA) Oxygen\nB) Carbon dioxide\nC) Nitrogen\nD) Hydrogen"]
answers = ['C', 'A', 'B', 'C', 'B', 'B', 'C', 'D', 'A', 'C', 'C', 'C', 'A', 'C']
for question in questions:
    print(question)
    yanswer = input('Your Answer: ').capitalize()
    if yanswer == answers[a]:
        print('Correct Answer')
        f = (f*2) +(5000*x)
        a+=1
        x=0
    else:
        print('Wrong Answer')
        print('Correct Answer is', answers[a])
        print('Your Total Winning is',f,'rupees')
        break

 