import os
import setuptools


app_enviroment = os.getenv('APP_ENVIROMENT')
requirements = [
    'numpy==1.23.2',
    'numpy-financial==1.0.0',
    'pandas==1.4.3',
    'python-dateutil==2.8.2',
    'pytz==2022.2.1',
    'six==1.16.0'
]

if app_enviroment != 'dev' or app_enviroment != 'homolog' or \
    app_enviroment == 'stage' or not app_enviroment:
        requirements.append('pytest==7.1.2')
        # requirements.append('pytest-freezegun==0.4.2')
        requirements.append('pytest-asyncio==0.19.0')


setuptools.setup(
    name='MyAuth-API',
    version='0.0.1',
    author='Giovani Liskoski Zanini',
    author_email='giovanilzanini@hotmail.com',
    description='Gerenciar a autenticação dos usuarios de sua plataforma.',
    packages=setuptools.find_packages(),
    package_dir={
        "IrrTool": "./IrrTool"
    },
    python_requires=">=3.10.*",
    install_requires=requirements
)
