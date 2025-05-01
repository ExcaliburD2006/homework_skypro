import pytest
from pathlib import Path
from src.decorators import log


def test_log_to_console_success(capsys: pytest.CaptureFixture[str]) -> None:
    @log()
    def add(a: int, b: int) -> int:
        return a + b

    result = add(2, 3)
    captured = capsys.readouterr()

    assert "add ok" in captured.out
    assert result == 5


def test_log_to_console_error(capsys: pytest.CaptureFixture[str]) -> None:
    @log()
    def div(a: int, b: int) -> float:
        return a / b

    with pytest.raises(ZeroDivisionError):
        div(5, 0)

    captured = capsys.readouterr()
    assert "div error: ZeroDivisionError. Inputs: (5, 0), {}" in captured.out


def test_log_to_file_success(tmp_path: Path) -> None:
    filename = tmp_path / "test_log.txt"

    @log(filename=str(filename))
    def mul(a: int, b: int) -> int:
        return a * b

    result = mul(3, 4)

    with open(filename, "r") as f:
        log_content = f.read()

    assert "mul ok" in log_content
    assert result == 12


def test_log_to_file_error(tmp_path: Path) -> None:
    filename = tmp_path / "test_log.txt"

    @log(filename=str(filename))
    def raise_error() -> None:
        raise ValueError("Oops")

    with pytest.raises(ValueError):
        raise_error()

    with open(filename, "r") as f:
        log_content = f.read()

    assert "raise_error error: ValueError. Inputs: (), {}" in log_content


def test_log_preserves_exception() -> None:
    @log()
    def error_func() -> None:
        raise TypeError("Test error")

    with pytest.raises(TypeError) as exc_info:
        error_func()

    assert "Test error" in str(exc_info.value)
