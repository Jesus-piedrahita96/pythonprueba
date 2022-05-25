import numbers


def read():
    numbers = []
    with open("./archivos/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = int(line)
            numbers.append(line)
    print(numbers)


def write():
    name = ["jesus", "mauricio", "jose", "jhon", "jorge", "piedrahita", "blanca"]
    with open("./archivos/name.txt", "a", encoding="utf-8") as f:
        for i in name:
            f.write(i)
            f.write("\n")


def run():
    #read()
    write()


if __name__ == '__main__':
    run()