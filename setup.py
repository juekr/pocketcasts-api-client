import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pocketcastsapi',
    version='0.0.23',
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
    packages=['pocketcastsapi'],
    install_requires=['requests'],
)