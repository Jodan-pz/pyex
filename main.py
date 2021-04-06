from commands import hello, read_file
import click

@click.group()
def cli():
    pass

cli.add_command(hello.command)
cli.add_command(read_file.command)

if __name__ == '__main__':
    cli()