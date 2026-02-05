import unittest
from crawl import normalize_url

class TestCrawlHTTPS(unittest.TestCase):
    def test_normalize_url(self):
        input_url = "https://blog.boot.dev/path"
        actual = normalize_url(input_url)
        expected = "blog.boot.dev/path"
        self.assertEqual(actual, expected)

class TestCrawlHTTPSSlash(unittest.TestCase):
    def test_normalize_url(self):
        input_url = "https://blog.boot.dev/path/"
        actual = normalize_url(input_url)
        expected = "blog.boot.dev/path"
        self.assertEqual(actual, expected)

class TestCrawlHTTP(unittest.TestCase):
    def test_normalize_url(self):
        input_url = "http://blog.boot.dev/path"
        actual = normalize_url(input_url)
        expected = "blog.boot.dev/path"
        self.assertEqual(actual, expected)

class TestCrawlHTTPSlash(unittest.TestCase):
    def test_normalize_url(self):
        input_url = "http://blog.boot.dev/path/"
        actual = normalize_url(input_url)
        expected = "blog.boot.dev/path"
        self.assertEqual(actual, expected)

class TestCrawlHTTPWWW(unittest.TestCase):
    def test_normalize_url(self):
        input_url = "http://www.blog.boot.dev/path"
        actual = normalize_url(input_url)
        expected = "blog.boot.dev/path"
        self.assertEqual(actual, expected)

class TestCrawlHTTPWWWSlash(unittest.TestCase):
    def test_normalize_url(self):
        input_url = "http://www.blog.boot.dev/path/"
        actual = normalize_url(input_url)
        expected = "blog.boot.dev/path"
        self.assertEqual(actual, expected)

class TestCrawlHTTPSWWW(unittest.TestCase):
    def test_normalize_url(self):
        input_url = "https://www.blog.boot.dev/path"
        actual = normalize_url(input_url)
        expected = "blog.boot.dev/path"
        self.assertEqual(actual, expected)

class TestCrawlHTTPSWWWSlash(unittest.TestCase):
    def test_normalize_url(self):
        input_url = "https://www.blog.boot.dev/path/"
        actual = normalize_url(input_url)
        expected = "blog.boot.dev/path"
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()