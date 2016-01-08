
def receiver():
    print("Ready to receive")
    while True:
        n = (yield)
        print("Got %s" % n)

def catch_and_increment():
    total = 0
    print("Ready to receive")
    while True:
        n = (yield) or 0
        total += n
        print("i got %s" % n)
        print("total is %s" % total)
