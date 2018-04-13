import os
import click
import subprocess


class ViewerClient(object):

    @click.group(chain=True)
    @click.pass_context
    def cli(ctx):
        pass

    
    @cli.command()
    @click.argument('filename')
    def view(filename):
        # TODO: Set PAGER in a proper place.
        os.environ['PAGER'] = 'LESS -S'
        cmd = 'head -n 3 {} | column -t -s, | less -S'.format(filename)
        process = subprocess.Popen(
            cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()
        out_string = out.decode()
        lines = out_string.splitlines()
        click.echo_via_pager("\n".join(lines))
