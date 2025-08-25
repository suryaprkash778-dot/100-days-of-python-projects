from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    q_text = question["text"]
    q_answer = question["answer"]
    ques = Question(q_text,q_answer)
    question_bank.append(ques)

quiz = QuizBrain(question_bank)
quiz.next_question(0,question_bank)
