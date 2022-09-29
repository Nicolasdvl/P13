# Project 13 - Data visualisation of tweets network

This repo was created as part of coding learning with Open Classroom. 

## Application
This application provide :
- Parser based on [tweepy](https://github.com/tweepy/tweepy) to parse data from Twitter API
- Database models to saved data requested
- Data visualisation based on [anychart](https://www.anychart.com/products/anychart/overview/)

## Installation

### Pull the repo :  
```
git pull https://github.com/Nicolasdvl/P13.git
```  

### Install dependencies :  
- with pipenv :  
```
pipenv install
```  
- or with another virtual env using 'requirements.txt'

### Create .env file :
```
DJANGO_KEY=<SECRET KEY>
DJANGO_DEBUG='False'
TWITTER_BEARER=<YOUR BEARER TOKEN>
```
About [secret key](https://docs.djangoproject.com/en/4.1/ref/settings/#std-setting-SECRET_KEY)  
Get access to the twitter API [here](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api)


## Usage

### Activate virtual environment
```
pipenv shell
```  

### Launch the application locally  
```
python app/manage.py runserver
```

### Use the application
Open your browser at [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Development
### Run tests
```
python app/manage.py test app
```

## Production
This application use TailwindCSS framework. TailwindCSS is implemented via CDN, according to the doc this not the best choice for production. See more info [here](https://tailwindcss.com/docs/installation/play-cdn)