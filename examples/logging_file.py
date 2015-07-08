import blogging

blogging.init({
    'file': {
        'filepath': '/tmp/blogging.log',
        'level': 'debug',
    }
})

# You can see this log message at /tmp/blogging.log
blogging.debug("Hello World")
