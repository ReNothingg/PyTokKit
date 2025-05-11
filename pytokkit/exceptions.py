class TikTokError(Exception):
    """Base exception class for PyTokKit errors."""
    pass

class AuthenticationError(TikTokError):
    """Raised for errors during authentication."""
    pass

class VideoUploadError(TikTokError):
    """Raised for errors during video upload."""
    pass

class APIError(TikTokError):
    """Raised for general API request errors."""
    def __init__(self, message, status_code=None):
        super().__init__(message)
        self.status_code = status_code