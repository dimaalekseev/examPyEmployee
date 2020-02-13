from lib.employee import Employee


class Developer(Employee):
    def __init__(self, first, last, age, salary, job):
        # super().__init__()
        Employee.__init__(self, first, last, age, salary)
        self.__job = job

    @property
    def job(self):
        return self.__job

    @job.setter
    def job(self, job):
        self.__job = job
