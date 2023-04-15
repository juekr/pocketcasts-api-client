import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pocketcasts-api-client',
    version='0.0.1',
    author='Jürgen Krauß',
    author_email='juergen@es-ist-ein-krauss.de',
    description='Inofficial Pocketcasts API client',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/juekr/pocketcasts-api-client',
    project_urls = {
        "Bug Tracker": "https://github.com/juekr/pocketcasts-api-client/issues"
    },
    license='CC-4.0-NC-BY',
    packages=['pocketcasts-api-client'],
    install_requires=['requests'],
)