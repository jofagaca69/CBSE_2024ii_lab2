from repositories.task_repository import TaskRepository

class TaskService:

    @staticmethod
    def create_task(name, description):
        return TaskRepository.create_task(name, description)

    @staticmethod
    def get_all_tasks():
        return TaskRepository.get_all_task()

    @staticmethod
    def update_task(task_id, name, description):
        task = TaskRepository.get_task_by_id(task_id)
        if task:
            if name and description:
                return TaskRepository.update_task(task, name, description)
            if name:
                return TaskRepository.update_task(task, name, task.description)
            if description:
                return TaskRepository.update_task(task, task.name, description)
        return None