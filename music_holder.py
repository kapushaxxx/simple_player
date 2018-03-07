class Music_Holder:
    def __init__(self, filename):
        self.filename = filename

    def method_for_test(self, a):
        return a - 5

    def print_name(self):
        print(self.filename)


if __name__ == "__main__":
    print(1)
    holder = Music_Holder('tests')
    if holder.method_for_test(5) != 0:
        print("ERROR")
        exit(0)
    print("SUCCESS")