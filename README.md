# flask-tutorial

Very simple Flask implementation to test Mixpanel

## Initial setup

Ensure Python3 is installed.

Add debug environment variables:

```
export FLASK_ENV=development 
export FLASK_DEBUG=1
```

Add Mixpanel token:

```
export MIXPANEL_TOKEN=[token here]
```

## To run

From the repository's main directory:

```
source bin/activate 
```

```
flask run
```
