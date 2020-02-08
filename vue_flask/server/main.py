from flask import Flask, render_template
from api import api_bp
from models import get_all, init_db, insert

app = Flask(__name__, static_folder='../frontend/dist/static', template_folder='../frontend/dist')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myspa.db'
app.register_blueprint(api_bp)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield b'--frame\r\n' + b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n'
        sleep(0.33)

@app.route('/video')
def video():
    camera = LifeGameCamera()
    return Response(gen(camera), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    with app.app_context():
        init_db(app)
        if not get_all():
            insert('foo', 'This is foo.')
            insert('bar', 'This is bar.')
    app.run()