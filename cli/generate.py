import shutil
import sys
from pathlib import Path

import click

from cli import constants

base_requirements = '''
bs4
checklib
dnslib
flask
gevent
gmpy2
gunicorn
lxml
numpy
pwntools
pycryptodome
pydantic
regex
requests
'''


@click.command(help='Generate a server from a function')
@click.option(
    '-s', '--src',
    type=str,
    help='File with decode function',
    required=True,
    prompt='Enter path to the decoder file',
)
@click.option(
    '-r', '--reqs',
    type=str,
    help='File with additional requirements (optional)',
    required=False,
)
def generate(src, reqs):
    requirements = base_requirements
    if reqs is not None:
        requirements += Path(reqs).read_text()
    constants.SERVICE_REQUIREMENTS.write_text(requirements.strip())

    shutil.copy2(src, constants.GENERATED_PATH)
    shutil.copy2(constants.MODELS_SRC, constants.MODELS_DST)

    try:
        from service.generated import decode
    except ImportError:
        print('Invalid decoder module, could not import "decode" function')
        sys.exit(1)


generate: click.Command  # noqa
