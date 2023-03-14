# API

- Download project and run `npm install`
- Use `npm run dev` to start the development server.
- If a `.env` file does not currently exist in the repo root directory, create one with:
```
# Express API Environment Variables
API_PORT=<api port>

PSQL_PORT=<psql port>
PSQL_USER=<psql user>
PSQL_PASS=<psql password>
PSQL_URI=<psql uri>

# Python Helper Environment Variables
S3_ACCESSKEYID=<aws s3 access key id>
S3_SECRETACCESSKEY=<aws s3 secret access key>
S3_ENDPOINT=<s3 endpoint uri>
S3_GAMES_BUCKET="devcade-games"
S3_SAVES_BUCKET="devcade-saves"
```

# Podman

First, build the container.
```
podman build . --tag devcade-api
```

You can run the container on your local machine with
```
podman run --rm -it --name devcade-api -p 8277:8277 --env-file=.env devcade-api
```

# API GET Routes

## Downloading A Game
- Route: `api/games/download/<existingGameId>`	
- Downloads a game zip containing a single game directory
	
```javascript
/// Sample Usage in JavaScript using Axios
	
const axios = require('axios');
	
axios.get(`<api_url>:<port>/api/games/download/${<existingGameId>}`)
	.then(res => {
		// response logic
	}).catch(err => {
		console.log(err);
	});
```

## Downloading A Game's Icon and Banner
- Route: `api/games/download/medias/<existingGameId>`
- Downloads a zip containing the banner and icon images for a game
	
```javascript
/// Sample Usage in JavaScript using Axios
	
const axios = require('axios');
	
axios.get(`<api_url>:<port>/api/games/download/medias/${<existingGameId>}`)
	.then(res => {
		// response logic
	}).catch(err => {
		console.log(err);
	});
```

## Get Available Games List

### Getting Game Objects
- Route: `api/games/gamelist`	
- Returns a JSON list containing the following object:
	
```javascript
{
	"id": "<game uuid>",
	"author": "<CSH username of author>",
	"uploadDate": "<date string of upload date>",
	"name": "<game title>",
	"hash": "<hash value of game files used for game versioning>"
}
```
	
- This list can be deserialized using the Newtonsoft.Json nuget library in C#/.NET	

```
/// Sample Usage in JavaScript using Axios
	
const axios = require('axios');
	
axios.get('<api_url>:<port>/api/games/gamelist')
	.then(res => {
		// response logic
	}).catch(err => {
		console.log(err);
	});
```

### Listing Game Ids
- Route: `api/games/gamelist/ids`
- Returns a JSON list containing game uuid strings
	
```javascript
/// Sample Usage in JavaScript using Axios
	
const axios = require('axios');
	
axios.get('<api_url>:<port>/api/games/gamelist/ids')
	.then(res => {
		// response logic
	}).catch(err => {
		console.log(err);
	});
```

# API POST Routes

## Uploading A Game
- Route: `api/games/upload`	
- Takes a game zip and uploads it to the database
	
```javascript
/// Sample Usage in JavaScript using Axios

const fs = require('fs');
const axios = require('axios');
const FormData = require('form-data');

const upload = async () => {
	try {
		const file = fs.createReadStream('./zip.zip');
		const title = 'GameName';

		const form = new FormData();
		form.append('title', title);
		form.append('file', file);

			const response = await axios.post(
				'<api_url>:<port>/api/games/upload', 
				form, 
				{ headers: { ...form.getHeaders(), }
		})
			if (response.status === 200) {
			return 'Upload complete';        
		}
	} catch (err) {
		throw err;
	}
}
```