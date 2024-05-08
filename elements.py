class WhatsAppXpathElements:
    def __init__(self):
        self.qr_code_for_login = (
            '//*[@id="app"]/div/div/div[2]/div[1]/div/div[2]/div/canvas'
        )
        self.logged_in_whatsapp_web = '//*[@id="side"]'
        self.search_bar = '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p'
        self.search_button = (
            '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/button'
        )
        self.selected_contact = (
            '//*[@id="pane-side"]/div/div/div/div[2]/div/div/div/div[2]'
        )
        self.message_box = (
            '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
        )
        self.send_button = (
            '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span'
        )
        self.plus_button = (
            '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span'
        )
        self.send_document = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/li[3]/div'
        self.send_image = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/li[1]/div'
        self.message_history = '//*[@id="main"]/div[3]/div/div[2]/div[2]'
        self.status_tab = (
            '//*[@id="side"]/header/div[2]/div/span/div[1]/div/ul/li[2]/div'
        )
        self.new_chat_button = '//*[@id="side"]/header/div[2]/div/span/div[2]/div/span'
        self.profile_icon = '//*[@id="side"]/header/div[1]/div/img'
        self.settings = '//*[@id="side"]/header/div[2]/div/span/div[3]/div/span'
        self.logout_button = (
            '//*[@id="side"]/header/div[2]/div/span/div[3]/div/span/div/ul/li[4]/div'
        )
