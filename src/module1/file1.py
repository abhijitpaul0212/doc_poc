from src.utils import print_value


class File1:

    def __int__(self):
        print("Init of File1")

    def file1_func1(self, first: str, second: str) -> str:

        """
        The file1_func1 function takes two strings and returns their concatenation.

        :param first: str: Specify that the first parameter is a string
        :param second: str: Specify the type of the second parameter
        :return: The concatenation of the two strings
        """
        val = first+second
        print_value(val)
        return val

    def file1_func2(self, a: int, b: int) -> int:

        """
        The file1_func2 function adds two numbers together.

        :param self: Represent the instance of the class
        :param a: int: Specify that the parameter a is an integer
        :param b: int: Specify the type of parameter b
        :return: The sum of the two arguments
        """
        val = a+b
        print_value(val)
        return val
