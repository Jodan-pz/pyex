from tasks import app

@app.task
def add_numbers(x: int, y : int):
    return x + y
