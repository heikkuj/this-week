from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = ['test1', 'test2', 'test3']


@app.route('/index')
def index():
    return render_template('index.html',
                           mssg='Good morning!',
                           tasks=tasks)

# add new tasks to todo-list
@app.route('/add', methods=['POST'])
def add_task():
    new_task = request.form.get('newTask')
    if new_task:
        tasks.append(new_task)
    return redirect(url_for('index'))

@app.route('/complete', methods=['POST'])
def complete_tasks():
    completed_tasks = request.form.getlist('taskCheckbox')
    for index in map(int, completed_tasks):
        if 1 <= index <= len(tasks):
            tasks[index - 1] += " - Completed"
    return redirect(url_for('index'))

@app.route('/login')
def login():
    return render_template('login.html')



if __name__ == '__main__':
    app.run()
