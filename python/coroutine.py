def print_name(prefix):
    print("Searching prefix: {}".format(prefix))
    try:
        while True:
            name = (yield)
            if prefix in name:
                print(name)
    except GeneratorExit:
        print("Closing coroutine!!")


corou = print_name("Dear")

corou.__next__()

corou.send("Atul")
corou.send("Dear Atul")
corou.send("Dear 123 dsad")
corou.close()
