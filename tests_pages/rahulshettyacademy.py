from lib2to3.pgen2 import driver
from webbrowser import open_new_tab
from selenium import webdriver
from locators import LocatorsXpath
from selenium.webdriver.common.action_chains import ActionChains
import pytest
import basepage
from time import sleep

class Elements_rahulshettyacademy:
    def __init__(self, driver):
        self.driver = driver
        self.radio_button = LocatorsXpath.radio_button
        self.static_dropdown  = LocatorsXpath.static_dropdown
        self.dynamic_dropdown = LocatorsXpath.dynamic_dropdown
        self.dropdown_option1 = LocatorsXpath.dropdown_option1
        self.check_box = LocatorsXpath.checkbox
        self.open_window = LocatorsXpath.open_window
        self.open_tab = LocatorsXpath.open_tab
        self.alert_search = LocatorsXpath.alert_search
        self.alert_button = LocatorsXpath.alert_button
        self.confirm_button = LocatorsXpath.confirm_button
        self.hide_button = LocatorsXpath.hide_button
        self.show_button = LocatorsXpath.show_button
        self.hide_show_displayed = LocatorsXpath.hide_show_displayed
        self.scroll = LocatorsXpath.scroll
        self.hover = LocatorsXpath.hover
        self.hover_top = LocatorsXpath.hover_top
        self.hover_reload  = LocatorsXpath.hover_reload 
        self.iframe = LocatorsXpath.iframe
        self.in_iframe = LocatorsXpath.in_iframe
    
    def rad_but(self):
        radio1 = self.driver.find_element_by_xpath(self.radio_button)
        radio1.click()
        radio1_selected = radio1.is_selected()
        return radio1_selected, radio1.get_attribute("value")

    def static_drdown(self,text):
        static_dropdown = self.driver.find_element_by_xpath(self.static_dropdown)
        static_dropdown.send_keys(text)
        static_dropdown.click()


    def dyn_drdown(self):
        dynamic_dropdown = self.driver.find_element_by_xpath(self.dynamic_dropdown)
        dynamic_dropdown.click()

    def drdown_option1(self):
        dropdown_option1 = self.driver.find_element_by_xpath(self.dropdown_option1)
        dropdown_option1.click()

    def checkbox(self):
        checkbox = self.driver.find_element_by_xpath(self.check_box)
        checkbox.click()
        checkbox_selected = checkbox.is_selected()
        return checkbox_selected, checkbox.get_attribute("value")
    
    def window(self):
        parent_window = driver.current_window_handle
        print(parent_window)
        opwindow = self.driver.find_element_by_xpath(self.open_window)
        opwindow.click()
        all_windows = driver.window_handles
        print(all_windows)
        for window in all_windows:
            if window != parent_window:
                driver.switch_to.window(window)
                if self.driver.title == "QA Click Academy | Selenium,Jmeter,SoapUI,Appium,Database testing,QA Training Academy":
                    return self.driver.title
                self.driver.close()

    def tab(self):
        parent_window = driver.current_window_handle
        print(parent_window)
        optab = self.driver.find_element_by_xpath(self.open_tab)
        optab.click()
        all_windows = driver.window_handles
        print(all_windows)
        for window in all_windows:
            if window != parent_window:
                driver.switch_to.window(window)
                if self.driver.title == "Rahul Shetty Academy":
                    return self.driver.title
                self.driver.close()

    def alert(self,text):
        alertSearch = self.driver.find_element_by_xpath(self.alert_search)
        alertSearch.send_keys(text)
        alert_but = self.driver.find_element_by_xpath(self.alert_button)
        alert_but.click()
        alert_ = self.driver.switch_to.alert()
        enter_your_name = alert_.text
        if enter_your_name == "Hello Jemma, share this practice page and share your knowledge":
            return enter_your_name

    def alert_confirm(self,text):
        alertSearch = self.driver.find_element_by_xpath(self.alert_search)
        alertSearch.send_keys(text)
        confirm = self.driver.find_element_by_xpath(self.confirm_button)
        confirm.click()
        alert_ = self.driver.switch_to.alert()
        enter_your_name = alert_.text
        if enter_your_name == "Hello Jemma, Are you sure you want to confirm?":
            return enter_your_name

    def hide(self):
        hide = self.driver.find_element_by_xpath(self.hide)
        hide.click()
        return hide.get_attribute("value")

    def show(self):
        show = self.driver.find_element_by_xpath(self.show)
        show.click()
        return show.get_attirbute("value")

    def scroll_table(self):
        table_scroll = self.driver.find_element_by_xpath(self.scroll)
        self.driver.execute_script("window.scrollTo(0, 1080)",table_scroll)


    def hover_over1(self):
        hover_button = self.driver.find_element_by_xpath(self.hover)
        actions = ActionChains(driver)
        actions.move_to_element(hover_button).perform()
        sleep(1)
        top = self.driver.find_element_by_xpath(self.hover_top)
        top.click()
    
    def hover_over2(self):
        hover_button = self.driver.find_element_by_xpath(self.hover)
        actions = ActionChains(driver)
        actions.move_to_element(hover_button).perform()
        sleep(1)
        reload = self.driver.find_element_by_xpath(self.hover_reload)
        reload.click()
    
    def i_frame(self):
        self.driver.execute_script("window.scrollTo(0, 1080)","")
        self.driver.switch_to.iframe(self.iframe)
        part_in_iframe = self.driver.find_element_by_xpath(self.in_iframe)
        part_in_iframe.click()
        part_in_iframe.is_dplayed()


        






