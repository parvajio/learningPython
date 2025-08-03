class computer:

    def config(self):
        print("i5, 16gb, 1tb")

com1 = computer()
com2 = computer()

# print(type(com1))
computer.config(com1)
computer.config(com2)

com2.config()