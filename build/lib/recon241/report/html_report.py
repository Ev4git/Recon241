import os
from jinja2 import Environment, FileSystemLoader


class HTMLReport:
    def __init__(self, results, output_dir):
        self.results = results
        self.output_dir = output_dir

    def generate(self):
        os.makedirs(self.output_dir, exist_ok=True)

        base_dir = os.path.dirname(os.path.dirname(__file__))
        template_dir = os.path.join(base_dir, "templates")

        env = Environment(loader=FileSystemLoader(template_dir))
        template = env.get_template("report.html")

        html = template.render(results=self.results)

        report_path = os.path.join(self.output_dir, "recon241_report.html")

        with open(report_path, "w", encoding="utf-8") as file:
            file.write(html)

        return report_path
