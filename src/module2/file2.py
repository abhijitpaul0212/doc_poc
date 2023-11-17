from src.utils import print_value


class File2:

    def __int__(self):
        print("Init of File1")

    def file2_func1(self, a: float, b: float) -> float:

        """
        The file2_func1 function multiplies two numbers together.

        :param a: float: first parameter
        :param b: float: second parameter
        :return: The product of a and b
        """
        val = a*b
        print_value(val)
        return val


if __name__ == '__main__':
    f = File2()
    f.file2_func1(3.3, 6)
