from setuptools import setup, find_packages
from codecs import open

from ipfs_storage import __version__


try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    with open('README.rst', encoding='utf-8') as f:
        long_description = f.read()


setup(
    name='django-ipfs-storage',
    description='IPFS storage backend for Django.',
    long_description=long_description,
    keywords='django ipfs storage',
    version=__version__,
    license='MPL 2.0',

    author='Ben Jeffrey',
    author_email='mail@benjeffrey.net',
    url='https://github.com/jeffbr13/django-ipfs-storage',

    classifiers=(
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Framework :: Django',
    ),

    packages=find_packages(),

    install_requires=(
        'django',
        'ipfsapi',
    ),
    setup_requires=(
        'pypandoc',
    )
)
