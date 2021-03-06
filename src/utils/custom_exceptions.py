class BasicException(Exception):
    pass


class InvalidPathException(BasicException):
    pass


class InvalidVersionNumber(BasicException):
    pass


class NoFilesFound(BasicException):
    pass


class LibraryNotFoundException(BasicException):
    pass


class BadSetOfOptions(BasicException):
    pass


class NoOperationSelected(BasicException):
    pass


class IncompatibleWithDRSConfigPath(BasicException):
    pass


class OutputDirectoryNotFound(BasicException):
    pass
