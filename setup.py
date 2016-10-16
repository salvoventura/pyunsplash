from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='pyunsplash',
    version='0.1.0',
    description='A Python client for the Unsplash API.',
    long_description='A Python client for the Unsplash API.',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='unsplash unsplash.com client rest api',
    url='http://github.com/salvoventura/pyunsplash',
    author='Salvatore Ventura',
    author_email='salvoventura@gmail.com',
    license='MIT',
    packages=['pyunsplash'],
    install_requires=['requests'],
    zip_safe=False,
)

