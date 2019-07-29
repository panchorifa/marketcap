#!/usr/bin/env python
import signal
import sys
import os
from market.app import create_app


def signal_handler(signal, frame):
    print 'Ctrl-c detected. App is going down!'
    sys.exit(0)


def main():
    signal.signal(signal.SIGINT, signal_handler)
    app = create_app()
    app.run(port=8000, debug=os.environ.get('DEBUG', False))

if __name__ == '__main__':
    main()
