from flask import Flask
from get_workday import *
app = Flask(__name__)

@app.route("/")
def hello():
    return "hello"

@app.route('/get_workday/<int:year>/<int:month>/<int:day>')
def get_workday(year:int, month: int, day: int):
    now = datetime.now()
    weekday = datetime(year, month, day).weekday() + 1
    with open('./HolidaySetting.json', 'r', encoding='utf8') as fp:
        json_data:dict = json.load(fp)
        try:
            monthCfg:list = json_data.get(str(year or now.year)).get(str(month or now.month))
            #不是周六周天，但是是节假日
            if (weekday != 6 and weekday != 7):
                if((day or now.day) in monthCfg.get("yes")):
                    return "False"
            #是周六周天，但是tm的要调休
            elif ((day or now.day) in monthCfg.get("no")):
                return "True"
            else:
                return "False"
        except Exception as e:
            return "True"
        return "True"

if __name__ == "__main__":
    # app.debug = False
    app.run()
