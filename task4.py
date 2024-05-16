def calculate_average(*args):
    if not args:
        return None
    return sum(args) / len(args)

if __name__ == "__main__":
    print("Среднее арифметическое:", calculate_average(10, 20, 30))