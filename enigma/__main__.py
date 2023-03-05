"""RP To-Do entry point script."""
# enigma/__main__.py

from enigma import cli, __app_name__


def main():
    with open("./enigma/banner.txt", 'r') as banner:
        print(banner.read())
    cli.app(prog_name=__app_name__)


if __name__ == "__main__":
    main()
