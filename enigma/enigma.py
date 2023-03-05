"""Enigma Engine handler"""

from enigma import types


class EnigmaEngine:
    """Enigma Engine"""

    def __init__(self, options: types.Options) -> None:
        self._options: types.Options = options

    def process(self, payload: str) -> str:
        """Entrypoint"""
        print(f"Process Payload: {payload}")
        print(f"Options: {str(self._options)}")


def encrypt(payload, options):
    """Encrypt façade"""
    engine: EnigmaEngine = EnigmaEngine(options)
    engine.process(payload)


def decrypt(payload, options):
    """Decrypt façade"""
    engine: EnigmaEngine = EnigmaEngine(options)
    engine.process(payload)
