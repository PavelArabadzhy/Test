from page.main_page import MainPage
from data.data import BaseData



def test_open_garage(browser):
    mp = MainPage(browser, 'https://qauto.forstudy.space/')
    mp.auth_by_url(BaseData.baseLogin, BaseData.basePassword, BaseData.host)
    mp.BUTTON()
    mp.add()
    mp.add_car1()
    mp.mlg_1()
    mp.lastbut()
    assert mp.is_url_changed('https://guest:welcome2qauto@qauto.forstudy.space/panel/garage')

