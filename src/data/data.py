class Data:
    # Класс - генератор данных

    expressions = [
        "2+2"
        , "3+3"
        , "12*3+3+5+2*2"
        , "1+2*(3+5)"
        , "15/(7-(1+1))*3-(2+(1+1))"
        , "2^5"
        , "-2*5"
        , "-2^5"
        , "2+2"
        , "1+2*3"
        , "1-2*3"
        , "1+2*3"
        , "(1+2)*3"
        , "1/2+1/3"
        , "1-22/22-2/2*2+1"
        , "-11+1"
    ]

    def __init__(self):
        self.counter = 0

    def __iter__(self):  # итератор
        return self

    def __next__(self):  # генератор данных
        if self.counter < len(self.expressions):
            self.counter += 1
            return self.expressions[self.counter - 1]
        else:
            raise StopIteration
