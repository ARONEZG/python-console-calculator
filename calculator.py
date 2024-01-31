
class ExpressionConverter:
    def __init__(self, string):
        self.expression = []
        self.__SetExpression(self.__TrimSpases(string))
    
    def __SetExpression(self, string):
        i = 0
        char_num = 0
        for char in string:
            if char == "+" or char == "-" or char == "*" or char == "/":
                 if len(string[char_num: i]) != 0:
                    self.expression.append(string[char_num: i])
                 self.expression.append(char)
                 char_num = i + 1
            i += 1
        i = len(string)
        for char in reversed(string):
            if char == "+" or char == "-" or char == "*" or char == "/":
                self.expression.append(string[i : len(string)])
                break
            i -= 1
        


    def __TrimSpases(self, string):
        new_string = ""
        for i in range(len(string)):
            if string[i] == " ":
                continue
            new_string += string[i]
        return new_string


class Calculator:

    def __init__(self):
        self.map = {}

    def __PutHistory(self, expression, result):
        new_string = ""
        for string in expression:
            new_string += " " + string
        self.map[new_string] = result

    def Calculate(self, expression):
        numbers = []
        operations = []
        i = 0
        while(i < len(expression)):
            if expression[i] == "+" or expression[i] == "-":
                operations.append(expression[i])
            elif expression[i] == "*" or expression[i] == "/":
                back_num = int(numbers[len(numbers) - 1])
                numbers.pop()
                if expression[i] == "*":
                    numbers.append(back_num * int(expression[i + 1]))
                if expression[i] == "/":
                    numbers.append(back_num / int(expression[i + 1]))
                i += 1
            else:
                numbers.append(int(expression[i]))
            i += 1
        if len(numbers) == len(operations) :
            if operations[0] == "-":
                numbers[0] = -numbers[0]
            operations = operations[1 : len(operations)]
        j = 0
        result = numbers[0]
        for i in range(len(operations)):
            if operations[j] == "+":
                result += numbers[i+1] 
            if operations[j] == "-":
                result -= numbers[i+1]
            j += 1
        self.__PutHistory(expression, result)
        return result
    
    def WriteHistory(self):
        history_txt = open("history.txt", "w")
        for element in self.map.items():
            key, value = element
            history_txt.write(key + " = " + str(value) + "\n")
            history_txt.write("\n")
        history_txt.close()
            
    
text = ""    
calculator = Calculator()
while True:
    print("Чтобы выйти введите <exit> \n")
    text = input("Введите выражение: \n")
    if (text == "exit"):
        break
    expression = ExpressionConverter(text).expression
    try:
        d = calculator.Calculate(expression)
    except:
        print("Некорректное выражение")
    else:
        print("Ответ:", d)
    

calculator.WriteHistory()