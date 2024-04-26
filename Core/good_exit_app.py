import sys
import atexit
import signal

def exit_handler():
    print("Cleaning up")

def kill_handler(*args):
    sys.exit(0)

atexit.register(exit_handler)
signal.signal(signal.SIGINT, kill_handler)
signal.signal(signal.SIGTERM, kill_handler)

# MAIN PROGRAM
# for example just reading from the input:
input("Press enter: ")