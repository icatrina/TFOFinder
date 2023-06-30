from setuptools import setup

setup(name='TFOFinder',
      version='1.0',
      description='Find TFO probes',
      url='https://github.com/icatrina/TFOFinder',
      author='Irina E. Catrina',
      author_email='iecatrina@gmail.com',
      license='Yeshiva University',
      #packages=['TFOFinder'],
      install_requires=[
          'pandas', 'Biopython<1.79'],


      zip_safe=False,
      platforms=['any'])
