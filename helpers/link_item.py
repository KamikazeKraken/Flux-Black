from dataclasses import dataclass
from typing import Optional


@dataclass
class LinkItem:
    """
    A helper class for HTML url data.
    """
    title: str
    url: str
    type: Optional[str] = None
