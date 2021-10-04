from selenium import webdriver

def main():
    path = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get("https://store.brandonsanderson.com/collections/signed-leatherbound-books/products/elantris-leather-bound-book?variant=32867344056400")

if __name__ == '__main__':
    main()