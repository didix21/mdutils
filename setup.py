from setuptools import setup

setup(name='mdutils',
      version=1.0,
      license='BSD-3-Clause',
      author='Didac Coll',
      author_email='didaccoll_93@hotmail.com',
      description='A package useful to create Markdown files while executing python code.',
      long_description=open('README.md').read(),
      classifiers=['Development Status :: 1 - Beta',
                   'Programming Language :: Python :: 3.6'],
      platforms=['Python 3.6'],
      packages=['mdutils', 'mdutils.tools'],
      # Depndent Packages
      include_package_data=True,
      zip_safe=False)
