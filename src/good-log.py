import os
import sys
import syslog

os.system('cls||clear')

# Logger --- Composition Over Inheritance ---


class Logger:
    def __init__(self, filters, handlers):
        self.filters = filters
        self.handlers = handlers

    def log(self, message):
        if all(f.match(message) for f in self.filters):
            for h in self.handlers:
                h.emit(message)


class TextFilter:
    def __init__(self, pattern):
        self.pattern = pattern

    def match(self, text):
        return self.pattern in text


class StreamHandler:
    def __init__(self, stream):
        self.stream = stream

    def emit(self, message):
        self.stream.write(message + '\n')
        self.stream.flush()


class SocketHandler:
    def __init__(self, sock):
        self.sock = sock

    def emit(self, message):
        self.sock.sendall((message + '\n').encode('ascii'))


class SyslogHandler:
    def __init__(self, priority):
        self.priority = priority

    def emit(self, message):
        syslog.syslog(self.priority, message)


filters = [TextFilter("error"), TextFilter("severe")]
handlers = [StreamHandler(sys.stdout)]

logger = Logger(filters, handlers)

logger.log("Meh, this will be ignored!")
logger.log("Meh, this if a super error!")
logger.log("[severe] Meh, this if a super error!")

