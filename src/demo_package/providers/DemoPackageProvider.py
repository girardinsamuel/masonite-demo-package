"""A DemoPackageProvider Service Provider."""

from masonite.packages import PackageProvider


class DemoPackageProvider(PackageProvider):

    def configure(self):
        """Register objects into the Service Container."""
        (
            self.root("demo_package")
            .name("demo-package")
            .config("config/demo_package.py", publish=True)
        )

    def register(self):
        super().register()

    def boot(self):
        """Boots services required by the container."""
        pass
