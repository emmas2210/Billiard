from setuptools import setup 
from billiardpack import __version__ as current_version 

setup(
    name='billiardpack',
    version='current_version',
    description='Square,torrus and elliptic billiard game',
    url='https://github.com/emmas2210/Billiard',
    author='Selena Iskounen, Emma Santinelli, Oumayma Khalifi',
    author_mail='selena.iskounen@etu.umontpellier.fr, emma.santinelli@etu.umontpellier.fr, oumayma.khalifi@etu.umontpellier.fr',
    license='MIT',
    packages=['billiardpack','billiardpack.square','billiardpack.torrus','billiardpack.elliptic'],
    zip_safe=False
)
