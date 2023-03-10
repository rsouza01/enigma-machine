"""File for enigma related types"""
from enigma import rotors


class Options:
    """Option class"""

    def __init__(self, rotor_config: rotors.RotorConfig) -> None:
        self._rotor_config = rotor_config
