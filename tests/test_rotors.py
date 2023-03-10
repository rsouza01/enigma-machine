# tests/test_rotors.py
from typer.testing import CliRunner

from enigma import __app_name__, __version__, rotors


def test_rotor():
    """test_rotor"""
    contacts = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
    rotor_config = rotors.RotorConfig(contacts)

    rotor = rotors.Rotor(rotor_config)

    result = rotor.transform(1)
    assert result == 1

    result = rotor.transform(20)
    assert result == 20
