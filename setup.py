from setuptools import find_packages
from setuptools import setup


setup(
    name='sll.basepolicy',
    version='0.7',
    description='Base policy for sll, slt and ll packages.',
    long_description=open("README.rst").read(),
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7"],
    keywords='',
    author='ABITA OY',
    author_email='taito.horiuchi@abita.fi',
    url='https://github.com/taito/sll.basepolicy',
    license='Non-free',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    namespace_packages=['sll'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'abita.development',
        'hexagonit.socialbutton',
        'sll.baselocales',
        'setuptools'],
    extras_require={'test': ['hexagonit.testing']},
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """)
