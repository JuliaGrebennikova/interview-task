# coding=UTF-8
"""Unit tests."""
import asyncio
import io

import pytest

from app.main import hash_message, main, print_after, print_data


def test_print_after(capsys) -> None:
    asyncio.run(print_after('Testing...\n', 1))
    output, _ = capsys.readouterr()
    assert output == 'Testing...\n'


@pytest.mark.timeout(5)
def test_print_data(capsys) -> None:
    information = ['Foo', 'Bar\n']
    asyncio.run(print_data(information))
    output, _ = capsys.readouterr()
    assert output == 'FooBar\n' or output == 'Bar\nFoo'


def test_hash_message() -> None:
    assert (
        hash_message('Hello World!\n') ==
        '03ba204e50d126e4674c005e04d82e84c21366780af1f43bd54a37816b6ab340'
    )


@pytest.mark.timeout(5)
def test_main(monkeypatch, capsys) -> None:
    monkeypatch.setattr('sys.stdin', io.StringIO('Hello World!\n'))
    main()
    output, _ = capsys.readouterr()
    assert 'Julia' in output
