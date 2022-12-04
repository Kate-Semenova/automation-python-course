"""
Create classes to track homeworks.
1. Homework - accepts howework text and deadline (datetime.timedelta)
Homework has a method, that tells if deadline has passed.
2. Student - can solve homework with `do_homework` method.
Raises DeadlineError with "You are late" message if deadline has passed
3. Teacher - can create homework with `create_homework`; check homework with `check_homework`.
Any teacher can create or check any homework (even if it was created by one of colleagues).
Homework are cached in dict-like structure named `homework_done`. Key is homework, values are
solutions. Each student can only have one homework solution.
Teacher can `reset_results` - with argument it will reset results for specific homework, without -
it clears the cache.
Homework is solved if solution has more than 5 symbols.
-------------------
Check file with tests to see how all these classes are used. You can create any additional classes
you want.
"""
from typing import Dict
from datetime import datetime, timedelta


class Hoooman:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Homework:

    def __init__(self, text, deadline: timedelta):
        self.text = text
        self.deadline = deadline
        self.creation_date = datetime.now()

    def is_deadline_has_passed(self):
        return self.creation_date + timedelta(days=self.deadline) < datetime.now()


class Result:
    def __init__(self, hw, solution, author):
        self.hw = hw
        self.solution = solution
        self.author = author


class Teacher(Hoooman):
    homework_done: Dict = {}

    @staticmethod
    def create_homework(name, deadline):
        homework = Homework(name, deadline)
        return homework

    @classmethod
    def check_homework(cls, result: Result):
        if result.hw in cls.homework_done:
            if result in cls.homework_done[result.hw]:
                return True
        else:
            cls.homework_done[result.hw] = set()
        if len(result.solution) > 5:
            cls.homework_done[result.hw].add(result)
            return True
        else:
            return False

    @classmethod
    def reset_results(cls, hw=None):
        if hw is None:
            cls.homework_done.clear()
        else:
            cls.homework_done.setdefault(hw, None)


class Student(Hoooman):
    def do_homework(self, hw: Homework, solution):
        if hw.is_deadline_has_passed():
            raise DeadlineError("You are late")
        return Result(hw, solution, self)


class DeadlineError(Exception):
    """Deadline is missed"""
