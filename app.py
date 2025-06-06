from flask import Flask, render_template, redirect, url_for, request, session
from fetchUsers import fetchUsers, insertUser
from fetchQuestions import getQuestionByTest, getTestName

app = Flask(__name__)
app.secret_key = '###secret_key###'

# Home Page route
@app.route('/')
def home():
  return render_template('home.html')

# Show Tests route
@app.route('/test/')
def test():
  if 'username' not in session:
    return redirect(url_for('login'))
  tests = getTestName()
  return render_template('test.html', tests = tests)

# Show the actual questions of the test. -- Questionnarie page
@app.route('/test/<tid>', methods = ['GET', 'POST'])
def showQuestions(tid):
  if 'username' in session:
    questions = getQuestionByTest(tid)
    if request.method == 'GET':
      return render_template('question.html', questions = questions, tid = tid)
    
    elif request.method == 'POST':
      results = {}
      score = 0

      correct_options = questions[0].correctAnswers(questions)
      for i, question in enumerate(questions):
        qid = question.qid
        key = f'option-{qid}'
        selected_options = request.form.getlist(key)

        is_correct = set(selected_options) == set(correct_options[i])
        if is_correct:
            score += 1

        results[qid] = {
          'question': question.question,
          'selected': selected_options,
          'correct': correct_options[i],
          'is_correct': is_correct
        }
      return render_template('result.html', results = results, score = score, tid = tid)
  else:
    return redirect(url_for('login'))

# Register route
@app.route('/register', methods = ['GET', 'POST'])
def register():
  if 'username' in session:
    return redirect(url_for('test'))
  usernameError = ''
  if request.method == 'GET':
    return render_template('register.html', usernameError=usernameError)
  
  elif request.method == 'POST':
    username = request.form.get('username')
    password = request.form.get('password')
    flUsers = fetchUsers()
    if username not in flUsers:
      session['username'] = username
      insertUser(username, password)
      return redirect(url_for('test'))
    else: 
      usernameError = 'User Name already taken or Already have an account'
      return render_template('register.html', usernameError=usernameError)


# Login route
@app.route('/login', methods = ['GET'])
def login():
  if 'username' in session:
    return redirect(url_for('test'))
  if 'try' not in session:
    session['try'] = 0

  if session['try'] < 3:
    error = False
    if session['try'] > 0:
      error = True
    return render_template('login.html', error = error)
  return redirect(url_for('failure'))

# Authentication route
@app.route('/authenticator', methods = ['POST'])
def authenticator():
  if 'username' in session:
    return redirect(url_for('test'))
  if 'try' in session and session['try'] < 3:
    username = request.form.get('username')
    password = request.form.get('password')
    flUsers = fetchUsers()
    if flUsers:
      if username in flUsers and password == flUsers[username]:
        session['username'] = username
        return redirect(url_for('test'))
    session['try'] += 1
    return redirect(url_for('login'))
  return redirect(url_for('login'))

# Failure Page route
@app.route('/failure')
def failure():
  if 'username' in session:
    return redirect(url_for('test'))
  if 'try' in session and session['try'] < 3:
    return redirect(url_for('login'))
  return render_template('failure.html')

# Logout route
@app.route('/logout')
def logout():
  session.pop('try', None)
  if 'username' in session:
    session.pop('username')
  return redirect(url_for('home'))

app.run(debug=True)