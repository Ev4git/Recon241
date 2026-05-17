import click

from recon241.core.config import ScanConfig
from recon241.core.engine import Recon241Engine


@click.command()
@click.argument("target")
@click.option("-o", "--output", default="reports", help="Output directory for reports")
@click.option("--timeout", default=10, help="Request timeout in seconds")
def main(target, output, timeout):
    """
    Recon241 - Simple Reconnaissance and HTML Reporting Tool.

    Example:
        recon241 example.com
    """
    config = ScanConfig(
        target=target,
        output=output,
        timeout=timeout,
    )

    engine = Recon241Engine(config)
    engine.run()


if __name__ == "__main__":
    main()
