# GhCalServer

**Base URL: 

This is a simple application that re-serves the GitHub contributions calendar graph data, without [CORS](http://en.wikipedia.org/wiki/Cross-origin_resource_sharing) restrictions.

This application also supports [JSONP requests](http://en.wikipedia.org/wiki/JSONP).

## Usage

|Method|URL|Response|
|:------|:---:|:--------|
|GET|/|Redirect to GitHub repo|
|GET|/<username>|JSON of GitHub contributions data. See [here](http://github.com/users/rukmal/contributions_calendar_data) for example.|

## Deployment

### Local

```bash
$ sudo pip install -r requirements.txt
$ sudo python app.py
```

## Heroku

```bash
$ heroku create <app_name_here>
$ git push heroku master
```

## Contact

This is an open source project released under the [MIT License](LICENSE). Contact me if you want to suggest an improvement, or fork and send a pull request!

Follow me on Twitter ([@rukmal](http://twitter.com/rukmal_w)) and [GitHub](http://github.com/rukmal).

http://rukmal.me