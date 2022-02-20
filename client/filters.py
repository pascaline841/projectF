from abc import ABC, abstractmethod

from .models import Client


class DataSource(ABC):
    @abstractmethod
    def query(self, **kwargs):
        ...

    @property
    @abstractmethod
    def name(self):
        ...


class FilterDatabase(DataSource):
    def __init__(self, name):
        self._name = name

    def query(self, **kwargs):
        filters = {'first_name': kwargs['first_name'], 
                   'last_name': kwargs['last_name'], 
                   'email': kwargs['email'],
                   }
        return Client.objects.using(self.name).filter(**filters)  

    @property
    def name(self):
        return self._name

