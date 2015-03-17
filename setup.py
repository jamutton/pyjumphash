# ***** BEGIN LICENSE BLOCK *****
#
# For copyright and licensing please refer to COPYING.
#
# ***** END LICENSE BLOCK *****
from setuptools import setup
import os
import platform

requirements = list()
requirements.append('numpy')

long_description = ('Pika is a pure-Python implementation of the AMQP 0-9-1 '
                    'protocol that tries to stay fairly independent of the '
                    'underlying network support  library. Pika was developed '
                    'primarily for use with RabbitMQ, but should also work '
                    'with other AMQP 0-9-1 brokers.')

setup(name='pyjumphash',
      version='0.9',
      description='Python Jump Hash Library',
      long_description=long_description,
      maintainer='James Mutton',
      maintainer_email='monkey@themuttons.com',
      url='https://github.com/jamutton/pyjumphash ',
      py_modules=['jumphash'],
      license='Apache v2.0',
      install_requires=requirements,
      extras_require={'numpy': ['numpy']},
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache License 2.0',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Topic :: Communications',
          'Topic :: Internet',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules'],
      zip_safe=False)
