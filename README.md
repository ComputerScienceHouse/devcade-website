# Devcade Website

The front-end website for learning about the Devcade project, viewing the list of games, uploading new games, and editing existing games.

## Local Development
In order to run it locally, you will need to install [node](https://nodejs.org/en/).


### Setup with npm

Before running the project, you will need to install dependencies. This can be done by running the following command from within the project directory.
Note: It may take some time to install all dependencies.

```
npm install
```

### Run in development

```
npm start
```

In order to run locally, you're going to need an OIDC client, by default there's a `.env` file which defines all variables you don't want to commit to the repo directly. The default SSO variables will work for development purposes. 
<!-- It will only work on `http://localhost:3000`. -->
For more information on CSH SSO, and getting an OIDC client, talk to an RTP.


All variables need to be prepended with `REACT_APP_`

___

## Help! I don't have a CSH account or I dont want to secure the website in development!

No problem! You can disable SSO in `configuration.ts` by changing `SSOEnabled` to `'false'`, or alternatively, you can set the `REACT_APP_SSO_ENABLED` variable to false.