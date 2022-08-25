"""
Custom resolutions to provide answers
"""

from .is_enabled import IsEnabled

# Natural language sugar
Enabled = IsEnabled

__all__ = [
    "Enabled",
    "IsEnabled",
]
