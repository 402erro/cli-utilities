class Calculator:
    def __init__(self):
        self.input = float(input("Enter a number: "))
        self.operation = input("Enter an operation (add, subtract, multiply, divide): ")
        self.initial_value = 0
    
    def choices(self):
        if self.operation == "add" or self.operation == "+":
            self.add()
    
    def add(self):
        counter = 0
        """
          Ask the user for the number they'd like to add (store this as a second variable)
          Is this the first calculation? - counter = 0
          Take that and add the two numbers
          Is this the second calculation? - counter >=1 
          Add the third number, etc
        """

        while True:
            if counter == 0:
                input2 = float(input("Enter another number: "))
                self.initial_value += self.input + input2
                counter += 1
                print(self.initial_value)
            elif counter >= 1:
                input3 = float(input("Enter another number: "))
                self.initial_value += input3
                print(self.initial_value)
            


if __name__ == "__main__":
    calc = Calculator()

    while True:
        try:
            run = calc.choices()
        except Exception as e:
            print("Error:", e)