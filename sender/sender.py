from abc import abstractmethod


class Sender:

    @abstractmethod
    def send_message(self, message, receiver_url, headers=None):
        pass

    @abstractmethod
    def send(self):
        pass
