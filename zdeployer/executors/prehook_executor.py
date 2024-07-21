class PreHookExecutor:
    """
    Know how to perform the operations associated with carrying out a
    request. Any class may serve as a Receiver.
    """
    def execute_commands(self, commands):
        for command in commands:
            command.execute()