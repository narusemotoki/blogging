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
    description="blogging supports to setup python standard logging package.",
    long_descriptiondescription=readme(),
    classifiers=[
        'Topic :: Utilities',
        'Topic :: Software Development',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    license=blogging.__license__,
    author=blogging.__author__,
    author_email='motoki@naru.se',
    url='https://github.com/narusemotoki/blogging',
    keywords=' '.join(['log', 'logging', 'logger']),
    zip_safe=False,
    install_requires=parse_requirements(),
)
