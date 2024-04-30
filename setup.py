from setuptools import setup, find_packages

# Read the requirements from the requirements.txt file
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="test_library",
    version="1.0.0",
    author="Thivin Anandh",
    author_email="thivinanandh@gmail.com",
    description="Test Description",
    packages=find_packages(),
    license="MIT",
    install_requires=requirements,
    keywords=['test', 'library', 'python', 'example']
)
