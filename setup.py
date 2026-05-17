from setuptools import setup, find_packages

setup(
    name="recon241",
    version="1.0.0",
    author="Ev@",
    description="Recon241 - Automated Reconnaissance and HTML Reporting Tool",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click>=8.1.0",
        "rich>=13.0.0",
        "requests>=2.28.0",
        "beautifulsoup4>=4.11.0",
        "jinja2>=3.1.0",
    ],
    entry_points={
        "console_scripts": [
            "recon241=recon241.core.cli:main",
        ],
    },
    python_requires=">=3.8",
)
