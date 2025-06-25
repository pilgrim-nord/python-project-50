import json


def input_data(data):
    with open(data, "r") as file:
        parsed_data = json.load(file)
        return parsed_data



# def main():
    # file1 = input_data("gendiff/inputs/file1.json")
    # file2 = input_data("gendiff/inputs/file2.json")
    #
    # print(file1)
    # print(file2)
    #

# if __name__ == "__main__":
#     main()

