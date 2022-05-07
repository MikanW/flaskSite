from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>烤鞋底子都好吃系列食谱（缓慢施工中）</h1><div><ul><li><a href="static/cookBook/swtPttCrnTrt.html">红薯玉米挞</a></li></ul></div></footer>'