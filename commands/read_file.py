import os
import click

@click.command(name="fread")
@click.option('--file', required=True, help='File to read.')
def command(file):
    """Simple to command to spool a file."""
    if not os.path.exists(file):
        click.echo(f"File '{file}' doest not exists!")
        return
    with open(file, mode='r') as file_stream:        
        [click.echo( line ) for line in file_stream]
            
