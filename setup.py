from setuptools import setup, find_packages

setup(
    name="recon241",
    version="2.0.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "dnspython",
        "python-whois",
        "beautifulsoup4",
        "lxml",
        "aiohttp",
        "rich",
        "jinja2",
        "weasyprint",
        "python-dotenv",
    ],
    entry_points={
        "console_scripts": [
            "recon241=recon241.main:main",
        ],
    },
    python_requires=">=3.8",
)
