class Calculator:
    def __init__(self):
        self.input = input("Enter a number: ")
        self.operation = input("Enter an operation (add, subtract, multiply, divide): ")
        self.initial_value = 0
    
    def choices(self):
        if self.operation == "add" or self.operation == "+":
            self.add()
    
    def add(self):

            self.input = float(self.input)
            self.input2 = float(input("Enter another number to add: "))
            if i == 0:


            
    
if __name__ == "__main__":
    calc = Calculator()

    while True:
        try:
            run = calc.choices()
        except Exception as e:
            print("Error:", e)