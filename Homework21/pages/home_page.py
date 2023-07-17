class Homepage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://guest:welcome2qauto@qauto.forstudy.space")
