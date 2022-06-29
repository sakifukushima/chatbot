from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <h1>Hello I'm Saki!</h1>
    <img src="https://i.etsystatic.com/33728303/r/il/239341/3579213608/il_1588xN.3579213608_re6w.jpg" alt="Test">
    '''

if __name__ == '__main__':
    app.run(debug=True)