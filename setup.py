from setuptools import setup

setup(
    name='catfacts',
    version='1.0',
    packages=['catfacts'],
    url='https://github.com/lndbrg/catfacts',
    license='MIT',
    author='Olle',
    author_email='geek@nerd.sh',
    description='CATFACTS! MEOW!',
    install_requires=['requests', 'beautifulsoup', 'lxml'],
    entry_points={
        'console_scripts': [
            'catfacts = catfacts:catfact',
        ]
    },
)
