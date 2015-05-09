from app import app

from flask import jsonify, request

from app import pin

@app.route('/api/status', methods=['GET'])
def status():
    state = pin.status()
    return jsonify({
        'brewing': state,
    })

@app.route('/api/specs', methods=['GET'])
def specs():
    return jsonify({'status': 'fail', 'message': 'not implemented'})

@app.route('/api/brew', methods=['POST'])
def brew():
    j = request.get_json(force=True)
    if 'brewing' not in j:
        abort(400)
    pin.set_state(j['brewing'])
    return jsonify({ 'brewing': j['brewing'] })
