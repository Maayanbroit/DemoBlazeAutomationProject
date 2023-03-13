from selenium import webdriver
from selenium.webdriver.edge.service import Service


def get_edge_driver():
    edgedriver_path = 'C:/chromedriver/msedgedriver.exe'
    options = webdriver.EdgeOptions()
    service = Service(executable_path=edgedriver_path)
    driver = webdriver.Edge(service=service, options=options)
    options.add_argument("--disable-extensions")

    return driver