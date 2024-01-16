import socketio

sio_server = socketio.AsyncServer(
    async_mode='asgi',
    cors_allowed_origins=[]
)

sio_app = socketio.ASGIApp(
    socketio_server=sio_server,
    socketio_path='sockets'
)


@sio_server.event
async def connect(sid, environ, auth):
    username = auth.get('username', '')
    print(f'{sid}: connected')
    await sio_server.emit('join', {'sid': sid, 'username': username})


@sio_server.event
async def chat(sid, message, username):
    await sio_server.emit('chat', {'sid': sid, 'message': message, 'username': username})


@sio_server.event
async def disconnect(sid, username):
    print(f'{sid}: disconnected')
    await sio_server.emit('leave', {'sid': sid, 'username': username})