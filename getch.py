## Used to get key input without refreshing stdin.
## Compeltely and utterly stolen from here:
## http://code.activestate.com/recipes/134892-getch-like-unbuffered-character-reading-from-stdin/
## Should work on both Windows and Mac/Unix systems, but I haven't tested on Windows.


class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchUnix()
        except ImportError:
            self.impl = _GetchWindows()

    def __call__(self):
        return self.impl()


class _GetchUnix:
    def __init__(self):
        pass

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        pass

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = _Getch()
