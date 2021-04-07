from commands import hello, read_file, add_task
import click

@click.group()
def cli():
    pass


cli.add_command(hello.command)
cli.add_command(read_file.command)
cli.add_command(add_task.command)

if __name__ == '__main__':
    cli()
