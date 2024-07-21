class Invoker:
    """
    Ask the command to carry out the request.
    """

    def __init__(self):
        self._commands = []

    def store_command(self, command):
        self._commands.append(command)

    def invoke_executor(self, executor):
        executor.execute_commands(self._commands)