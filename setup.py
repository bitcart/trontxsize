from setuptools import find_packages, setup

setup(
    name="trontxsize",
    packages=find_packages(),
    version="1.0.4",
    license="MIT",
    description="Calculate tron transaction size (bandwidth)",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="MrNaif2018",
    author_email="chuff184@gmail.com",
    url="https://github.com/bitcartcc/trontxsize",
    keywords=["tron", "trx", "bitcartcc", "bandwidth"],
    install_requires=["protobuf", "base58"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
)
