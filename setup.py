from distutils.core import setup
files = ["pycachera/*"]
setup(
        name = 'pycachera',
        packages = ['pycachera'],
        package_data = {'pycachera' : files },
        version = '2.0.5',
        install_requires = ['numpy','pandas'],
        description = 'A powerfull python caching tool',
        author = 'Anto Idicherian Lonappan',
        author_email = 'mail@antolonappan.me',
        url = 'https://github.com/antolonappan/pycachera'
        )
