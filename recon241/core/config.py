from dataclasses import dataclass


@dataclass
class ScanConfig:
    target: str
    output: str = "reports"
    timeout: int = 10
