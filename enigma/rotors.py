"""File for enigma related types"""


class RotorConfig:
    """Rotor Config class"""

    def __init__(self, contact_list) -> None:
        self.contact_list = contact_list


class Rotor:
    """Rotor class"""

    def __init__(self, config: RotorConfig) -> None:
        self.config: RotorConfig = config

    def transform(self, key: int) -> int:
        """Transform method"""
        return self.config.contact_list[key]


class ReflectorRotor(Rotor):
    """Reflector rotor"""
    pass


class MovingRotor(Rotor):
    """Regular rotor"""
    pass


class ScramblerUnitConfig:
    """ScramblerUnitConfig class"""

    def __init__(self, rotor_2_letter_position, rotor_3_letter_position) -> None:
        self._rotor_2_letter_position = rotor_2_letter_position
        self._rotor_3_letter_position = rotor_3_letter_position
