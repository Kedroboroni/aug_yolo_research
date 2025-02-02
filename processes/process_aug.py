
import sys, os
sys.path.append(os.path.dirname(
                    os.path.dirname(
                        os.path.dirname(
                            os.path.abspath(__file__)
                        )
                    )
                )
            )
sys.path.append(os.path.dirname(
                    os.path.dirname(
                        os.path.dirname(
                            os.path.dirname(
                                os.path.abspath(__file__)
                            )
                        )
                    )
                )
            )
from PySide6.QtCore import QThread, Signal
from multiprocessing import Process, Queue
from events.internal.on_btnStart import *





class ProcessThread(QThread):
    finished = Signal(int)
    done = Signal()
    progress = Signal(int)

    def __init__(self, path):
        super().__init__()
        self.path = path

    def run(self):
        queue = Queue()
        process = Process(target=on_btnStart, args=(queue, self.path, ))
        process.start()

        while True:
            percentage = queue.get()
            if percentage is None:
                self.done.emit()
                break
            self.progress.emit(percentage)
        self.finished.emit(percentage)    