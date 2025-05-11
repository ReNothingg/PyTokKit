from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()



def get_version(rel_path):
    with open(rel_path, 'r') as fp:
        for line in fp.read().splitlines():
            if line.startswith('__version__'):
                delim = '"' if '"' in line else "'"
                return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")

VERSION = get_version("pytokkit/__init__.py") 

setup(
    name="PyTokKit", 
    version=VERSION,
    author="Ваше Имя или Никнейм", 
    author_email="your.email@example.com", 
    description="A Python SKELETON library for interacting with TikTok (Proof of Concept - Not Functional for Real API Calls)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/PyTokKit", 
    packages=find_packages(exclude=["tests*", "examples*"]), 
    classifiers=[
        "Development Status :: 2 - Pre-Alpha", 
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License", 
        "Operating System :: OS Independent",
        "Warning :: Other", 
        "Topic :: Internet",
        "Framework :: Scrapy", 
    ],
    python_requires='>=3.7', 
    install_requires=[
        
        
        
    ],
    extras_require={
        "dev": [ 
            "pytest>=6.0",
            "flake8>=3.8",
            "black>=20.0", 
            "twine>=3.0.0", 
            "wheel",
            "setuptools",
            "build",
        ]
    },
    keywords="tiktok api wrapper tiktok-api python tiktok-client skeleton",
    project_urls={ 
        "Bug Tracker": "https://github.com/yourusername/PyTokKit/issues", 
        "Source Code": "https://github.com/yourusername/PyTokKit", 
        
    },
    include_package_data=True, 
)
