import click
import os

TRACKPADNAME="ETPS/2 Elantech Touchpad"
#TRACKPAD_COMMAND = "xinput disable 'SynPS/2 Synaptics TouchPad'"
TRACKPAD_COMMAND = "xinput disable '{}'".format(TRACKPADNAME)
#TOUCH_COMMAND = "xinput disable 'ELAN Touchscreen'"
TOUCHSCREENNAME="Wacom Pen and multitouch sensor Finger touch"
TOUCH_COMMAND = "xinput disable '{}'".format(TOUCHSCREENNAME)


@click.command('disable', short_help='Disable component.')
@click.argument('component', default='all', type=click.Choice(['trackpad', 'touch', 'all']))
def cli(component):
    exit_code = 0
    if component in ['trackpad', 'all']:
        exit_code = os.system(TRACKPAD_COMMAND)

    if exit_code == 0 and component in ['touch', 'all']:
        exit_code = os.system(TOUCH_COMMAND)

    return exit_code
