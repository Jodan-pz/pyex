import sys

# Simplify the filter by making it a mixin.

class Logger(object):
    def __init__(self, file):
        self.file = file

    def log(self, message):
        self.file.write(message + '\n')
        self.file.flush()


class FilterMixin:  # No base class!
    pattern = ''
    def log(self, message):
        if self.pattern in message:
            super().log(message)

# Multiple inheritance looks the same as above.

class FilteredLogger(FilterMixin, Logger):
    pass  # Again, the subclass needs no extra code.

# Works just fine.

logger = FilteredLogger(sys.stdout)
logger.pattern = 'Error'
logger.log('Warning: not that important')
logger.log('Error: this is important')