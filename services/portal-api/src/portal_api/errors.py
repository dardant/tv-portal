"""Errors a handler turns into a client response."""

from __future__ import annotations


class ClientError(Exception):
    """Bad input. Becomes a 4xx response carrying a stable, machine-readable ``code`` (CONTRIBUTING.md, rule 4)."""

    status = 400

    def __init__(self, code: str, message: str) -> None:
        super().__init__(message)
        self.code = code
