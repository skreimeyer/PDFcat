#!/usr/bin/env python

from distutils.core import setup

with open('README.rst','r') as infile:
    README = infile.read()

setup(
    name="PDFcat",
    version="1.0.0",
    description="Concatenate all PDFs in a folder to a specified output file",
    author="Samuel Kreimeyer",
    author_email="samuel.kreimeyer@gmail.com",
    long_description=README,
    url="https://github.com/skreimeyer/pdfcat",
    project_urls={
        'Documentation':'https://skreimeyer.github.io/pdfcat',
        'Source':'https://github.com/skreimeyer/pdfcat'
    }
    packages=['pdfcat'],
    license='Unlicense',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Office/Business',
        'Topic :: Utilities',
        'License :: Freeware',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='pdf merge concatenate',
    entry_points={
        'console_scripts': [
            'pdfcat = pdfcat.pdfcat:main',
        ]
    },
)
