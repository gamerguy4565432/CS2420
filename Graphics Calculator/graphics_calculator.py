from graphics import *

class Stack:
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity

        self.items = []
        self.output = []
        self.switching = {'+': 1, '-':1, '*': 2, '/': 2, '^':3}


    def isEmpty(self):
        if self.top == -1:
            return True

        else:
            return False


    def peek(self):
        return self.items[-1]


    def popItem(self):
        if not self.isEmpty():
            self.top -= 1
            return self.items.pop()
        else:
            return "$"
    

    def pushItem(self, op):
        self.top += 1
        self.items.append(op)

    
    def isOperand(self, ch):
        if ch == '+' or ch == '-' or ch == '*' or ch == '/' or ch == ')' or ch == '(':
            return False
        
        else:
            return True
        


    def notGreater(self, i):
        try:
            a = self.switching[i]
            b = self.switching[self.peek()]

            return True if a <= b else False
        
        except KeyError:
            return False
        
    
    def infixToPostFix(self, exp):
        for i in exp:
            if self.isOperand(i):
                self.output.append(i)

            elif i == '(':
                self.pushItem(i)

            elif i == ')':
                while((not self.isEmpty()) and self.peek() != '('):
                    a = self.popItem()
                    self.output.append(a)

                if((not self.isEmpty()) and self.peek() != '('):
                    return -1
                
                else:
                    self.popItem()

            else:
                while not self.isEmpty() and self.notGreater(i):
                    self.output.append(self.popItem())

                self.pushItem(i)

        
        while not self.isEmpty():
            self.output.append(self.popItem())

        
        return self.output
    
    def eOperand(self, ch):
        if ch == '+' or ch == '-' or ch == '*' or ch == '/' or ch == ')' or ch == '(' or ch == 'x':
            return False
        
        else:
            return True
        

    
    def evaluatePostfix(self, postfix):
        new_list = []
        x_list = []

        for i in range(len(postfix)):
            if self.isOperand(postfix[i]):
                new_list.append(postfix[i])

            else:
                j = len(new_list)
                if postfix[i] == '*':
                    operand = new_list[j - 2] * new_list[j - 1]
                    new_list.pop(-1)
                    new_list.pop(-1)
                    new_list.insert(0, operand)

                if postfix[i] == "/":
                    operand = new_list[j - 1] / new_list[j - 2]
                    new_list.pop(-1)
                    new_list.pop(-1)
                    new_list.insert(0, operand)

                if postfix[i] == "+":
                    operand = new_list[j - 2] + new_list[j - 1]
                    new_list.pop(-1)
                    new_list.pop(-1)
                    new_list.insert(0, operand)

                if postfix[i] == "-":
                    operand = new_list[j - 2] - new_list[j - 1]
                    new_list.pop(-1)
                    new_list.pop(-1)
                    new_list.insert(0, operand)
        
        print(new_list)
        return new_list[0]
    

def reset(prompt):
    if prompt == "Reset":
        return True

    return False


def calculate(prompt):
    if prompt == "Calculate":
        return True

    return False

def seemyhistory(prompt):
    if prompt == "See My History":
        return True

    return False


def plot(prompt):
    if prompt == "Plot":
        return True

    return False


def graph(prompt):
    if prompt == "Graph":
        return True

    return False

def exit(prompt):
    if prompt == "Exit":
        return True

    return False

def Create():
    s = ''

    for i in range(129):
        a = chr(i)
        s += '[' + '"' + a + '"' + '], '

    return self


def Terminator():
    print("Thank you for your time, Good Bye!")
    quit()


def main():
    items = []

    prompt = input("Welcome to the Graphics Calculator. What would you like to do? [Calculate] [Exit]")

    if prompt == "Debug":
        check = 1
        username = input("Please enter your UserName: ")
        user_name = "jorda"
        if username != user_name:
            check = 0

            for i in range(3):
                username = input("Error: User not found. Please try again")

                if username == user_name:
                    check = 1
                    break

        if check == 0:
            print("You entered the wrong Username. Goodbye!")
            Terminator()



        password = input("Please enter the Password")
        pass_word = "passGo!"

        if pasword != pass_word:
            check = 0
            for i in range(3):
                password = input("The is not correct. Please try again")

                if password == pass_word:
                    check = 1
                    break


        if check == 0:
            print("You entered the wrong Password. Goodbye!")
            Terminator()

        prompt = input("Please enter your given command. [Create] [TestInPos]")

        if prompt == "Create":
            print(Create())
            Terminator()


        if prompt == "TestInPos":
            s = Stack(10)
            prompt = input("Enter what you would like to convert")
            print(s.infixToPostFix(prompt))
            Terminator()

    calculateV = calculate(prompt)
    exitV = exit(prompt)
    prompted = False

    if calculateV == True:
        prompted = True

    elif exitV == True:
        prompted = True

    while prompted == False:
        prompt = input("The is not a valid input. Please try again. [Calculate] [See My History] [Reset] [Exit]")
        calculateV = calculate(prompt)
        exitV = exit(prompt)

        if calculateV == True:
            prompted = True

        elif exitV == True:
            prompted = True


    if calculateV == True:
        s = Stack(10)

        while calculateV == True:

            prompt = input("Please state what you would ike to do next: [Plot] [Graph] [Reset] [Exit]")

            resetV = reset(prompt)
            exitV = exit(prompt)
            plotV = plot(prompt)
            graphV = graph(prompt)

            if exitV == True:
                Terminator()

            if resetV == True:
                s = Stack(10)
                print("List has ben reset")


            if plotV == True:
                plotT = input("Please input the values you would ike to plot. ")
                item = s.infixToPostFix(plotT)
                st = ""

                for i in range(len(item)):
                    st += item[i]

                for i in range(len(item)):
                    if item[i].isdigit():
                        item[i] = float(item[i])


                print("Here is your new expresssion: " + st)
                items.append(item)


            if graphV == True:
                win = GraphWin("Results", 1920, 1000)
                win.setBackground(color="black")

                XLOW = -200.0
                XHIGH = +200.0
                YLOW = -200.0
                YHIGH = +200.0
                XINC = 1.0

                win.setCoords(XLOW, YLOW, XHIGH, YHIGH)

                points = []
                i = 0
                x = XLOW
                while x < XHIGH:
                    post = []
                    for i in range(len(items)):
                        for j in range(len(items[i])):
                            if items[i][j] == 'x':
                                post.append(x)

                            else:
                                post.append(items[i][j])

                    y = s.evaluatePostfix(post)
                    point = Point(int(x), int(y))
                    points.append(point)
                    x2 = x + XINC
                    post2 = []

                    for i in range(len(items)):
                        for j in range(len(items[i])):
                            if items[i][j] == 'x':
                                post2.append(x2)

                            else:
                                post2.append(items[i][j])

                    y2 = s.evaluatePostfix(post2)
                    point = Point(int(x2), int(y2))
                    points.append(point)
                    x += XINC

                i = 0
                for i in range(0, len(points) - 1):
                    line = Line(points[i], points[i + 1])
                    line.setOutline(color="red")
                    line.setWidth(10)

                    line.draw(win)


                win.getMouse()
                win.close()

    Terminator()



if __name__ == '__main__':
    main()
    
