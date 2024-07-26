from setuptools import setup, find_packages

setup(
    name='postgredb',
    version='0.1.0',
    author='sovanedev',
    author_email='info@sovanedev.fun',
    description='',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/sovanedev/postgredb',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'psycopg2',
    ],
)
