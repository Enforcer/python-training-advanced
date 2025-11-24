class Server:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port

    def __hash__(self) -> int:
        return hash((self.host, self.port))

    def __bool__(self) -> bool:
        return True


server = Server("127.0.0.1", 8000)
print(hash(server))
print(bool(server))
len(server)
from typing import Sized