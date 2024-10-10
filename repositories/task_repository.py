from models.task import Task, db

class TaskRepository:

    @staticmethod
    def create_task(name, description):
        task = Task(name=name, description=description)
        db.session.add(task)
        db.session.commit()
        return task

    @staticmethod
    def get_all_task():
        tasks = Task.query.all()
        return tasks

    @staticmethod
    def update_task(task, name, description):
        task.name = name
        task.description = description
        db.session.commit()
        return task

    @staticmethod
    def get_task_by_id(task_id):
        tasks = Task.query.get(task_id)
        return tasks