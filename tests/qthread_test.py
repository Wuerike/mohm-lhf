from multiprocessing import Process, Queue
from PyQt4 import QtCore
from MyJob import job_function


# Runner lives on the runner thread

class Runner(QtCore.QObject):
    """
    Runs a job in a separate process and forwards messages from the job to the
    main thread through a pyqtSignal.

    """

    msg_from_job = QtCore.pyqtSignal(object)

    def __init__(self, start_signal):
        """
        :param start_signal: the pyqtSignal that starts the job

        """
        super(Runner, self).__init__()
        self.job_input = None
        start_signal.connect(self._run)

    def _run(self):
        queue = Queue()
        p = Process(target=job_function, args=(queue, self.job_input))
        p.start()
        while True:
            msg = queue.get()
            self.msg_from_job.emit(msg)
            if msg == 'done':
                break


# Things below live on the main thread

def run_job(input):
    """ Call this to start a new job """
    runner.job_input = input
    runner_thread.start()


def handle_msg(msg):
    print(msg)
    if msg == 'done':
        runner_thread.quit()
        runner_thread.wait()


# Setup the OQ listener thread and move the OQ runner object to it
runner_thread = QtCore.QThread()
runner = Runner(start_signal=runner_thread.started)
runner.msg_from_job.connect(handle_msg)
runner.moveToThread(runner_thread)