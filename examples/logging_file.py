import exlogging

exlogging.init({
    'file': {
        'filepath': '/tmp/exlogging.log',
        'level': 'debug',
    }
})

# You can see this log message at /tmp/exlogging.log
exlogging.debug("Hello World")
