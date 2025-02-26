import threading
from functools import cached_property


class Event(threading.Event):
    def is_set(self):
        value = super().is_set()
        print(f"is_set() -> {value}")
        return value


class Reloader:
    def start(self):
        from threading import Thread

        self.thread = Thread(target=self.run)
        self.thread.start()

    def stop(self):
        self._event.set()
        assert self._event.is_set()
        del self._event  # remove this line can solve the issue too
        self.thread.join()

    @cached_property
    def _event(self):
        return Event()

    def run(self):
        from watchfiles import watch  # move this line to the top of the file to solve the issue

        for _ in watch(".", stop_event=self._event):
            ...


reloader = Reloader()

reloader.start()
reloader.stop()

print("done")
