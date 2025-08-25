class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list




    def next_question(self,q_num,q_list):
        ans = True
        while ans:
            user_ans = input(f"Q.{q_num + 1}: {q_list[q_num].text}. (True/False)?:").title()
            if user_ans == q_list[q_num].answer:
                print(f"You got it right!\nThe correct answer was: {q_list[q_num].answer}."
                      f"\nYour current score is: {q_num + 1}/{q_num + 1}")
                print("\n")
                q_num += 1
                if q_num == 12:
                    print("You've completed the quiz")
                    ans = False

            else:
                print(f"That's wrong.\nThe correct answer was: {q_list[q_num].answer}"
                      f"\nYour final score is: {q_num}/{q_num + 1}")
                ans = False
