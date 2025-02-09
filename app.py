from flask import Flask, render_template, request, jsonify, redirect, url_for
import os
import json
from datetime import datetime

app = Flask(__name__)

# タスクデータを保存するファイル
DATA_FILE = os.path.join('data', 'tasks.json')

# タスクデータを読み込む関数
def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

# タスクデータを保存する関数
def save_tasks(tasks):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)

@app.route('/')
def index():
    tasks = load_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    tasks = load_tasks()
    new_task = {
        'id': len(tasks) + 1,
        'title': request.form['title'],
        'description': request.form.get('description', ''),
        'due_date': request.form.get('due_date', ''),
        'tags': request.form.get('tags', '').split(','),
        'completed': False
    }
    tasks.append(new_task)
    save_tasks(tasks)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>', methods=['POST'])
def edit_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            data = request.get_json()  # JSON データを取得
            task['title'] = data['title']
            task['description'] = data.get('description', '')
            task['due_date'] = data.get('due_date', '')
            task['tags'] = data.get('tags', '').split(',')
            break
    save_tasks(tasks)
    return redirect(url_for('index'))


@app.route('/toggle/<int:task_id>', methods=['POST'])
def toggle_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = not task['completed']
            break
    save_tasks(tasks)
    return redirect(url_for('index'))

if __name__ == '__main__':
    os.makedirs('data', exist_ok=True)
    app.run(debug=True)