import bfi
with open('hello.bf', 'r') as file:
    bf = file.read()
bfi.interpret(bf)