# -*- coding: utf-8 -*-

class LogLevel:
    verbose = 0
    inform = 1
    warning = 2
    error = 3
    default = 1

    @staticmethod
    def toString(level=1):
        # type: (int) -> str
        mapping = ["Verbose", "Inform", "Warning", "Error"]
        return mapping[level]