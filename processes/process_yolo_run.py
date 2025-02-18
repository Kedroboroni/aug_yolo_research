
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
from multiprocessing import Process
from events.external.on_btnStart_external import *





class ProcessThreadExternal(QThread):
    finished = Signal(int)

    def __init__(self, path, listKeys, dictParams):
        super().__init__()
        self.path = path
        self.listKeys = listKeys
        self.dictParams = dictParams

    def run(self):
        process = Process(target=on_btnStart_external, args=(self.path, self.listKeys, self.dictParams))
        process.start()

        process.join()
        self.finished.emit(100)

