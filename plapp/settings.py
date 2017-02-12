import os
import sys


SECRET_KEY = '3rlnzua_-qmc5jz0v960v-3os2j$_1i4rck4f!#!olwvhp=x@s'

try:

    env = os.environ.get('EWKS')

    if env == 'dev':
        config_type = 'dev_settings'
        print "running in environment: dev"
    elif env == 'prod':
        config_type = 'prod_settings'
        print "running in environment: prod"
    else:
        sys.exit("Earthworkx environment variable is not properly configured.")

    # Import the configuration settings file - REPLACE projectname with your project
    config_module = __import__(config_type, globals(), locals(), 'plapp')

    # Load the config settings properties into the local scope.
    for setting in dir(config_module):
        if setting == setting.upper():
            locals()[setting] = getattr(config_module, setting)

except Exception, e:

    sys.exit("Please set the proper environment variable so to run the dashboard.")