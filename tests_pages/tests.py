from selenium import webdriver
import pytest
from locators import LocatorsXpath
from rahulshettyacademy import Elements_rahulshettyacademy
from basepage import Base


@pytest.mark.usefixtures('set_up')
class TestsPositive(Base):
    def test_radio_button(self):
        driver = self.driver
        radio_button  = Elements_rahulshettyacademy.rad_but(driver)
        assert radio_button == True

    def test_static_dropdown_search(sdriver):
        driver = self.driver
        static_dropdwon  = Elements_rahulshettyacademy.static_drdown("ita")
        assert static_dropdwon == "Italy"

    def test_dynamic_dropdown_(self):
        driver = self.driver
        dynamic_dropdown  = Elements_rahulshettyacademy.dyn_drdown(driver)
        dynamic_option1 = Elements_rahulshettyacademy.drdown_option1(driver)
        assert dynamic_dropdown == True
        assert dynamic_option1 == "option1"

    def test_checkbox_(self):
        driver = self.driver
        checkbox  = Elements_rahulshettyacademy.checkbox(driver)
        assert checkbox == "option1"

    def test_open_window(self):
        driver = self.driver
        open_window  = Elements_rahulshettyacademy.window(driver)
        assert open_window == "QA Click Academy | Selenium,Jmeter,SoapUI,Appium,Database testing,QA Training Academy"

    def test_open_tab(self):
        driver = self.driver
        open_tab  = Elements_rahulshettyacademy.tab(driver)
        assert open_tab == "Rahul Shetty Academy"

    # def test_open_alert(self):
    #     driver = self.driver

    def test_hide(self):
        driver = self.driver
        hide_button = Elements_rahulshettyacademy.hide(driver)
        assert hide_button == True

    def test_show(self):
        driver = self.driver
        show_button = Elements_rahulshettyacademy.show(driver)
        assert show_button == True

    def test_scroll(self):
        driver = self.driver
        scroll_ = Elements_rahulshettyacademy.scroll_table(driver)
        assert scroll_ == True

    def test_hover_over(self):
        driver = self.driver
        hover1 = Elements_rahulshettyacademy.hover_over1(driver)
        hover2 = Elements_rahulshettyacademy.hover_over2(driver)
        assert hover1 == True
        assert hover2 == True

    def test_iframe(self):
        driver = self.driver
        iframe_action = Elements_rahulshettyacademy.i_frame(driver)
        assert iframe_action == True


        

