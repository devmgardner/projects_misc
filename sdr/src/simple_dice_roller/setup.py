from setuptools import setup
  
# reading long description from file
with open('DESCRIPTION.txt') as file:
    long_description = file.read()
  
  
# specify requirements of your package here
REQUIREMENTS = ['random','re','argparse']
  
# some more details
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Internet',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.10',
    ]
  
# calling the setup function 
setup(name='simple-die-roller',
      version='1.0.0',
      description='A simple die-/dice-rolling program',
      long_description=long_description,
      url='https://github.com/devmgardner/projects_misc',
      author='Devin M Gardner',
      author_email='devin@devinmgardner.com',
      license='MIT',
      packages=['geo'],
      classifiers=CLASSIFIERS,
      install_requires=REQUIREMENTS,
      keywords='maps location address'
      )