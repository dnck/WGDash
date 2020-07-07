# WGDash
## Features
* read rss feeds
* read weather
* read lights on status
* read playlist info
* read messages

## Hack for now
launch docker container:
```
docker run --rm --it -p 5000:5000 --entrypoint /bin/bash wgdash
```
to run the server:
```
uswgi --http 0.0.0.0:5000 ---wsgi-file /WGDash/wsgi.py
```
