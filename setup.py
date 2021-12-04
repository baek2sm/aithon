import setuptools

setuptools.setup(
    name='aithon',
    version='0.0.1',
    license='MIT',
    author='SeungBaek Hong',
    author_email='baek2sm@gmail.com',
    description='Aithon is a library for use in AI hackathon.',
    long_description=open('README.md').read(),
    url='https://github.com/baek2sm/aithon',
    packages=setuptools.find_packages(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.9',
    ],
)