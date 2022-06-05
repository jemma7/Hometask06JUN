from selenium import webdriver
import pytest
from locators import LocatorsXpath
from rahulshettyacademy import Elements_rahulshettyacademy
from basepage import Base


@pytest.mark.usefixtures('set_up')
class TestsPositive(Base):
    def test_radio_button(self):
        driver = self.driver
        radio_button  = Elements_rahulshettyacademy.rad_but(self)
        assert radio_button == True

    def test_static_dropdown_search(self):
        driver = self.driver
        static_dropdwon  = Elements_rahulshettyacademy.static_drdown("ita")
        assert static_dropdwon == "Italy"

    def test_dynamic_dropdown_(self):
        driver = self.driver
        dynamic_dropdown  = Elements_rahulshettyacademy.dyn_drdown(self)
        dynamic_option1 = Elements_rahulshettyacademy.drdown_option1(self)
        assert dynamic_dropdown == True
        assert dynamic_option1 == "option1"

    def test_checkbox_(self):
        driver = self.driver
        checkbox  = Elements_rahulshettyacademy.checkbox(self)
        assert checkbox == "option1"

    def test_open_window(self):
        driver = self.driver
        open_window  = Elements_rahulshettyacademy.window(self)
        assert open_window == "QA Click Academy | Selenium,Jmeter,SoapUI,Appium,Database testing,QA Training Academy"

    def test_open_tab(self):
        driver = self.driver
        open_tab  = Elements_rahulshettyacademy.tab(self)
        assert open_tab == "Rahul Shetty Academy"

    # def test_open_alert(self):
    #     driver = self.driver

    def test_hide(self):
        driver = self.driver
        hide_button = Elements_rahulshettyacademy.hide(driver)
        assert hide_button == True

    def test_show(self):
        driver = self.driver
        show_button = Elements_rahulshettyacademy.show(self)
        assert show_button == True

    def test_scroll(self):
        driver = self.driver
        scroll_ = Elements_rahulshettyacademy.scroll_table(self)
        assert scroll_ == True

    def test_hover_over(self):
        driver = self.driver
        hover1 = Elements_rahulshettyacademy.hover_over1(self)
        hover2 = Elements_rahulshettyacademy.hover_over2(self)
        assert hover1 == True
        assert hover2 == True

    def test_iframe(self):
        driver = self.driver
        iframe_action = Elements_rahulshettyacademy.i_frame(self)
        assert iframe_action == True


        

