import abc

class ICommand(metaclass=abc.ABCMeta):
    """
    Declare an interface for executing an operation.
    """
    @abc.abstractmethod
    def execute(self):
        pass