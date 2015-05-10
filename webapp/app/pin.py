import os

PIN = 17 # this needs to match the number in init_pin.sh

BASE = '/sys/class/gpio/gpio%d' % (PIN,)

def status():
    with open(os.path.join(BASE, 'value'), 'rt') as f:
        data = f.read().strip()
    if data == '0':
        return False
    elif data == '1':
        return True
    else:
        raise RuntimeError('unknown state %s' % data)

def set_state(value):
    v = '1' if bool(value) else '0'
    with open(os.path.join(BASE, 'value'), 'wt') as f:
        f.write(v)

def on():
    set_state(True)

def off():
    set_state(False)

def toggle():
    state = status()
    set_state(not state)
    return not state
