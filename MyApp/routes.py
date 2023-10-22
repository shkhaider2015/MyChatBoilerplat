from flask import current_app as app
from MyApp import a





##decorator
@app.route('/')
def home():
    return ({
        'message': 'Success'
    })

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@app.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    app.emit('my response', json, callback=messageReceived)
