from setuptools import setup

setup(
  name='awsclientbot',
  version='0.1',
  description='AWS Client for Telegram',
  author='Ivan Tertychnyy',
  author_email='it@chatfirst.co',
  packages=['awsclientbot'],
  url='https://github.com/tertychnyy/awsclientbot',
  license='LICENSE.txt',
  install_requires=[
        "requests>=2.10.0",
    ],
)
