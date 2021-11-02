#!/usr/bin/python3

def main():
	with open("numbers.txt", 'r') as file:
		data = file.read()

	summ = 0
	for line in data:
		if line.isdigit():
			summ += int(line)
	print(summ)


if __name__ == "__main__":
	main()