import click

from giveme.gitignore import giveme as git_giveme

table = {
    'git': git_giveme
}


@click.group()
def cli():
    pass


@cli.command()
@click.option('--name', '-n', multiple=True)
@click.option('--system', '-s', default='macOS', help='macOs, Windows, Linux')
@click.option('--target', '-t', default='./.gitignore')
def git(name: list, system: str, target):
    git_giveme(name, system=system, target=target)


if __name__ == '__main__':

    cli()