import os, sys, errmgr

def update():
    # TODO: Implement, temporarily using built in test list
    os.system("mkdir " + os.getenv("HOME") + "/.local/share/pkgtranslate/ -p")
    with open(os.getenv("HOME") + "/.local/share/pkgtranslate/pkglist", "w") as ls:
        ls.write(",deb:Debian,fed:Fedora,arc:Arch,\ntestdeb:Debian,testfeb:Fedora,testarc:Arch")
# Get Everything After This Index
def geati(String, Substring, index):
    loop = 0
    while loop != index:
        String = String[String.find(Substring) + 1:]
        loop += 1
    return String
def gebti(String, Substring, index):
    loop = 0
    while loop != index:
        String = String[:String.find(Substring)]
        loop += 1
    return String


pkgs = []

if not os.path.exists(os.getenv("HOME") + "/.local/share/pkgtranslate/pkglist"):
    print("pkglist not found, updating...")
    update()
if len(sys.argv) == 1:
    print("Error: No not enough arguments")
    errmgr.fatal()
index = 0
for arg in sys.argv:
    index += 1
    if index == 1:
        continue
    elif arg[0] != "-":
        pkgs.append(arg)
    elif arg == "-U" or arg == "--update":
        update()
index = 1
with open(os.getenv("HOME") + "/.local/share/pkgtranslate/pkglist", "r") as ls:
    for ln in ls.readlines():
        if ln[0] == "#":
            continue
        for pkg in pkgs:
            while index != ln.count(":") + 1:
                if pkg in gebti(geati(ln, ",", index), ":", 1):
                    print("\nPackage Found!")
                    print("Searched Package: " + pkg)
                    index2 = 1
                    loop2 = 1
                    while loop2 != ln.count(":") + 1:
                        print(gebti(geati(ln, ":", index2), ",", 1) + " Package: ", end="")
                        print(gebti(geati(ln, ",", index2), ":", 1))
                        loop2 += 1
                        index2 += 1
#                else:
                index += 1
#                print(index)
