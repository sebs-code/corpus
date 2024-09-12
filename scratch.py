from decorators import do_twice


@do_twice
def hello_world(name):
    print(f'Hello {name}')

test = hello_world('Sebastian')
breakpoint()
test == None



