import socket
from typing import Pattern

class Logger(object):
    def __init__(self, file):
        self.file = file

    def log(self, message):
        self.file.write(message + '\n')
        self.file.flush()

class SocketLogger(Logger):
    def __init__(self, sock):
        self.sock = sock

    def log(self, message):
        self.sock.sendall((message + '\n').encode('ascii'))

class FilteredLogger(Logger):
    def __init__(self, pattern, file):
        self.pattern = pattern
        super().__init__(file)

    def log(self, message):
        if self.pattern in message:
            super().log(message)

# A class derived through multiple inheritance.

class FilteredSocketLogger(FilteredLogger, SocketLogger):
    def __init__(self, pattern, sock):
        FilteredLogger.__init__(self, pattern, None)
        SocketLogger.__init__(self, sock)

# Works just fine.
sock1, sock2 = socket.socketpair()

logger = FilteredSocketLogger('Error', sock1)
logger.log('Warning: not that important')
logger.log('Error: this is important')

print('The socket received: %r' % sock2.recv(512))


# Don’t accept a “pattern” during initialization.
class FilteredLogger(Logger):
    pattern = ''

    def log(self, message):
        if self.pattern in message:
            super().log(message)

# Multiple inheritance is now simpler.

class FilteredSocketLogger(FilteredLogger, SocketLogger):
    pass  # This subclass needs no extra code!

# The caller can just set “pattern” directly.

logger = FilteredSocketLogger(sock1)
logger.pattern = 'Error'

# Works just fine.

logger.log('Warning: not that important')
logger.log('Error: this is important')

print('The socket received: %r' % sock2.recv(512))
