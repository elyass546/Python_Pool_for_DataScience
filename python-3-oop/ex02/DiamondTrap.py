from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    def __init__(self, first_name, is_alive=True):
        # Initialize using Baratheon to set Baratheon-specific defaults
        super().__init__(first_name, is_alive)
    
    def set_eyes(self, color):
        """
        Set the eye color of the king.

        Args:
            color (str): The color of the king's eyes.
        """
        self.eyes = color

    def set_hairs(self, color):
        """
        Set the hair color of the king.

        Args:
            color (str): The color of the king's hair.
        """
        self.hairs = color

    def get_eyes(self):
        """
        Get the eye color of the king.

        Returns:
            str: The color of the king's eyes.
        """
        return self.eyes

    def get_hairs(self):
        """
        Get the hair color of the king.

        Returns:
            str: The color of the king's hair.
        """
        return self.hairs