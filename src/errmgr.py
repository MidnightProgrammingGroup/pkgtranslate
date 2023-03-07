def help():
    print("pkgt [Arguments] {Package}")


def fatal(msg = ""):
    if msg == "":
        help()
        exit(1)
