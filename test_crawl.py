import unittest
from crawl import normalize_url, get_h1_from_html, get_first_paragraph_from_html, get_urls_from_html, get_images_from_html, extract_page_data

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

class TestCrawlURLs(unittest.TestCase):
    def test_get_urls_from_html_absolute(self):
        input_url = "https://blog.boot.dev"
        input_body= "<html><body><a href=\"https://blog.boot.dev\"><span>Boot.dev</span></a></body></html>"
        actual = get_urls_from_html(input_body, input_url)
        expected = ["https://blog.boot.dev"]
        self.assertEqual(actual, expected)

class TestCrawlURLs_None(unittest.TestCase):
    def test_get_urls_from_html_absolute(self):
        input_url = "https://testurldoesnotexist.com"
        input_body= "<html><body><img src=\"/logo.png\" alt=\"Logo\"></body></html>"
        actual = get_urls_from_html(input_body, input_url)
        expected = []
        self.assertEqual(actual, expected)

class TestCrawlURLs_Multi(unittest.TestCase):
    def test_get_urls_from_html_absolute(self):
        input_url = "https://testurldoesnotexist.com"
        input_body= "<html><body><a href=\"https://testurldoesnotexist.com/silly\"><br /><a href=\"https://testurldoesnotexist.com/testagain\"></body></html>"
        actual = get_urls_from_html(input_body, input_url)
        expected = ["https://testurldoesnotexist.com/silly", "https://testurldoesnotexist.com/testagain"]
        self.assertEqual(actual, expected)

class TestCrawlURLs_Multi_Relative(unittest.TestCase):
    def test_get_urls_from_html_relative(self):
        input_url = "https://testurldoesnotexist.com"
        input_body= "<html><body><a href=\"/silly\"><br /><a href=\"/testagain\"></body></html>"
        actual = get_urls_from_html(input_body, input_url)
        expected = ["https://testurldoesnotexist.com/silly", "https://testurldoesnotexist.com/testagain"]
        self.assertEqual(actual, expected)

class TestCrawlImages(unittest.TestCase):
    def test_get_images_from_html_relative(self):
        input_url = "https://blog.boot.dev"
        input_body = "<html><body><img src=\"/logo.png\" alt=\"Logo\"></body></html>"
        actual = get_images_from_html(input_body, input_url)
        expected = ["https://blog.boot.dev/logo.png"]
        self.assertEqual(actual, expected)

class TestCrawlImages_None(unittest.TestCase):
    def test_get_images_from_html_relative(self):
        input_url = "https://testurldoesnotexist.com"
        input_body = "<html><body><a href=\"https://testurldoesnotexist.com\"></body></html>"
        actual = get_images_from_html(input_body, input_url)
        expected = []
        self.assertEqual(actual, expected)

class TestCrawlImages_Multi(unittest.TestCase):
    def test_get_images_from_html_relative(self):
        input_url = "https://testurldoesnotexist.com"
        input_body = "<html><body><img src=\"/logo.png\" alt=\"Logo\"><br /><img src=\"/icon.png\" alt=\"Icon\"></body></html>"
        actual = get_images_from_html(input_body, input_url)
        expected = ["https://testurldoesnotexist.com/logo.png", "https://testurldoesnotexist.com/icon.png"]
        self.assertEqual(actual, expected)

class TestCrawlExtraction(unittest.TestCase):
    def test_extract_page_data_basic(self):
        input_url = "https://blog.boot.dev"
        input_body = """<html><body>
        <h1>Test Title</h1>
        <p>This is the first paragraph.</p>
        <a href="/link1">Link 1</a>
        <img src="/image1.jpg" alt="Image 1">
        </body></html>"""
        actual = extract_page_data(input_body, input_url)
        expected = {
            "url": "https://blog.boot.dev",
            "h1": "Test Title",
            "first_paragraph": "This is the first paragraph.",
            "outgoing_links": ["https://blog.boot.dev/link1"],
            "image_urls": ["https://blog.boot.dev/image1.jpg"]
        }
        self.assertEqual(actual, expected)

class TestCrawlExtraction_2(unittest.TestCase):
    def test_extract_page_data_basic(self):
        input_url = "https://www.testsitenotincluded.com"
        input_body = """<html><body>
        <img src="/moon.png" alt="Moon">
        <main>
        <a href="https://www.testsitenotincluded.com/gotalink">Gotalink</a>
        <h1>Need Batteries</h1>
        <p>Writing and things</p>
        <h2>Subheading</h2>
        <h1>Who did this?</h1>
        <p>More things</p>
        </main>
        </body></html>"""
        actual = extract_page_data(input_body, input_url)
        expected = {
            "url": "https://www.testsitenotincluded.com",
            "h1": "Need Batteries",
            "first_paragraph": "Writing and things",
            "outgoing_links": ["https://www.testsitenotincluded.com/gotalink"],
            "image_urls": ["https://www.testsitenotincluded.com/moon.png"]
        }
        self.assertEqual(actual, expected)

class TestCrawlExtraction_3(unittest.TestCase):
    def test_extract_page_data_basic(self):
        input_url = "http://blog.boot.dev"
        input_body = """<html>
        <p>Super paragraph</p><body>
        <h1>Title Tester</h1>
        <main>
        <img src="/sun.jpg" alt="Sun">
        <a href="/link11282">Link 11282</a>
        <p>This is some stuff here</p>
        </main>
        </body></html>"""
        actual = extract_page_data(input_body, input_url)
        expected = {
            "url": "http://blog.boot.dev",
            "h1": "Title Tester",
            "first_paragraph": "This is some stuff here",
            "outgoing_links": ["http://blog.boot.dev/link11282"],
            "image_urls": ["http://blog.boot.dev/sun.jpg"]
        }
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()