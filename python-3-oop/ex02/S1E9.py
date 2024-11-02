from abc import ABC, abstractmethod


class Character(ABC):
    """Your docstring for Class"""
    @abstractmethod
    def __init__(self, first_name, is_alive=True, **kwargs):
        """
        Initializes a character.

        Parameters:
        - first_name (str): The first name of the character.
        - is_alive (bool, optional): Character's living status: default True.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """
        Marks the character as dead.

        This method should be overridden by subclasses.
        """
        pass


class Stark(Character):
    """Your docstring for Class"""
    def __init__(self, first_name, is_alive=True):
        """Your docstring for Constructor"""
        super().__init__(first_name, is_alive)

    def die(self):
        """Your docstring for Method"""
        self.is_alive = False
