==========================
django-deferred-filelogger
==========================

This package provides a new logging handler that defers evaluation of the
filepath until a message is emitted.  It uses a setting ``LOG_ROOT`` as the
folder for the log files.  This is useful when you don't know the exact location
of your log files when the ``LOGGING`` setting is defined - this can be the case
if you have a environment specific settings file which gets imported after your
core settings.

Usage
-----

In your main settings file, configure your handlers with a filename

.. code:: python

    LOGGING = {
        ...
        'handlers': {
            'error_file': {
                'level': 'INFO',
                'class': 'deferred_filelogger.DeferredFilehandler',
                'filename': 'errors.log',
            }
        },
        'loggers': {
            'django.request': {
                'handlers': ['error_file', 'mail_admins'],
                'level': 'ERROR',
                'propagate': False
            }
        }
    }

then in your environmental overrides (eg ``settings_local.py``), specify a
``LOG_ROOT`` folder.  For instance, in your test environment you might specify

.. code:: python

    LOG_ROOT = '/var/www/client/project/logs/test'

which would cause your Django errors to be logged to
``/var/www/client/project/logs/test/errors.log``.
