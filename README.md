# Lyrics Translation Web App

Welcome to our lyrics translation web app, built with HTML, CSS, and Python (Flask). This app uses the [Genius API](https://docs.genius.com/) to retrieve lyrics and the [Translators API](https://pypi.org/project/translators/) to translate them into Spanish.

### You can try it out live [here](https://lyrics-translate-web-app.onrender.com).

## Running the app locally

To run this app locally, you will need to have Docker and Docker Compose installed. You will also need to set up a Genius API account and obtain an access token from [here](https://genius.com/api-clients).

1. Clone the repository to your local machine
2. Navigate to the root directory of the project and run docker-compose up
3. The app should now be running on your local machine

## TODO

There are a few features that we plan to add in the future:

- [ ] Render lyrics dynamically using ajax
- [ ] Remove the back button
- [ ] Add a search bar
- [ ] Add a light/dark mode toggle
- [ ] Add a music player
- [ ] Add more CSS styling to improve the visual appeal of the app
