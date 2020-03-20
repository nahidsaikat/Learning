import click


@click.command()
@click.option('--count', default=1, help='Number of greetings.')
def hello(count):
    """Simple program that prints Hello World for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello World')

if __name__ == '__main__':
    hello()

