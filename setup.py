# python3 setup.py sdist bdist_wheel
import PipPackageInstaller
import setuptools

with open("README.md", "r") as file:
    long_description = file.read()

setuptools.setup(
    name="pip_package_installer",
    version="1.0.0",
    author="Jorge Cardona",
    author_email="correo@example.com",
    description="Descripción del paquete",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jorgecardona",
    py_modules=["main"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)