import requests
import threading
import sys

class WebhookTool:
    def __init__(self):
        def spam():
            webhook = input("Your webhook > ")
            msg = input("Your message > ")

            json = {
                'content': msg
            }
            while True:
                r = requests.post(webhook, json=json)
                if r.status_code == 204:
                    print(f"Successfully sent msg to | {webhook}")
                else:
                    print("Failed sending message")

                t = threading.Thread(target=spam)
                t.start()

        def sendmsg():
            webhook = input("Your webhook > ")
            msg = input("Your message > ")

            json = {
                'content': msg
            }

            r = requests.post(webhook, json=json)
            if r.status_code == 204:
                print(f"Successfully sent msg to | {webhook}")
            else:
                print("Failed sending message")

        def delete():
            webhook = input("Your webhook > ")

            n = requests.delete(webhook)
            if n.status_code == 200:
                print("Successfully deleted webhook")
            else:
                print("Failed to delete webhook")

        def exit_program():
            sys.exit()

        self.spam = spam
        self.delete = delete
        self.sendmsg = sendmsg
        self.exit_program = exit_program

        def main():
            print("Choose from | 1. webhook spammer | 2. webhook deleter | 3. Send only a message | 4. Exit")
            choice = input("Your choice: ")

            options = {
                '1': self.spam,
                '2': self.delete,
                '3': self.sendmsg,
                '4': self.exit_program,
            }

            if choice in options:
                options[choice]()

        self.main = main


if __name__ == "__main__":
    tool = WebhookTool()
    tool.main()
