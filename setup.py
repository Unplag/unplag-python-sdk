from setuptools import setup

setup(name='unplag',
      version='1.0.2',
      description='Unplag API python client',
      url='https://unplag.com',
      author='Oleg Mykolaichenko',
      author_email='mukolaichenko@gmail.com',
      license='Apache 2.0 License',
      packages=['unplag'],
      install_requires=[
            'requests_oauthlib',
            'requests_toolbelt',
            'msgpack-python>=0.4.8',
      ],
      test_suite = 'tests',
      zip_safe=False)
