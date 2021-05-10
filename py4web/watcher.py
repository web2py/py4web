import urllib3
import json
import asyncio
from watchgod import awatch
import os
import click


HTTP = urllib3.PoolManager()


class Params:
    host_port = None
    cli_key = None
    apps_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '../apps'))


def watch(apps_folder):
    def watch_folder_event_loop(apps_folder):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(watch_folder(apps_folder))

    async def watch_folder(apps_folder):
        async for changes in awatch(os.path.join(apps_folder)):
            notify(changes)

    watch_folder_event_loop(apps_folder)


def notify(changes):
    changes = {'$args': [list(changes)]}
    changes = json.dumps(changes).encode('utf-8')
    HTTP.request(
        'POST',
        f'http://{Params.host_port}/py4web_cli/track_changes',
        body = changes,
        headers = {
            'Content-Type': 'application/json',
            'X-Py4web-Cli-Key': Params.cli_key
        }
    )


@click.command()
@click.option("-H", "--host", default="127.0.0.1", help="Host name", show_default=True)
@click.option(
    "-P", "--port", default=8000, type=int, help="Port number", show_default=True
)
@click.option(
    "--apps", default=Params.apps_folder, help="Apps folder", show_default=True
)
@click.argument('cli_key')
def run(host, port, apps, cli_key):
    Params.host_port = f'{host}:{port}'
    Params.cli_key = cli_key
    Params.apps_folder = apps
    watch(Params.apps_folder)

if __name__ == '__main__':
    run()
