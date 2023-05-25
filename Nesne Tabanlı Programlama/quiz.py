

class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    def checkAnswer(self, answer):
        return self.answer == answer 
        
"""
        
q1 = Question('Hangi şehir ege bölgesinde değildir?', ['Denizli','İzmir','Ankara','Muğla'], 'Ankara')

q2 = Question('Hangi şehir karadeniz bölgesinde değildir?', ['Rize','İzmir','Trobzon','Sinop'], 'İzmir')
              
q3 = Question('Hangi şehir Marmara bölgesinde bulunur?', ['İstanbul','İzmir','Ankara','Muğla'], 'İstanbul')


# """

# print("""
#       1.Soru: Hangi şehir ege bölgesinde değildir?
#         Denizli, İzmir, Ankara, Muğla
#       2.Soru: Hangi şehir karadeniz bölgesinde değildir?
#         Rize, İzmir, Trobzon, Sinop
#       3.Soru: Hangi şehir Marmara bölgesinde bulunur?
#         İstanbul, İzmir, Ankara, Muğla
#       """)
"""
answer1 = str(input('1.Soru için cevabınız?: '))
answer2 = str(input('2.Soru için cevabınız?: '))
answer3 = str(input('3.Soru için cevabınız?: '))

print(q1.checkAnswer(answer1))

print(q2.checkAnswer(answer2))

print(q3.checkAnswer(answer3))

"""

# Quiz

class Quiz:
  def __init__(self, questions):
    self.questions = questions
    self.score = 0
    self.questionIndex = 0 
    
  def getQuestions(self):
    return self.questions[self.questionIndex]
  
  def displayQuestion(self):
    question = self.getQuestions()
    print(f'Soru {self.questionIndex + 1}: {question.text}')
    
    for q in question.choices:
      print('-' + q)
    
    answer = input('Cevap?: ')
    self.guess(answer)
    self.loadQuestion()
    
  def guess(self, answer):
    question = self.getQuestions()
    
    if question.checkAnswer(answer):
      self.score += 1
      self.questionIndex += 1
    
    else:
      self.questionIndex += 1
      self.score -= 1
      
  def loadQuestion(self):
    if len(self.questions) == self.questionIndex:
      self.showScore()
    else:
      self.displayProgress()
      self.displayQuestion()
      
  def showScore(self):
    print(f'Punınız: {self.score}')
    
  def displayProgress(self):
    totalQuestion = len(self.questions)
    questionNumber = self.questionIndex + 1
    
    if questionNumber > totalQuestion:
      print('Daha Fazla Quiz Yok')
    else:
      print(f'{questionNumber}/{totalQuestion}'.center(100, '*'))
q1 = Question('Hangi şehir ege bölgesinde değildir?', ['Denizli','İzmir','Ankara','Muğla'], 'Ankara')
q2 = Question('Hangi şehir karadeniz bölgesinde değildir?', ['Rize','İzmir','Trobzon','Sinop'], 'İzmir')           
q3 = Question('Hangi şehir Marmara bölgesinde bulunur?', ['İstanbul','İzmir','Ankara','Muğla'], 'İstanbul')
questions = [q1, q2, q3]

quiz = Quiz(questions)

quiz.loadQuestion()

 