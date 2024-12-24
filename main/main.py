import requests
from concurrent.futures import ThreadPoolExecutor
import sys

class hooks:
    def __init__(self):
        self.hook = None
        self.msg = None

    def spam(self):
        json = {
            'content': self.msg
        }
        while True:
            r = requests.post(
                self.hook, 
                json=json
            )

            if r.status_code == 204:
                print(f"Successfully sent msg to | {self.hook}")

            else:
                print("Failed sending message")

    def sendmsg(self):
        json = {
            'content': self.msg
        }

        r = requests.post(
            self.hook, 
            json=json
        )

        if r.status_code == 204:
            print(f"Successfully sent msg to | {self.hook}")
            
        else:
            print("Failed sending message")

    def delete(self):
        r = requests.delete(
            self.hook
        )
        if r.status_code == 200:
            print("Successfully deleted webhook")

        else:
            print("Failed to delete webhook")

    def exit(self):
        sys.exit()

    def execute(self, func):
        with ThreadPoolExecutor(max_workers=10) as exec:
            exec.submit(func)

    def main(self):
        print("Choose from | 1. webhook spammer | 2. webhook deleter | 3. Send only a message | 4. Exit")
        choice = input("Your choice: ")

        self.hook = input('Webhook - ')
        if choice in ['1', '3']:
            self.msg = input('Message - ')

        options = {
            '1': self.spam,
            '2': self.delete,
            '3': self.sendmsg,
            '4': self.exit,
        }

        if choice in options:
            self.execute(options[choice])

hooks().main()
