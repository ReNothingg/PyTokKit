import unittest
from pytokkit import TikTokClient, AuthenticationError, VideoUploadError

class TestTikTokClientSkeleton(unittest.TestCase):

    def setUp(self):
        self.client = TikTokClient(session_id="test_session_id")

    def test_client_initialization(self):
        self.assertIsNotNone(self.client)
        self.assertEqual(self.client.session_id, "test_session_id")

    def test_get_user_info_skeleton(self):
        # Тестируем, что заглушка возвращает ожидаемую структуру
        user_info = self.client.get_user_info("testuser")
        self.assertIn("username", user_info)
        self.assertEqual(user_info["username"], "testuser")

    def test_get_trending_videos_skeleton(self):
        videos = self.client.get_trending_videos(count=2)
        self.assertEqual(len(videos), 2)
        self.assertIn("id", videos[0])

    def test_upload_video_raises_error(self):
        with self.assertRaises((NotImplementedError, VideoUploadError)):
            self.client.upload_video("fake_path.mp4", "caption")
            
    def test_login_raises_error(self):
        with self.assertRaises((NotImplementedError, AuthenticationError)):
            self.client.login_with_credentials("user", "pass")

if __name__ == '__main__':
    unittest.main()