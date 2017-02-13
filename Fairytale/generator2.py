import random

beginning = ['he ', 'she ', 'it ', 'there ', 'the ', 'a ', 'an ']

class Markov(object):

    def __init__(self, order):
        self.order = order
        self.group_size = self.order + 1
        self.text = None
        self.graph = {}
        return

    def train(self, filename):
        self.text = file(filename).read().split()
        self.text = self.text + self.text [: self.order]

        for i in range(0, len (self.text) - self.group_size):
            key = tuple (self.text [i:i + self.order])
            value = self.text [i + self.order]
            if key in self.graph:
                self.graph[key].append(value)
            else:
                self.graph[key] = [value]
        return

    def generate(self,length):
        index = random.randint (0,(len(self.text) - self.order))
        result = self.text[index: index + self.order]

        for i in range (length):
            state = tuple (result[len(result) - self.order:])
            next_word = random.choice(self.graph[state])
            result.append(next_word)

        for i in range (length):
            state = tuple (result[len(result) - self.order:])
            first_word = random.choice(self.graph[state])
            result.append(first_word)

        #if first_word in beginning:
        #    print
            #first = " ".join(result[self.order:])

        first = random.choice(beginning)

        text = " ".join (result [self.order:])
        print "Once upon a time " + first + text + " and they lived happily ever after."


print "\n"'\033[1m'+"FAIRYTALE GONE BAD"+'\033[0m'

fairytale = Markov(2)
fairytale.train('fairytales2.txt')
fairytale.generate(98)

print "\n"


#http://il.pycon.org/2016/static/sessions/omer-nevo.pdf
