from setuptools import setup
import blogging


def parse_requirements():
    with open('requirements.txt') as f:
        return [l.strip() for l in f.readlines() if not l.startswith('#')]


def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='blogging',
    version=blogging.__version__,
    description=readme(),
    license=blogging.__license__,
    author=blogging.__author__,
    author_email='motoki@naru.se',
    url='https://github.com/narusemotoki/blogging',
    keywords=' '.join(['log', 'logging', 'logger']),
    install_requires=parse_requirements(),
)
