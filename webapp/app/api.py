from app import app

from flask import jsonify, request
from threading import Timer

from app import pin, db

import datetime

_TIME_FMT = '%Y-%m-%dT%H:%M:%S'
TIME = 360.0

def remaining_time():
    start_time = db.load_default('brew_time', None)
    if start_time is None:
        return None
    elapsed = datetime.datetime.now() - datetime.datetime.strptime(
            start_time['time'], _TIME_FMT)
    remaining = TIME - elapsed.total_seconds()
    return remaining

@app.route('/api/status', methods=['GET'])
def status():
    state = pin.status()
    brew_time = remaining_time()
    return jsonify({
        'brewing': state,
        'time': brew_time
    })

@app.route('/api/specs', methods=['GET'])
def specs():
    return jsonify({ 'brewTime': TIME })

def stop_brew():
    pin.set_state(False)
    app.BREW_TIMER = None

@app.route('/api/brew', methods=['POST'])
def brew():
    j = request.get_json(True)
    if 'brewing' not in j:
        abort(400)
    pin.set_state(j['brewing'])

    t = None

    if app.BREW_TIMER is not None:
        app.BREW_TIMER.cancel()

    if j['brewing']:
        app.BREW_TIMER = Timer(TIME, stop_brew)
        app.BREW_TIMER.start()

        t = datetime.datetime.now().strftime(_TIME_FMT)
        db.save('brew_time', {
            'time': t
        })
        t = 360.0
    else:
        db.delete('brew_time')

    return jsonify({
        'brewing': j['brewing'],
        'time': t
    })
