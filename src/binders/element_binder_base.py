from abc import ABC, abstractmethod


class ElementBinderBase(ABC):
    @abstractmethod
    def bind_elements(self):
        pass
