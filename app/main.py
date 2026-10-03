import os


def move_file(command: str) -> None:
    _, source, destination = command.split()

    directory = os.path.dirname(destination)

    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(source, "r") as file_in, open(destination, "w") as file_out:
        file_out.write(file_in.read())

    os.remove(source)
