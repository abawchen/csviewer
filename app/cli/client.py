import click


class ViewerClient(object):

    @click.group(chain=True)
    @click.pass_context
    def cli(ctx):
        pass

    
    @cli.command()
    @click.argument('filenam')
    def view(filename):
        click.echo(filename)

    
