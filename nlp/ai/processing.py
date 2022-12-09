import en_core_web_lg


class Processing:
    def __init__(self, text: str):
        self.text = text

        self.keywords = []
        self.results_text = []
        self.results_label = []

        self.nlp = en_core_web_lg.load()
        self.doc = self.nlp(self.text)

    async def processing(self):
        for entity in self.doc.ents:
            self.results_text.append(entity.text)
            self.results_label.append(entity.label_)

        for i in range(len(self.results_label)):
            if self.results_label[i] == "PERSON" or self.results_label[i] == "ORG":
                self.keywords.append(self.results_text[i])

        return self.keywords
