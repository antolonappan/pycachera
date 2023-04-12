from distutils.core import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

files = ["pycachera/*"]
setup(
        name = 'pycachera',
        packages = ['pycachera'],
        package_data = {'pycachera' : files },
        version = '3.0.2',
        install_requires = ['numpy','pandas'],
        description = 'A powerfull python caching tool',
        author = 'Anto Idicherian Lonappan',
        author_email = 'mail@antolonappan.me',
        url = 'https://github.com/antolonappan/pycachera',
        long_description=long_description,
        long_description_content_type="text/markdown",
        )
