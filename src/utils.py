
def print_value(val):

    """
    The print_value function prints the value passed to it.

    :param val: Print the value of val
    :return: True
    """
    print(val)

def kill_process(process_name):
    """
    This method checks if there is any instance of the application running on Windows OS.
    If found, then it tries to terminate it
    :param process_name: name of windows process (type: str)
    :return: None
    """
    tasklist_output = subprocess.check_output(['tasklist']).decode('utf-8')
    if process_name.lower() in tasklist_output.lower():
        print("The {0} process is running. Killing it".format(process_name))
        subprocess.call(['taskkill', '/F', '/IM', process_name])
    else:
        print("The {0} process is not running. We will launch a new instance of it".format(process_name))
