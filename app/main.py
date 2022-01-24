# coding=UTF-8
"""Print out the name, job name and expected salary asynchronously."""

import asyncio
import hashlib
import random
import sys


def main() -> None:
    """Run the program."""
    information = [
        'Name: Julia\n',
        'Job Posting: Python Developer Trainee\n',
        'Expected Salary after a Year: 80k rubles\n',
    ]
    asyncio.run(print_data(information))

    secret_message = sys.stdin.read()
    sys.stdout.write(hash_message(secret_message))


async def print_after(phrase: str, delay: int) -> None:
    """Output a phrase after a delay.

    Args:
        phrase (str): a string to output
        delay (int): delay time in seconds
    """
    await asyncio.sleep(delay)
    sys.stdout.write(phrase)


async def print_data(information: list[str]) -> None:
    """Output a list of phrases asynchronously with random delays.

    Args:
        information (list[str]): a list of arguments to output
    """
    rand_gen = random.SystemRandom()
    tasks: list[asyncio.Task] = []
    for entry in information:
        new_task = asyncio.create_task(
            print_after(entry, rand_gen.randrange(0, 5)),
        )
        tasks.append(new_task)

    for task in tasks:
        await task


def hash_message(secret_message: str) -> str:
    """Turn a string into its sha256 hash.

    Args:
        secret_message (str): initial string

    Returns:
        str: hashed string
    """
    hash_obj = hashlib.sha256(secret_message.encode())
    return hash_obj.hexdigest()


if __name__ == '__main__':
    main()
