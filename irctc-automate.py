#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 08:14:55 2017

@author: chandramouli
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login():
    browser.get('https://www.irctc.co.in/eticketing/loginHome.jsf')
    WebDriver.wait(driver,60).until(EC.presence_of_element_located((By.name,'j_username'))).send_keys(IRCTC_USERNAME)
    browser.find_element_by_name('j_password').send_keys(IRCTC_PASSWORD)
    browser.find_element_by_name('j_captcha').send_keys(IRCTC_CAPTCHA)

def planjourney():
    WebDriverWait(driver,60).until(EC.presence_of_element_located((By.name,'jpform:fromStation'))).send_keys(FROM_STATION)
    browser.find_element_by_id('jpform:toStation').send_keys(TO_STATION)
    browser.find_element_by_id('jpform:journeyDateInputDate').send_keys(DATE)
    waituntil('10:59:50')
    browser.find_element_by_id('jpform:jpsubmnit').click()
    WebDriverWait(driver,60).until(EC.presence_of_element_located((By.name,'quota')))[-1].click()
    browser.find_element_by_id('cllink-%s-%s-%s'%(TRAIN_NO,CLASS,CLASS_INDEX)).click()

def filldetails():
    WebDriverWait(driver, 60).until(EC.title_contains('Book Ticket'))
    for name, el in zip(NAMES, driver.find_elements_by_class_name('psgn-name')):
        el.send_keys(name)
    for age, el in zip(AGES, driver.find_elements_by_class_name('psgn-age')):
        el.send_keys(age)
    for gender, el in zip(GENDERS, driver.find_elements_by_class_name('psgn-gender')):
        Select(el).select_by_value(gender)
    for berth, el in zip(BERTHS, driver.find_elements_by_class_name('psgn-berth-choice')):
        Select(el).select_by_value(berth)
    browser.find_element_by_id('addPassengerForm:autoUpgrade').click()
    browser.find_element_by_id('addPassengerForm:onlyConfirmedBerths').click()

def sbi():
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID,'PREFERRED')))[-1].click()
    browser.find_element_by_id('validate').click()
    WebDriverWait(driver, 60).until(EC.presence_of_element_located(By.ID,'username'))).send_keys(SBI_USERNAME)
    browser.find_element_by_id('label2').send_keys(SBI_PASSWORD)
    browser.find_element_by_id('Button2').click()
    
if __name__ = '__main__':
    profile = webdriver.FirefoxProfile()
    profile.set_preference('webdriver.load.strategy', 'unstable')
    waituntil('10:59:00')
    browser = webdriver.Chrome(profile)
    login()
    planjourney()
    filldetails()
    sbi()
