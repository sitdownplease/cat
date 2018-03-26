from flask import Flask, request, abort
import json
import requests

app = Flask(__name__)

@app.route('/callback',methods=['POST'])
def callback():
    json_line = request.get_json()
    json_line = json.dumps(json_line)
    decoded = json.loads(json_line)
    user = decoded['result'][0]['content']['from']
    text = decoded['result'][0]['content']['text']
    sendText(user,text)
    return ''

def sendText(user, text):
    LINE_API = ''
    CHANNEL_ID = ''
    CHANNEL_SERECT = ''
    MID = ''

    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'X-Line-ChannelID': CHANNEL_ID,
        'X-Line-ChannelSecret': CHANNEL_SERECT,
        'X-Line-Trusted-User-With-ACL': MID
    }

    data = json.dumps({
        "to":[user],
        "toChannel":0,
        "eventType":"０",
        "content":{
            "contentType":1,
            "toType":1,
            "text":text
        }
    })

    r = requests.post(LINE_API, headers=headers, data=data)
    print(r.text)