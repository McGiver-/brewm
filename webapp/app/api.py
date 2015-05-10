from app import app

from flask import jsonify, request
from threading import Timer

from app import pin, db

from datetime import datetime

_TIME_FMT = '%Y-%m-%dT%H:%M:%S%z'

@app.route('/api/status', methods=['GET'])
def status():
    state = pin.status()
    brew_time = db.load_default('brew_time', None)
    return jsonify({
        'brewing': state,
        'time': brew_time['time']
    })

@app.route('/api/specs', methods=['GET'])
def specs():
    return jsonify({ 'brewTime': 360 })

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
        app.BREW_TIMER = Timer(360.0, stop_brew)
        app.BREW_TIMER.start()

        t = datetime.now().strftime(_TIME_FMT)
        db.save('brew_time', {
            'time': t
        })
    else:
        db.delete('brew_time')

    return jsonify({
        'brewing': j['brewing'],
        'time': t
    })
