from setuptools import setup, find_packages


setup(
    name='twisted_test',
    version='0.1',
    url='https://github.com/aseroglazov/twisted_test',
    license='BSD',
    author='Alexander Seroglazov',
    author_email='alexander.seroglazov@fake_mail.com',
    description='Twisted test',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Twisted',
        'pymongo==2.8',
        'mongoengine',
        'Pillow',
    ],
    tests_require=['requests']
)
