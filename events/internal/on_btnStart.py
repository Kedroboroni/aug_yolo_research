import time
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QProgressBar
from PySide6.QtCore import Qt
from PySide6.QtCore import QThread, Signal
from multiprocessing import Process, Queue

def long_running_task(queue):
    total_steps = 100
    current_step = 0

    for i in range(total_steps):
        if i % 6 == 0:
            time.sleep(1.3)
        else:
            print("Процесс выполняется")
        
        current_step += 1
        percentage = int((current_step / total_steps) * 100)
        queue.put(percentage)  # Отправляем процент в очередь

    queue.put(None)  # Отправляем сигнал о завершении


class ProcessThread(QThread):
    finished = Signal(int)
    done = Signal()  

    def run(self):
        queue = Queue()
        process = Process(target=long_running_task, args=(queue,))
        process.start()

        while True:
            percentage = queue.get()  # Получаем данные из очереди
            if percentage is None:  # Проверяем на завершение
                self.done.emit()
                break
            self.finished.emit(percentage)



#Посмотреть про возбуждение сигналов (emit)
#Посмотреть про Qthread 
#Думай над организацией потоков и событий
#Посмотреть про QProgressBar











def start_internal_aug(text):

    print(text)

    for i in range (100):

        if i % 6 == 0:
            time.sleep(1.3)

        else:
            print("Процесс выполняется")
    