from setuptools import setup, find_packages

setup(name='postnl_api',
      version='0.1',
      description='Python wrapper for the PostNL API, a way to track packages using their online portal',
      url='http://github.com/imicknl/python-postnl-api',
      author='Mick Vleeshouwer',
      author_email='mick@imick.nl',
      license='MIT',
      install_requires=['requests>=2.0'],
      packages=find_packages(),
      zip_safe=True)