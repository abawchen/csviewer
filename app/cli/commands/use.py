import click

# @click.group(invoke_without_command=True)
# @click.group()
# @click.pass_context
@click.command('use', short_help='Initializes a repo.')
def cli():
    """Initializes a repository."""
    # if ctx.invoked_subcommand is None:
    click.echo('I was invoked without subcommand')
    #else:
    #    click.echo('I am about to invoke %s' % ctx.invoked_subcommand)

'''
@cli.command()
@click.pass_context
def use(ctx):
    click.echo('The subcommand')

if __name__ == '__main__':
    cli(obj={})

'''
