class StringSplit:
    def __init__(self, text: str):
        self.message_strings = []
        self.counter: int = 0
        self.text = text

    def string_splitting(self):
        while self.counter < len(self.text):
            storage: int = self.counter + 1024

            for i in range(storage, self.counter):
                if self.text[i] == "!" or self.text[i] == " " or self.text[i] == "." or self.text[i] == "?":
                    storage = i
                    break

            self.message_strings.append(self.text[self.counter:storage])
            self.counter = storage + 1

        return self.message_strings
