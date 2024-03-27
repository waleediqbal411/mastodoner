from setuptools import setup, find_packages

setup(
    name="mastodoner",
    version="0.0.1",
    author="Haris Bin Zia",
    author_email="harisbinzia@hotmail.com",
    description="A package for crawling Mastodon instances",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/harisbinzia/mastodoner",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'mastodoner = mastodoner.cli:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        'requests',
    ],
)