from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.readlines()

setup(
    name='clichat',
    version='1.1.1',
    author='Vishal Sharma',
    author_email='vishalsharma1907@gmail.com',
    license='MIT',
    description='CliChat: A Python CLI tool for interactive chatbot interactions, offering features like clipboard copying and query retry. Compatible with Python 3.7+ on various operating systems.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/vishals9711/clichat',
    py_modules=['clichat'],
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'clichat=clichat:chat',
        ],
    },
)
