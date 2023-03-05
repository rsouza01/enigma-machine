"""This module provides the RP To-Do CLI."""
# enigma/cli.py

from typing import Optional
import typer
from enigma import __app_name__, __version__, enigma

app = typer.Typer()


@app.command()
def encrypt(
    to_encrypt: str = typer.Option(
        "",
        "--payload",
        "-p",
        prompt="payload to encrypt",
    ),
) -> None:
    """Encryption handler."""
    enigma.encrypt(to_encrypt, {})


@app.command()
def decrypt(
    to_decrypt: str = typer.Option(
        "",
        "--payload",
        "-p",
        prompt="payload to decrypt",
    ),
) -> None:
    """Decryption handler."""
    enigma.decrypt(to_decrypt, {})


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None, "--version", "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )

) -> None:
    """Main handler."""
    return
