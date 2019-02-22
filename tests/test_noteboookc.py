"""Tests for `notebookc` package."""
import pytest
from notebookc import notebookc


def test_convert(capsys):
    """Correct my_name argument prints"""
    notebookc.convert("Jill")
    captured = capsys.readouterr()
    assert "Jill" in captured.out

    """Incorrect my_name argument doesn't print"""
    notebookc.convert("Jose")
    captured = capsys.readouterr()
    assert "Jill" not in captured.out

    """Raise an exception if non-string argument passed"""
    with pytest.raises(TypeError):
        notebookc.convert(99)
