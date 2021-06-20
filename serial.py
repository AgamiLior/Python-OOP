"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    
    def __init__(self, start=100):
        self.start = self.num = start
        """
        create a number generator starting at 100
        """ 
    def __repr__(self):
        return f"Generated Serial is: {self.num}"
        """
        Represent the generated number
        """
    def generate(self):
        self.num += 1
        return self.num
        """
        show the serial number generated
        """
    
    def reset(self):
        self.num = self.start
        """
        reset the code to the original start (100)
        """
        
        
