from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.contrib.auth import get_user_model

User = get_user_model()


class SeleniumTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def setUp(self):
        self.user = User.objects.create_user(
            username='salfetka',
            email='salfetka@example.com',
            password='12ustal34'
        )

    def login(self):
        self.driver.get(f'{self.live_server_url}/login/')
        self.driver.find_element(By.ID, 'id_username').send_keys('salfetka')
        self.driver.find_element(By.ID, 'id_password').send_keys('12ustal34')
        self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    def test_login_and_profile_access(self):
        self.login()
        # Проверка наличия ссылки на личный кабинет
        profile_link = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.LINK_TEXT, 'Личный кабинет'))
        )
        assert profile_link is not None

    def test_profile_edit(self):
        self.login()
        # Переход в личный кабинет
        self.driver.find_element(By.LINK_TEXT, 'Личный кабинет').click()

        # Ждем загрузку формы и находим поле email
        email_input = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, 'id_email'))
        )
        email_input.clear()
        email_input.send_keys('salfetka_2@example.com')

        # Отправка формы (предположим, есть кнопка type="submit")
        self.driver.find_element(By.CSS_SELECTOR, 'form button[type="submit"]').click()

        # Повторно зайти в личный кабинет и проверить email
        self.driver.find_element(By.LINK_TEXT, 'Личный кабинет').click()
        updated_email = self.driver.find_element(By.ID, 'id_email').get_attribute('value')

        assert updated_email == 'salfetka_2@example.com'
