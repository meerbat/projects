try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Miriam Battistoni',
    'url': 'URL to get it at.',
    'download_url': "Where to download it.",
    'author_email': 'miriam.battistoni@maieuticallabs.it',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['exp36'],
    'scripts': [],
    'name': 'exp36'
}

setup(**config)
