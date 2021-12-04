import setuptools

setuptools.setup(
    name='hackathon',
    version='0.0.1',
    license='MIT',
    author='SeungBaek Hong',
    author_email='baek2sm@gmail.com',
    description='Hackathon is a library for use in AI competitions.',
    long_description=open('README.md').read(),
    url='https://github.com/baek2sm/hackathon',
    packages=setuptools.find_packages(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.9',
    ],
)