from setuptools import setup 
from Billiard import __version__ as current_version 

setup(
    name='Billiard',
    version='current_version',
    description='Square,torrus and elliptic billiard game',
    url='https://github.com/emmas2210/Billiard',
    author='Selena Iskounen, Emma Santinelli, Oumayma Khalifi',
    author_mail='selena.iskounen@etu.umontpellier.fr, emma.santinelli@etu.umontpellier.fr, oumayma.khalifi@etu.umontpellier.fr',
    license='MIT',
    packages=['Billiard','Billiard.square','Billiard.torrus','Billiard.elliptic'],
    zip_safe=False
)
