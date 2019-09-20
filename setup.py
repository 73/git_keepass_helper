from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(name='git_keepass_helper',
    version='0.1',
    description='A KeePass crendential helper for git',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Utilities',
    ],
    url='https://github.com/73/git_keepass_helper',
    author='Arnold Sykosch',
    author_email='arnold.sykosch@gmail.com',
    license='MIT',
    packages=['git_keepass_helper'],
    install_requires=[
      'pykeepass',
    ],
    scripts=['bin/git-credential-keepass'],
    zip_safe=False)
