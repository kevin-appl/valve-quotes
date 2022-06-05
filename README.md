# Valve quotes API [Beta Version]
A free fan-made API to retrieve quotes from the talented developers at Valve and from their groundbreaking video games!

Note: This repository currently doesn't contain the sources and configuration of the Nginx server. You can visit the linked [GitHub repository](https://github.com/kevin-appl/python-flask-docker-https) to see how to set up an Nginx server in combination with Flask, Gunicorn and Docker.

>Website and demo: https://valvequotes.xyz

>Production host: https://api.valvequotes.xyz


## Usage

`
 GET /v1/quotes/
`

Get a random quote in JSON format:

>https://api.valvequotes.xyz/v1/quotes/

```console
[
  {
    "quote": "You're a beautiful person with a charming personality",
    "author": "Gabe Newell, CEO Valve"
  }
]
```


`
 GET /v1/quotes/<INT>
`

Get multiple quotes in JSON format:

>https://api.valvequotes.xyz/v1/quotes/3

```console
[
  {
    "quote": "Fundamentally, [software] piracy is a service problem",
    "author": "Gabe Newell, CEO Valve"
  },
  {
    "quote": "Zoom times are awful for pitching.",
    "author": "Erik Wolpaw, Valve writer"
  },
  {
    "quote": "You're a beautiful person with a charming personality",
    "author": "Gabe Newell, CEO Valve"
  }
]
```

## How to contribute
If you want to submit a quote, you can do so via this GitHub repository. Fork this project and add your quote to the [mysql/quotes.csv](https://github.com/kevin-appl/valve-quotes/blob/main/mysql/quotes.csv) file. Now create a pull request. Voilà!

## Credits

Inspired by [Breaking Bad quotes API](https://github.com/shevabam/breaking-bad-quotes).

## About
Valve quotes API is a hobby project and is not affiliated with Valve Corporation. 
