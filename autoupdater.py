#!/usr/bin/env python3
import inspect
import os
import subprocess
import threading
import time

interval = 5  # seconds


def _worker(relpath):
    while True:
        command = subprocess.run(["git", "pull", "origin", "master"])
        if command.returncode == 0:
            print("yaey")
        else:
            print("oh noes")
        time.sleep(interval)


def initialize():
    # Initialize the auto-updater. Must be called in the main script.

    parent_globals = inspect.currentframe().f_back.f_globals
    assert parent_globals["__name__"] == "__main__"

    filepath = parent_globals["__file__"]
    relpath = os.path.relpath(filepath)

    threading.Thread(target=_worker, args=(relpath,)).start()
