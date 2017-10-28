from setuptools import setup, find_packages

from bina_bikers import __version__


name = 'bina_bikers'

version = __version__

setup(
    name=name,
    version=version,
    packages=find_packages(exclude=['tests', 'tests.*']),
    description='Bina bikers API',
    long_description=open('README.rst').read(),
    url='',
    author='Sheriff',
    author_email='danmbugua74@gmail.com',
    license='Proprietary',
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Bina Bikers',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 3 :: Only',
    ],
    install_requires=[
        'dj-database-url',
        'gunicorn==19.6.0',
        'djangorestframework==3.6.3',
        'djangorestframework-jwt==1.8.0',
        'django-filter==1.0.2',
        'django-cors-headers==1.2.2',
        'dj-database-url==0.4.1',
        'Click==6.6',
        'sarge==0.1.4',
        'ipython==5.1.0',
        'django==1.10.6',
        'psycopg2==2.6.2',
        'django-rest-auth==0.8.1',
        'drfdocs==0.0.11',
        'djangorestframework-gis==0.11.2',
        'raven==6.1.0',
        'django-sentry-400-middleware==0.3.0',
        'Pillow==4.1.1',
        'django-sendfile==0.3.11',
        'social_auth_core==1.4.0',
        'social-auth-app-django==1.2.0',
    ],
    scripts=[
        'bin/bina_bikers_manage.py',
    ],
    include_package_data=True
)
