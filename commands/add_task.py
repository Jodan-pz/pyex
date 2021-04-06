from task.add import add_numbers
import click


@click.command(name="add-task")
@click.option('--first', default=1, required=True, help='First number to add.')
@click.option('--second', default=2, required=True, help='Second number to add.')
def command(first, second):    
    """Simple celery task."""
    add_numbers.delay (first, second)
