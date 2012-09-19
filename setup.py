from distutils.core import setup
import os

# Stolen from django-registration
# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

for dirpath, dirnames, filenames in os.walk('responsive_design_helper'):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'):
            del dirnames[i]
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)
    elif filenames:
        prefix = dirpath[len('responsive_design_helper/'):]
        for f in filenames:
            data_files.append(os.path.join(prefix, f))


setup(
    name='django-responsive-design-helper',
    version='0.2.0',
    description='Helper for testing responsive designs in Django',
    author='Travis Swicegood',
    author_email='development@domain51.com',
    url='http://github.com/tswicegood/django-responsive-design-helper/',
    packages=packages,
    package_data={'responsive_design_helper': data_files},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)
