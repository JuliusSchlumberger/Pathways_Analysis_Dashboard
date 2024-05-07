from dash import Dash, html
import flask
import json
import uuid

app = Dash(__name__)
app.server.secret_key = 'your_secret_key_here'  # Set a secret key for session handling
server = app.server


@server.route('/save_viewport_size', methods=['POST'])
def save_viewport_size():
    print("Session ID from Flask session:", flask.session.get('session_id'))

    if 'session_id' not in flask.session:
        flask.session['session_id'] = str(uuid.uuid4())  # Ensure a session ID is assigned
        print("New session ID generated:", flask.session['session_id'])

    session_id = flask.session['session_id']
    data = flask.request.json
    print("Received data:", data)

    if data is None:
        return flask.jsonify({"status": "error", "message": "No data received"}), 400

    filename = f'screen_dimensions/viewport_sizes_{session_id}.json'
    with open(filename, 'w') as f:
        json.dump(data, f)

    return flask.jsonify({"status": "success"})


if __name__ == '__main__':
    app.run_server(debug=True)
