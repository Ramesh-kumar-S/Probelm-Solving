################################################################
#             UCSM GUI Automation Handler
#             Author : Ramesh Kumar Sekar
################################################################
import os
import signal
import subprocess
import sys
import time
import contextlib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DEFAULT_USERNAME = ""
DEFAULT_PASSWORD = ""


def register_signal_handlers():
    """Register signal handlers for SIGINT."""
    original_signal_handler = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    signal.signal(signal.SIGINT, original_signal_handler)


def get_credentials():
    """Get credentials from command-line arguments."""
    if len(sys.argv) == 1:
        print("\n\tPlease provide the Domain IP")
        print("\n\t<Script> <IP> <Username> <Password>")
        sys.exit(0)

    ip = sys.argv[1]

    if len(sys.argv) == 2:
        print("Proceeding with default credentials...")
        username = DEFAULT_USERNAME
        password = DEFAULT_PASSWORD
    else:
        username = sys.argv[2]
        password = sys.argv[3]

    return ip, username, password


class Chrome(object):
    """Class to handle UCSM browser automation."""

    def __init__(self, Path=None) -> None:
        """Initializes the  Chrome handler class"""
        self._chrome_options = self._get_chrome_options()
        self._path = Path
        self.logging_out = False
        self.driver = None

    @staticmethod
    def _get_chrome_options():
        chrome_options = Options()
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--ignore-ssl-errors')
        chrome_options.add_experimental_option("detach", True)
        return chrome_options

    @property
    def path(self):
        """Getter method for chromedriver path."""
        return self._path

    @path.setter
    def path(self, path):
        """Setter method for chromedriver path."""
        if not path:
            raise ValueError("Please specify the Valid Path")
        self._path = path

    def initializeDriver(self):
        # Get the current directory where the script is located
        current_directory = os.path.dirname(os.path.abspath(__file__))
        chrome_driver_path = os.path.join(
            current_directory, 'chromedriver.exe')
        service = Service(chrome_driver_path,
                          creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
        self.driver = webdriver.Chrome(
            service=service,
            options=self._chrome_options)

    def WebDriverWaitConfig(self, id, value=None, type=None):
        """Wait for an element to be present and interact with it."""
        try:
            if type != "Button":
                field = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, id)))
                field.send_keys(value)
            else:
                button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.ID, id)))
                button.click()
        except Exception as e:
            print(f"An error occurred: {e}")

    def LogOut(self):  # sourcery skip: extract-method
        """Log out from the application."""
        if not self.driver or self.logging_out:
            print("No driver found or already logging out...")
            return
        self.logging_out = True
        try:
            print("Logging out...")
            try:
                if self.driver.service.process is not None:
                    self.WebDriverWaitConfig("w56731", type="Button")
                    self.WebDriverWaitConfig(
                        "xform_TextButton_2", type="Button")
            except Exception as e:
                print(f"An error occurred during logout steps: {e}")
            time.sleep(10)
        except Exception as e:
            print(f"An error occurred during logout: {e}")
        finally:
            try:
                if self.driver:
                    self.driver.quit()
                    print("Logged out successfully.")
            except Exception as e:
                print(f"An error occurred while quitting the driver: {e}")
            self.driver = None

    def Login(self, Url, Username, Password):
        """Login to the application."""
        self.driver.get(Url)
        print(f'Opening {self.driver.title}')
        self.WebDriverWaitConfig(
            "form_TextBox_0", Username, type="textBox")
        self.WebDriverWaitConfig(
            "form_TextBox_1", Password, type="textBox")
        self.WebDriverWaitConfig("loginContainer_loginSubmit", type="Button")

        # Once the page is Opened, Keep it alive
        try:
            Exit = input("Please Enter 'exit' to terminate the program..... ")
            while Exit.lower() != "exit":
                Exit = input(
                    "Runnning...Please Enter 'exit' to terminate the program....")
                time.sleep(5)
            self.LogOut()
            sys.exit(0)
        except KeyboardInterrupt:
            print("\nProgram stopped by the user.")


def main():
    """Main function to handle the script execution."""
    register_signal_handlers()
    ip, username, password = get_credentials()

    ChromeHandler = Chrome()
    ChromeHandler.initializeDriver()

    try:
        with open(os.devnull, 'w') as devnull:
            with contextlib.redirect_stderr(devnull):
                ChromeHandler.Login(
                    f"https://{ip}", username, password)
    except Exception as e:
        print(f"An error occurred during login: {e}")
        if ChromeHandler and ChromeHandler.driver:
            ChromeHandler.LogOut()


if __name__ == "__main__":
    main()
