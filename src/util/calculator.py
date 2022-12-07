class Calculator:
    operators = '+-/*^'  # такие операции

    def my_parse(self, string):  # раскалываем строку на операнды, скобки и числа в список
        ret = []
        num = ''
        for char in string:
            if char in '.0123456789':
                num += char
            elif char in self.operators or char in '()':
                if len(num) > 0:
                    ret.append(num)
                    num = ''
                ret.append(char)
        if len(num) > 0:
            ret.append(num)
        return ret

    def solver2operand(self, expression):  # тут ждем 3 элемента в списке, из которых первый и последний - числа,
        # а средний - операнд (просто операция над 2-мя числами)
        match expression[1]:
            case '+':
                return str(float(expression[0]) + float(expression[2]))
            case '-':
                return str(float(expression[0]) - float(expression[2]))
            case '*':
                return str(float(expression[0]) * float(expression[2]))
            case '/':
                return str(float(expression[0]) / float(expression[2]))
            case '^':
                return str(pow(float(expression[0]), float(expression[2])))
            case _:
                print('Ошибка в выражении (1)')
                exit()
        return '0'

    def get_operand_index(self, expression, op):  # возвращаем первый сначала списка индекс элемента op
        try:
            return expression.index(op)
        except ValueError:  # а вот тут not op in expression
            return -1

    def iterator(self, expression):  # тут обрабатываем список элементов выражения
        if expression[0] == '-':  # это если в первое число в выражении отрицательное
            expression.insert(0, '0')
        match len(expression):
            case 0:
                return []  # такого не должно быть, но все же...
            case 1:
                return expression  # такого тоже не должно быть, но все же...
            case 2:
                return expression[0]  # и такого не должно быть, но все же...
            case 3:
                return [str(self.solver2operand(expression))]  # тут все просто - 3 элемента - просто считаем их
            case _:
                mypos = self.get_operand_index(expression, ')')  # ищем закр. скобку
                if mypos == -1:  # скобок нет!

                    mypos = self.get_operand_index(expression, '^')  # ^ - самая высокая приоритет
                    if mypos == -1 or \
                            ((self.get_operand_index(expression,
                                                     '*') < mypos)  # умножение и деление - равны по приоритету
                             and self.get_operand_index(expression,
                                                        '*') > -1):  # но, тут вычисляем, кто из */ стоит первым
                        mypos = self.get_operand_index(expression, '*')  #
                    if mypos == -1 or \
                            ((self.get_operand_index(expression, '/') < mypos)  #
                             and self.get_operand_index(expression, '/') > -1):  #
                        mypos = self.get_operand_index(expression, '/')  # вот прям до сюда вычисляем...

                    if mypos == -1:  # если */^ не нашли - то + или -
                        mypos = self.get_operand_index(expression, '-')
                    if mypos == -1:
                        mypos = self.get_operand_index(expression, '+')

                    if mypos > -1:
                        expression[mypos - 1] = str(
                            self.solver2operand(expression[mypos - 1:mypos + 2]))  # вычисляем операцию
                        # с наивысшим приоритетом
                        # результат пишем в ячейку
                        # первого операнда
                        del expression[mypos:mypos + 2]  # удаляем из списка операцию и второй операнд
                        return expression
                else:  # обработка скобок
                    open_bracket = mypos  # ищем откр. скобку - берем сначала позицию закр. скобку
                    for i in range(mypos, -1, -1):  # идем от закр. скобки назад, пока не надем откр. скобку
                        if expression[i] == '(':
                            open_bracket = i  # типа нашли
                            break

                    # делим список на 3 куска
                    expr1 = expression[0:open_bracket]  # то, что до откр. скобки
                    expr3 = expression[mypos + 1:]  # то, что после закр. скобки

                    expr2 = self.iterator(expression[open_bracket + 1:mypos])  # а вот середину без скобок - засовываем
                    # сами в себя (оно там само разберется, что к чему)
                    expression = []  # восстанавливаем наш бедный список

                    if len(expr1) > 0:  # вдруг впереди только одна скобка и была
                        expression.extend(expr1)
                    expression.extend(expr2)
                    if len(expr3) > 0:  # вдруг позади только одна скобка и была
                        expression.extend(expr3)
                    return expression

    def my_solver(self, expression):
        while len(expression) > 1:  # должен остаться один элемент в списке - ответ
            expression = self.iterator(expression)
        return expression

    def calculate(self, expession):  # Главный вызывающий метод
        return self.my_solver(self.my_parse(expession))[0]
