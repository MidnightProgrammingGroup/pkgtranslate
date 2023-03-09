def help():
    print("pkgt [Arguments] {Package}\n----------Arguments----------\n-U(--update):  Updates list\n-h(--help):    Show's this message")


def fatal(msg = ""):
    if msg == "":
        help()
        exit(1)
