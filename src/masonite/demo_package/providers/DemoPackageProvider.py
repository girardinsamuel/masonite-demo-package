"""A DemoPackageProvider Service Provider."""

from masonite.providers import Provider
from masonite.demo_package.commands.InstallCommand import InstallCommand


class DemoPackageProvider(Provider):
    """Provides Services To The Service Container."""

    def register(self):
        """Register objects into the Service Container."""
        self.app.make("commands").add(InstallCommand())

    def boot(self):
        """Boots services required by the container."""
        pass
