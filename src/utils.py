import subprocess

def print_value(val):

    """
    The print_value function prints the value passed to it.

    :param val: Print the value of val
    :return: None
    """
    print(val)


def kill_process(process_name):

    """
    The kill_process function checks if there is any instance of the application running on Windows OS.
    If found, then it tries to terminate it

    :param process_name: Check if the process is running
    :return: None
    """

    tasklist_output = subprocess.check_output(['tasklist']).decode('utf-8')
    if process_name.lower() in tasklist_output.lower():
        print("The {0} process is running. Killing it".format(process_name))
        subprocess.call(['taskkill', '/F', '/IM', process_name])
    else:
        print("The {0} process is not running. We will launch a new instance of it".format(process_name))
