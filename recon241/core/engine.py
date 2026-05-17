import requests
from datetime import datetime
from bs4 import BeautifulSoup
from rich.console import Console
from rich.table import Table

from recon241.report.html_report import HTMLReport


class Recon241Engine:
    def __init__(self, config):
        self.config = config
        self.console = Console()
        self.results = {
            "tool": "Recon241",
            "author": "Ev@",
            "target": config.target,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "status_code": None,
            "title": "N/A",
            "headers": {},
            "links": [],
            "findings": [],
        }

    def normalize_target(self):
        if not self.config.target.startswith(("http://", "https://")):
            return "https://" + self.config.target
        return self.config.target

    def run(self):
        target_url = self.normalize_target()

        self.console.print("\n[bold green]Recon241 Started[/bold green]")
        self.console.print(f"[cyan]Target:[/cyan] {target_url}\n")

        try:
            response = requests.get(target_url, timeout=self.config.timeout)
            self.results["status_code"] = response.status_code
            self.results["headers"] = dict(response.headers)

            soup = BeautifulSoup(response.text, "html.parser")

            title = soup.find("title")
            if title:
                self.results["title"] = title.get_text(strip=True)

            links = []
            for link in soup.find_all("a", href=True):
                links.append(link["href"])

            self.results["links"] = list(set(links))[:50]

            self.security_header_checks()

        except requests.RequestException as error:
            self.results["findings"].append({
                "severity": "High",
                "title": "Request Failed",
                "description": str(error),
            })

        self.print_summary()

        report = HTMLReport(self.results, self.config.output)
        report_path = report.generate()

        self.console.print(f"\n[bold green]HTML Report Generated:[/bold green] {report_path}")

    def security_header_checks(self):
        headers = self.results.get("headers", {})

        important_headers = [
            "Content-Security-Policy",
            "X-Frame-Options",
            "X-Content-Type-Options",
            "Strict-Transport-Security",
        ]

        for header in important_headers:
            if header not in headers:
                self.results["findings"].append({
                    "severity": "Medium",
                    "title": f"Missing Security Header: {header}",
                    "description": f"The target does not include the {header} header.",
                })

    def print_summary(self):
        table = Table(title="Recon241 Scan Summary")

        table.add_column("Field", style="cyan")
        table.add_column("Value", style="green")

        table.add_row("Tool", self.results["tool"])
        table.add_row("Author", self.results["author"])
        table.add_row("Target", self.results["target"])
        table.add_row("Status Code", str(self.results["status_code"]))
        table.add_row("Page Title", self.results["title"])
        table.add_row("Links Found", str(len(self.results["links"])))
        table.add_row("Findings", str(len(self.results["findings"])))

        self.console.print(table)
