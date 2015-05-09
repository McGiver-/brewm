import os

PIN = 17 # this needs to match the number in init_pin.sh

BASE = '/sys/class/gpio/gpio%d' % (PIN,)

def status():
    with open(os.path.join(BASE, 'direction'), 'rt') as f:
        data = f.read().strip()
    if data == 'in':
        return False
    elif data == 'out':
        return True
    else:
        raise RuntimeError('unknown state %s' % data)

def set_state(value):
    v = 'out' if bool(value) else 'in'
    with open(os.path.join(BASE, 'direction'), 'wt') as f:
        f.write(v)

def on():
    set_state(True)

def off():
    set_state(False)

def toggle():
    state = status()
    set_state(not state)
    return not state
