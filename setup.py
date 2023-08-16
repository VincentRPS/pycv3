import os

import setuptools

version = "3.0.0"

requirements = []
with open("requirements/required.txt") as f:
    requirements = f.read().splitlines()

packages: list[str] = []


for fn in os.scandir("pycord"):
    if fn.is_dir():
        packages.append(f.name)


def get_extra_requirements() -> dict[str, list[str]]:
    extra_requirements: dict[str, list[str]] = {}
    for fn in os.scandir("requirements"):
        if fn.is_file() and fn.name != "required.txt":
            with open(fn) as f:
                extra_requirements[fn.name.split(".")[0]] = f.read().splitlines()
    return extra_requirements


setuptools.setup(
    name="pycord",
    version=version,
    packages=packages,
    package_data={
        "pycord": ["panes/*.txt", "bin/*.dll"],
    },
    # TODO!
    project_urls={},
    url="https://github.com/",
    license="MIT",
    author="Pycord",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=requirements,
    extras_require=get_extra_requirements(),
    description="A Discord wrapper for building modern Discord bots.",
    python_requires=">=3.11",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Framework :: AsyncIO",
        "Framework :: aiohttp",
        "Topic :: Communications :: Chat",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
)
