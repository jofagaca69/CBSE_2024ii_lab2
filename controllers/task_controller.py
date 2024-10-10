from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from services.task_service import TaskService

task_blueprint = Blueprint('tasks', __name__)

@task_blueprint.route('/tasks', methods=['POST'])
def create_task():

    data = request.form
    name = data.get('name')
    description = data.get('description')

    if not name:
        return jsonify({'error': 'Name is required'}), 400

    TaskService.create_task(name, description)
    return redirect(url_for('tasks.index'))

@task_blueprint.route('/update_task', methods=['POST']) 
def update_task():
    data = request.form
    task_id = data.get('id_update')
    name = data.get('name_update')
    description = data.get('description_update')

    if not task_id:
        return jsonify({'error': 'Task id is required'}), 400

    task = TaskService.update_task(task_id, name, description)
    return redirect(url_for('tasks.index'))

@task_blueprint.route('/')
def index():
    tasks = TaskService.get_all_tasks()
    return render_template('index.html', tasks=tasks)