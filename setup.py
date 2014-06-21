from distutils.core import setup


setup(
    name='secretariobot',
    version='0.0.1',
    url="https://github.com/aniversarioperu/secretariobot",
    author="AniversarioPeru",
    author_email="aniversarioperu1@gmail.com",
    maintainer="AniversarioPeru",
    maintainer_email="aniversarioperu1@gmail.com",
    contact="AniversarioPeru",
    contact_email="aniversarioperu1@gmail.com",
    license="GPL v3",
    description="be a secretariobot",
    long_description=open('README.md').read(),
    platforms="any",
    download_url="",
    classifiers=[
        "Programming Language :: Python",
        ("Topic :: Scientific/Engineering :: Bio-Informatics"),
        ("Intended Audience :: Science/Research"),
        ("License :: OSI Approved :: GNU General Public License v3 (GPLv3)"),
        ("Operating System :: OS Independent"),
        ("Environment :: Console"),
    ],
    install_requires=['nltk'],
    packages=['secretariobot'],
)

