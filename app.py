from flask import Flask, render_template, request, redirect
from flask_socketio import SocketIO
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET'] = ')ZnNk7hluN7OBejlct#WgV5d65uTABT73rQwZjj(XQl#Q8s1CM(N@^#WsdJl'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# mqtt = Mqtt(app)
socketio = SocketIO(app)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)


class MqttServers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_address = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return "<ID %r>" % self.id_address


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        server_id = request.get_json()
        print(server_id)
        '''new_server = MqttServers(id_address=server_id)

        try:
            db.session.add(new_server)
            db.session.commit()
            return redirect('/')
        except:
            return "Sorry, error" '''

    return render_template('index.html')


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, use_reloader=False, debug=True)
