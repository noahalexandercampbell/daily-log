"""Smoke tests for daily-log CLI."""

from daily_log.cli import main, review, build_parser
from pathlib import Path
import tempfile


def test_review_counts_lines():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        f.write("entry one\nentry two\nentry three\n")
        fpath = f.name
    try:
        result = review(fpath)
        assert result == 0
    finally:
        Path(fpath).unlink()


def test_build_parser_has_review_choice():
    parser = build_parser()
    ns = parser.parse_args(["review", "dummy.txt"])
    assert ns.command == "review"


def test_main_returns_int():
    result = main(["review", __file__])
    assert isinstance(result, int)


def test_main_unknown_command_exits():
    try:
        main(["unknown", "x"])
        assert False, "should have raised"
    except SystemExit as e:
        assert e.code != 0
