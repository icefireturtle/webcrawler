import unittest
from crawl import normalize_url, get_h1_from_html

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

class TestCrawlH1(unittest.TestCase):
    def test_get_h1(self):
        input_html = "<html><body><h1>Welcome to Boot.dev</h1><main><p>Learn to code by building real projects.</p><p>This is the second paragraph.</p></main></body></html>"
        actual = get_h1_from_html(input_html)
        expected = "Welcome to Boot.dev"
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()