# Theorem as a Service

## Introduction

Math and Python are two great flavours that taste great separately, so why not put them together?

This project creates a service that provides both HTML and a RESTful API to get assorted mathematical theorems.

## Access through a browser

Go to 
```
http://theoremsasaservice-production.up.railway.app/index.html
```
to see a theorem.

## Access through Terminal

Using a tool like `curl`, you can access the API by running
```
curl http://theoremsasaservice-production.up.railway.app/theorem

```
from a terminal. Helpful if you're a terminal user.

## Local development

This project uses [uv](https://docs.astral.sh/uv/)

so to get started you can run

```
uv install
uv run fastapi dev
```

which will start a service at `localhost:8000`.

Contributions, Bug Reports and Discussions Welcome!