import sqlite3

class Question:
  def __init__(self, qid, question, option1, option2, option3, option4, answer):
    self.qid = qid
    self.question = question
    self.option1 = option1
    self.option2 = option2
    self.option3 = option3
    self.option4 = option4
    self.answer = answer   

  def correctAnswers(self, questions):
    correctOptions = []
    for question in questions:
      correctAnswer = question.answer.split('-')
      correctOption = [str(i + 1) for i, val in enumerate(correctAnswer) if val == '1']
      correctOptions.append(correctOption)
    return correctOptions
  
def getQuestionByTest(qid):
  db = sqlite3.connect('dbs/exam.db')
  cur = db.cursor()
  cur.execute('select * from question where qid in (select qid from testpaper where tid = ?)', (qid, ))
  rows = cur.fetchall()

  db.commit()
  db.close()

  questions = []

  if rows:
    for row in rows:
      question = Question(
        qid=row[0],
        question=row[1],
        option1=row[2],
        option2=row[3],
        option3=row[4],
        option4=row[5],
        answer=row[6]
      )
      questions.append(question)
  return questions
  
class Test:
  def __init__(self, testId, testName, testCreated, testCreator):
    self.testId = testId
    self.testName = testName
    self.testCreated = testCreated
    self.testCreator = testCreator

def getTestName():
  db = sqlite3.connect('dbs/exam.db')
  cur = db.cursor()
  cur.execute('select * from test')
  tests = []
  rows = cur.fetchall()
  db.commit()
  db.close()

  if rows:
    for row in rows:
      test = Test(
        testId = row[0],
        testName=row[1],
        testCreated=row[2],
        testCreator=row[3]
      )
      tests.append(test)
  return tests
