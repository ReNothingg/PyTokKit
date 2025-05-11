from .client import TikTokClient
from .exceptions import TikTokError, AuthenticationError, VideoUploadError

__version__ = "0.1.0" # Начальная версия
__all__ = [
    "TikTokClient",
    "TikTokError",
    "AuthenticationError",
    "VideoUploadError",
]

print("PyTokKit: WARNING - This is a skeleton library for TikTok interaction.")
print("Using unofficial APIs can be risky and may violate TikTok's ToS.")
print("Proceed with caution and at your own risk.")