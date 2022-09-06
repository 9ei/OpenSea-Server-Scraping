import requests, random, time, json, threading, warnings, re, fnmatch, os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(executable_path=r'C:\Users\Ruthless Economy PC\Desktop\Gemini Webdriver\chromedriver.exe')
full = []

browser.get("https://opensea.io/rankings")
clean = browser.page_source
collections = re.findall(",\"slug\":\"(.*?)\",\"logo\"", clean)
collections = list(dict.fromkeys((collections)))
count = len(collections)

while count > -1:
    count = count - 1
    full = ("https://opensea.io/collection/" + collections[count])
    browser.get(full)
    clean = browser.page_source

    floor = re.findall("unit\":\"(.*?)\"},", clean)
    servers = re.findall("href=\"https://discord.gg/(.*?)\" rel=\"nofollow noopener\"", clean)
    gate = len(servers)

    if gate > 0:
        server = ("https://discord.gg/" + servers[0])
        print(full, server, floor[1], "ETH floor price")
