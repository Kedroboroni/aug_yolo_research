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

    def __init__(self, path, listKeys, dictParams, p, check):
        super().__init__()
        self.path = path
        self.listKeys = listKeys
        self.dictParams = dictParams
        self.p = p
        self.check = check

    def run(self):
        queue = Queue()
        if self.check == 1:
            process = Process(target=on_btnStart_ON, args=(queue, self.path, self.listKeys, self.dictParams, self.p))
            
        elif self.check == 2:
            process = Process(target=on_btnStart_OFF, args=(queue, self.path, self.listKeys, self.dictParams, self.p))
        process.start()

        while True:
            percentage = queue.get()
            if percentage is None:
                self.done.emit()
                break
            self.progress.emit(percentage)
        self.finished.emit(percentage)   

 