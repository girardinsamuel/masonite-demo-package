"""A DemoPackageProvider Service Provider."""

from masonite.provider import ServiceProvider
from masonite.demo_package.commands.InstallCommand import InstallCommand


class DemoPackageProvider(ServiceProvider):
    """Provides Services To The Service Container."""

    wsgi = False

    def register(self):
        """Register objects into the Service Container."""
        self.app.bind("InstallCommand", InstallCommand())

    def boot(self):
        """Boots services required by the container."""
        pass
