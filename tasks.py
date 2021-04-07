from celery import Celery

app = Celery('tasks', broker='redis://localhost', include=['task.add'])
