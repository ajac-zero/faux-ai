import os
import subprocess

import typer

cli = typer.Typer()

dir_path = os.path.dirname(os.path.realpath(__file__))


@cli.command()
def start(port: int = 8100):
    typer.echo(f"Starting MockAI server on port {port}...\n")
    subprocess.run(
        ["uvicorn", "--app-dir", f"{dir_path}", "server:app", "--port", f"{port}"]
    )