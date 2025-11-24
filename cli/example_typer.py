import typer
from typing_extensions import Annotated

app = typer.Typer()

@app.command()
def greet(
        name: str,
        count: Annotated[
            int,
            typer.Option(
                "--count", "-c",
                help="Number of times to repeat the greeting."
            )
        ] = 1,
):
    message = f"Hello, {name}!"

    for _ in range(count):
        print(message)

if __name__ == "__main__":
    app()
