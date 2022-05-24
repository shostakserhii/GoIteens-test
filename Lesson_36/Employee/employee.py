import requests


class Employee:
    """simple class Employee."""
    raise_amt = 1.05

    def __init__(self, first, last, pay):
        for i in first:
            if i.isdigit():
                raise TypeError(f'{i} should not be in name')
        self._first = first
        self._last = last
        self._pay = pay

    @property
    def email(self):
        return f'{self._first}.{self._last}@email.com'

    @property
    def fullname(self):
        return f'{self._first} {self._last}'

    def apply_raise(self):
        self._pay *= self.raise_amt

    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self._last}/{month}')
        if response.ok:
            return response.text
        return 'Bad Response!'

