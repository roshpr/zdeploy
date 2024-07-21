from zdeployer.commands.icommand import ICommand


class GenerateCDKConfig(ICommand):
    """
    Define a binding between a Receiver object and an action.
    Implement Execute by invoking the corresponding operation(s) on
    Receiver.
    """

    def execute(self):
        print('Generate CDK Config')