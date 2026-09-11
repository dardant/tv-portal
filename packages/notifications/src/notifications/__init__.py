"""Customer email content. Other components use only the names in ``__all__``."""

from notifications.digest import build_digest
from notifications.templates import shipped_body, shipped_subject

__all__ = ["build_digest", "shipped_body", "shipped_subject"]
