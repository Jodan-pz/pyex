import click


@click.command(name="hello")
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def command(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    [click.echo(f'Hello {name}!') for x in range(count)]
