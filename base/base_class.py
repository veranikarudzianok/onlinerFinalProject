import datetime

class Base():
    def __init__(self, driver_g):
        self.driver_g = driver_g

    """Getting current URL"""
    def get_current_url(self):
        get_url = self.driver_g.current_url
        print('Current URL: ' + get_url)
        return get_url

    """Checking current URL"""
    def assert_current_url(self, expected_url):
        current_url = self.get_current_url()
        assert current_url == expected_url
        print('Current URL is correct')

    """Checking text"""
    def assert_word(self, word, result):
        value_word = word.text
        print('Text is:', value_word)
        assert value_word == result
        print('Text is correct')

    """Check product names"""
    def assert_product_names(self, name1, name2):
        assert name1 == name2
        print("Product name on Catalog and Comparison page match")

    """Screenshot"""
    def make_screenshot(self):
        current_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot ' + current_date + '.png'
        self.driver_g.save_screenshot('C:\\PyCharmProjects\\1\\screenshots\\' + name_screenshot)

