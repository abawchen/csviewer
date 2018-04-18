#!/usr/bin/env python

import click
import os
import sys

plugin_folder = os.path.join(os.path.dirname(__file__), 'commands')

class MyCLI(click.MultiCommand):

    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(plugin_folder):
            if filename.endswith('.py'):
                rv.append(filename[:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        '''
        ns = {}
        fn = os.path.join(plugin_folder, name + '.py')
        print(fn)
        with open(fn) as f:
            code = compile(f.read(), fn, 'exec')
            eval(code, ns, ns)
        return ns['cli']
        '''
        try:
            if sys.version_info[0] == 2:
                name = name.encode('ascii', 'replace')
            mod = __import__('commands.' + name,
                             None, None, ['cli'])
        except ImportError:
            return
        return mod.cli


cli = MyCLI(help='This tool\'s subcommands are loaded from a plugin folder dynamically.')

# if __name__ == '__main__':
#     cli(obj={})

'''
@click.command(cls=MyCLI)
# @click.pass_context
def cli():
    """A complex command line interface."""
    pass
'''
if __name__ == '__main__':
    cli(obj={})

