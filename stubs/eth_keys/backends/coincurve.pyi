from .base import BaseECCBackend
from eth_keys.datatypes import PrivateKey, PublicKey, Signature
from typing import Any, Optional

def is_coincurve_available() -> bool: ...

class CoinCurveECCBackend(BaseECCBackend):
    keys: Any = ...
    ecdsa: Any = ...
    def __init__(self) -> None: ...
    def ecdsa_sign(self, msg_hash: bytes, private_key: PrivateKey) -> Signature: ...
    def ecdsa_recover(self, msg_hash: bytes, signature: Signature) -> Optional[PublicKey]: ...
    def private_key_to_public_key(self, private_key: PrivateKey) -> PublicKey: ...
