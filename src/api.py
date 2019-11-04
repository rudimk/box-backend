from sanic import Sanic
from sanic.response import json
from db.config import db

app = Sanic()


## Define endpoints for manipulating credentials.

# GET /credentials
@app.get('/credentials')
async def getCredentials(request):
	credentials = db.table('credentials').get()
	return json(credentials)


# GET /credentials/<credential_id>
@app.get('/credentials/<credential_id>')
async def getCredentialByID(request, credential_id):
	credential = db.table('credentials').where('id', int(credential_id)).first()
	return json(credential)


# POST /credentials
@app.post('/credentials')
async def createCredentials(request):
	credentials = request.json
	newCredentials = db.table('credentials').insert_get_id(credentials)
	return json({'success': True, 'id': newCredentials})




if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8888)