from flask import Flask

app = Flask(__name__)

@app.route('/get_workday')
def get_workday():
    return "Hello World"

if __name__ == "__main__":
    app.run()


from datetime import datetime
datetime.now().year