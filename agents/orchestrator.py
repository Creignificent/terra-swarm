"""Simple orchestrator that chains agents for a demo flow."""
import argparse
from rich.console import Console
from .diagnostics import DiagnosticsAgent
from .design import ConsortiumDesignAgent

console = Console()

def run_demo():
    console.print("[bold green]TerraSwarm Demo Flow[/bold green]")

    diag = DiagnosticsAgent()
    design = ConsortiumDesignAgent()

    # Simulated customer input
    inputs = {
        "sample": {
            "reported": ["petroleum hydrocarbons"],
            "soil_type": "loam",
            "location": "demo farm"
        }
    }

    console.print("1. Diagnostics Agent")
    profiled = diag.run(inputs)
    console.print(profiled)

    console.print("\n2. Consortium Design Agent")
    designed = design.run(profiled)
    console.print(designed)

    console.print("\n[bold]Demo complete.[/bold] Extend by wiring Compliance, Sourcing, etc.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()
    if args.demo:
        run_demo()
