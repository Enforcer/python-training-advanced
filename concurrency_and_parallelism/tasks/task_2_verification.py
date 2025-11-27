import time
from concurrent.futures import ThreadPoolExecutor

import httpx


HOST = "127.0.0.1"
PORT = 8080

def register_and_login() -> None:
    username = str(time.time())  # ensure uniqueness
    payload = {"username": username, "password": "admin"}
    response = httpx.post(f"http://{HOST}:{PORT}/users/register", json=payload)
    response.raise_for_status()
    for _ in range(10):
        response = httpx.post(f"http://{HOST}:{PORT}/users/login", json=payload)
        print(f"Login response:", response)


def ping_health() -> None:
    for _ in range(10):
        time.sleep(0.1)
        start = time.time()
        response = httpx.get(f"http://{HOST}:{PORT}/health")
        duration = time.time() - start
        print("Health response:", response, "took:", duration)


def main() -> None:
    print("Health endpoint speed without register and login")
    ping_health()
    print("Health endpoint speed with register and login")
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(ping_health)
        executor.submit(register_and_login)


if __name__ == "__main__":
    main()
