import random
import main as source
import json
import time


# JSON
def load_json(json_list: str) -> list[str]:
    with open(json_list, "r+") as json_file:
        return json.load(json_file)


def save_json(value: list[str], json_list: str) -> bool:
    with open(json_list, "w") as json_file:
        try:
            json.dump(value, json_file, indent=4, separators=(',', ': '))
            return True
        except SyntaxError:
            print(Exception)
            return False


# ***********************************************************************


# Methods
def method1(returned_string: str) -> str:
    test_list: list[int] = []
    for counter1 in range(11):
        test_list.append(random.randint(0, 9))
    for counter2 in range(len(test_list)):
        returned_string += str(test_list[counter2])
    return returned_string


def method2(returned_string: str) -> str:
    pos_dict: dict[int, int] = {}
    test_list: list[int] = []

    # Definir as posições e seus valores, tendo a chave como o número e o valor como a posição
    for counter1 in range(4):
        value: int = random.randint(0, 9)
        while True:
            pos: int = random.randint(0, 10)
            if pos in pos_dict.values():
                pass
            else:
                break
        pos_dict.update({value: pos})

    for counter2 in range(11):
        if pos_dict.get(counter2) is True:
            test_list.append(pos_dict.get(counter2))
        else:
            test_list.append(random.randint(0, 9))
    for counter3 in range(len(test_list)):
        returned_string += str(test_list[counter3])

    return returned_string


def method3_values_to_str(test_list: list[int], pos_dict: dict[int, int]) -> list[int]:
    for counter in range(11):
        if pos_dict.get(counter) is not None:
            test_list.append(pos_dict.get(counter))
        else:
            test_list.append(random.randint(0, 9))
    return test_list


def method3_values() -> dict[int, int]:
    pos_dict: dict[int, int] = {}

    for counter1 in range(2):
        pos = 9 + counter1
        value: int = random.randint(0, 9)
        pos_dict.update({pos: value})

    return pos_dict


def method3(returned_string: str, pos_dict: dict[int, int]) -> str:
    test_list: list[int] = []

    test_list = method3_values_to_str(test_list=test_list, pos_dict=pos_dict)

    for counter3 in range(len(test_list)):
        returned_string += str(test_list[counter3])

    return returned_string


# ***********************************************************************



# ***********************************************************************


def main(repeats: int, method: int) -> list[str]:
    timer = time.time()
    returned_list: list[str] = []
    pos_dict: dict[int, int] = method3_values()
    for counter1 in range(int(repeats)):
        json_list: list[str] = load_json(json_list="cpfs.json")
        while True:
            string_value: str = ""

            if method == 1:
                string_value = method1(returned_string=string_value)
            elif method == 2:
                string_value = method2(returned_string=string_value)
            elif method == 3:
                string_value = method3(returned_string=string_value, pos_dict=pos_dict)
            else:
                raise "Insert a valid method value."

            if source.main(value=string_value):
                if string_value not in json_list:
                    returned_list.append(string_value)
                    json_list.append(string_value)
                    save_json(value=json_list, json_list="cpfs.json")
                    break
                else:
                    pass
            else:
                pass
    print(f"It took {round(time.time() - timer, 2)} seconds to find all {repeats} CPF's using method {method}.")
    return returned_list


if __name__ == "__main__":
    # while True:
        # inputted_repeats: int = 0
        # inputted_method: int = 0
        #
        # try:
        #     inputted_repeats = int(source.clean_number(input("Quantidade de CPF's para gerar: ")))
        #     inputted_method = int(source.clean_number(input("Método usado: ")))
        #     break
        # except ValueError:
        #     pass

    for counter1 in range(3):
        for counter2 in range(100):
            main(repeats=100, method=counter1 + 1)
