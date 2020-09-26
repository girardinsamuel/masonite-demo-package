"""A InstallCommand Command."""
import os
from cleo import Command
from masonite.packages import create_or_append_config


package_directory = os.path.dirname(os.path.realpath(__file__))


class InstallCommand(Command):
    """
    Install Demo Package into a project.

    command:name
        {argument : description}
    """

    def handle(self):
        # publish config files
        create_or_append_config(
            os.path.join(package_directory, "../config/demo_package.py")
        )
        # you could publish views, controllers, commands or assets here
        # you can also do it in boot() method of the provider with publishes()
