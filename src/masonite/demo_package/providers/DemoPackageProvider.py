"""A DemoPackageProvider Service Provider."""

from masonite.providers import Provider
from ..commands.InstallCommand import InstallCommand


class DemoPackageProvider(Provider):
    """Provides Services To The Service Container."""

    def __init__(self, application):
        self.application = application

    def register(self):
        """Register objects into the Service Container."""
        self.application.make("commands").add(InstallCommand())

    def boot(self):
        """Boots services required by the container."""
        pass
