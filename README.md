# devcade-website
Front-end for the Devcade website that allows members to view the game catalog and upload games.

# How to Run
`pip3 install -r requirements.txt`

`cd src`

`flask run`

# Project Structure

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
| config.py         // Environ variable loaders
| init.py           // Initialization for flask project
| models.py         // User model
```