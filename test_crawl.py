import unittest
from crawl import normalize_url, get_h1_from_html, get_first_paragraph_from_html

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

class TestCrawlH1_1(unittest.TestCase):
    def test_get_h1(self):
        input_html = "<html><body><h1>Welcome to Boot.dev</h1><main><p>Learn to code by building real projects.</p><p>This is the second paragraph.</p></main></body></html>"
        actual = get_h1_from_html(input_html)
        expected = "Welcome to Boot.dev"
        self.assertEqual(actual, expected)

class TestCrawlH1_2(unittest.TestCase):
    def test_get_h1(self):
        input_html = "<html><body><h1>Test Title</h1></body></html>"
        actual = get_h1_from_html(input_html)
        expected = "Test Title"
        self.assertEqual(actual, expected)

class TestCrawlH1_3_Main(unittest.TestCase):
    def test_get_h1(self):
        input_html = "<html><body><main><h1>In the main test nested</h1><p>Some other test</p></main></body></html>"
        actual = get_h1_from_html(input_html)
        expected = "In the main test nested"
        self.assertEqual(actual, expected)

class TestCrawlParagraph_1(unittest.TestCase):
    def test_get_first_paragraph_from_html(self):
        input_html = "<html><body><h1>Welcome to Boot.dev</h1><main><p>Learn to code by building real projects.</p><p>This is the second paragraph.</p></main></body></html>"
        actual = get_first_paragraph_from_html(input_html)
        expected = "Learn to code by building real projects."
        self.assertEqual(actual, expected)

class TestCrawlParagraph_2(unittest.TestCase):
    def test_get_first_paragraph_from_html(self):
        input_html = "<html><body><h1>Title</h1><main><p>Test Paragraph</p></main></body></html>"
        actual = get_first_paragraph_from_html(input_html)
        expected = "Test Paragraph"
        self.assertEqual(actual, expected)

class TestCrawlParagraph_3_Main(unittest.TestCase):
    def test_get_first_paragraph_from_html(self):
        input_html = "<html><body><p>Outside paragraph.</p><main><p>Main paragraph.</p></main></body></html>"
        actual = get_first_paragraph_from_html(input_html)
        expected = "Main paragraph."
        self.assertEqual(actual, expected)

class TestCrawlParagraph_4_No_Main(unittest.TestCase):
    def test_get_first_paragraph_from_html(self):
        input_html = "<html><body><p>Outside paragraph.</p><p>Main paragraph.</p></body></html>"
        actual = get_first_paragraph_from_html(input_html)
        expected = "Outside paragraph."
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()