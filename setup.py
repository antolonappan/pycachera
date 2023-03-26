from distutils.core import setup
files = ["pycacher/*"]
setup(
        name = 'pycacher',
        packages = ['pycacher'],
        package_data = {'pycacher' : files },
        version = '1.0.0',
        description = 'A powerfull python caching tool',
        author = 'Anto Idicherian Lonappan',
        author_email = 'mail@antolonappan.me',
        url = 'https://github.com/antolonappan/pycacher'
        )