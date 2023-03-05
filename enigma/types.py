"""File for enigma related types"""


class Rotor:
    """Rotor class"""


class ReflectorRotor(Rotor):
    pass


class MovingRotor(Rotor):
    pass



class RotorConfig:
    """RotorConfig class"""

    def __init__(self, rotor_2_letter_position, rotor_3_letter_position) -> None:
        self._rotor_2_letter_position = rotor_2_letter_position
        self._rotor_3_letter_position = rotor_3_letter_position


class Options:
    """Option class"""

    def __init__(self, rotor_config: RotorConfig) -> None:
        self._rotor_config = rotor_config
