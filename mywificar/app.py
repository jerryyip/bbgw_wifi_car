#!/usr/bin/env python


import time
from mywificar import goFront, goBack, stop, turnRight, turnLeft
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect
async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None

def background_thread(): 
     """Example of how to send server generated events to clients.""" 
     count = 0 
     while True: 
         socketio.sleep(10) 
         count += 1 
         socketio.emit('my_response', 
                       {'data': 'Server generated event', 'count': count}, 
                       namespace='/test') 


@app.route('/')
def index():
    return render_template('index.html',async_mode=socketio.async_mode)

@socketio.on('my_event', namespace='/test')
def test_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': message['data'], 'count': session['receive_count']})

@socketio.on('connect', namespace='/test')
def test_connect():
    global thread
    if thread is None:
        thread = socketio.start_background_task(target=background_thread)
    emit('my_response', {'data': 'Connected', 'count': 0})


@socketio.on('front_event', namespace='/test')
def add_message():
    session['receive_count'] = session.get('receive_count', 0) + 1
    print("go front")
    goFront()
    emit('my response',{'data': "go front" , 'count': session['receive_count']})

@socketio.on('left_event', namespace='/test')
def left_message():
    session['receive_count'] = session.get('receive_count', 0) + 1
    print("turn left")
    turnLeft()
    emit('my response',{'data': "turn left" , 'count': session['receive_count']})
    
@socketio.on('back_event', namespace='/test')
def back_message():
    session['receive_count'] = session.get('receive_count', 0) + 1
    print("go back")
    goBack()
    emit('my response',{'data': "go back" , 'count': session['receive_count']})
    
@socketio.on('right_event', namespace='/test')
def right_message():
    session['receive_count'] = session.get('receive_count', 0) + 1
    print("turn right")
    turnRight()
    emit('my response',{'data': "turn right" , 'count': session['receive_count']})

@socketio.on('reset_event', namespace='/test')
def stop_message():
    session['receive_count'] = session.get('receive_count', 0) + 1
    print("reset")
    stop()
    emit('my response',{'data': "reset" , 'count': session['receive_count']})
    
if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0', debug=False)
