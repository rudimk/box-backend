from sanic import Sanic
from sanic.response import json
from sanic_cors import CORS
from db.config import db

app = Sanic()
CORS(app, automatic_options=True)

## Define endpoints for manipulating credentials.

# GET /credentials
@app.get('/credentials')
async def getCredentials(request):
	credentials = db.table('credentials').get()
	return json({'data': credentials, 'total': len(credentials)})


# GET /credentials/<credential_id>
@app.get('/credentials/<credential_id>')
async def getCredentialByID(request, credential_id):
	credential = db.table('credentials').where('id', int(credential_id)).first()
	return json({'data': credential})


# POST /credentials
@app.post('/credentials')
async def createCredentials(request):
	credentials = request.json
	newCredentialID = db.table('credentials').insert_get_id(credentials)
	newCredential = db.table('credentials').where('id', newCredentialID).first()
	return json({'data': newCredential})


# PUT /credentials/<credential_id>
@app.put('/credentials/<credential_id>')
async def modifyCredentialbyID(request, credential_id):
	updateBody = request.json
	updatedCredentialStatus = db.table('credentials').where('id', int(credential_id)).update(updateBody)
	updatedCredential = db.table('credentials').where('id', int(credential_id)).first()
	return json({'data': updatedCredential})


# DELETE /credentials/<credential_id>
@app.delete('/credentials/<credential_id>')
async def deleteCredentialsByID(request, credential_id):
	deleteCredentials = db.table('credentials').where('id', int(credential_id)).delete()
	return json({'data': None})


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8888)