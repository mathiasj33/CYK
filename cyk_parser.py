from ast import AST


class CYKParser:
    def __init__(self, grammar, dictionary):
        self.grammar = grammar
        self.dictionary = dictionary

    @staticmethod
    def from_files(grammar_file, dict_file):
        grammar = CYKParser.create_dict(grammar_file)
        dictionary = CYKParser.create_dict(dict_file)
        return CYKParser(grammar, dictionary)

    @staticmethod
    def create_dict(file):
        d = {}
        with open(file) as infile:
            for line in infile:
                arr = line.split('->')
                left = arr[0].strip()
                right = arr[1].strip()
                d[right] = left  # Bottom-up parsing
        return d

    def parse(self, sentence):
        words = sentence.split(' ')
        chart = self.create_chart(len(words))
        self.fill_chart_with_dictionary(chart, words)
        print(chart)

    def create_chart(self, length):
        chart = []
        for i in range(length):
            column = [None] * (i+1)
            chart.append(column)
        return chart

    def fill_chart_with_dictionary(self, chart, words):
        for i in range(len(chart)):
            chart[i][i] = self.dictionary[words[i]]


if __name__ == '__main__':
    parser = CYKParser.from_files('grammar.txt', 'dictionary.txt')
    parser.parse("time flies like an arrow")
