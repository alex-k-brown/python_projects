class Job(object):
    def __init__(self, job_title):
        self.job_title = job_title

class Employee(object):

    def __init__(self, name, age, job_title):
        self.job = Job(job_title)
        self.name = name
        self.age = age
    def __str__(self):
        return "My name is %s, I am %d years old and I am a %s." %(self.name, self.age, self.job.job_title)

morgan = Employee("Morgan Williams", 24, "Software Developer")

print morgan