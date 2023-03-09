# devcade-website
Front-end for the Devcade website that allows members to view the game catalog and upload games.

# How to Run
`pip3 install -r requirements.txt`

`cd src`

`flask run`

# Project Structure
This project follows a standard template for a Flask project. Below is the basic file structure of the project, with every file described other than those in the `static/` folder (for brevity).

```
devcade-website
| src/
| | static/         // Static content (images, css, js)
| | templates/      // Header and content templates
| | | header.html   // Includes game block macro and header block macro
| | | game.html     // Game focus page
| | | catalog.html  // Game catalog page
| | | credits.html  // Game credits page (using game blocks)
| | | error.html    // Error page
| | | home.html     // Main page, includes project details
| | | upload.html   // Game upload page, including instructions
| | | profile.html  // User profile -- not implemented
| app.py            // Main file
| auth.py           // Helper functions for handling CSH auth
| config.py         // Environment variable getters
| init.py           // Initialization for flask project
| models.py         // User model
| envs.py           // Environment variable setters (Follows template described in Local Development section)
```

# Local Development
If you would like to run this project using your local machine, first create a `envs.py` file with the following structure:

```
import os

os.environ['SERVER_NAME'] = ''
os.environ['PREFERRED_URL_SCHEME'] = ''
os.environ["OIDC_CLIENT_SECRET"] = ""
os.environ["DEVCADE_DB_PORT"] = ""
os.environ["DEVCADE_DB_NAME"] = ""
os.environ["DEVCADE_DB_USER"] = ""
os.environ["DEVCADE_DB_PASS"] = ""
os.environ["DEVCADE_DB_URI"] = ""
os.environ["DEVCADE_API_URI"] = ""
```

Note that this is just a template for the `envs.py` file. You will need to get these secrets from an RTP or Devcade developer.