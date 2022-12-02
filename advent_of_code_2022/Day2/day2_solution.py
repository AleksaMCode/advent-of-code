# A -       Rock        - X
# B -       Paper       - Y
# C -       Scissors    - Z
class RockPaperScissors:
    value: int

    def __init__(self, value):
        self.value = "XYZ".index(value)

    def __eq__(self, other) -> int:
        match (self.value - "ABC".index(other)) % 3:
            case 0:
                return self.value + 1 + 3
            case 1:
                return self.value + 1 + 6
            case _:
                return self.value + 1

    def __ne__(self, other) -> int:
        other = "ABC".index(other)
        match self.value:
            case 0:
                return (other - 1) % 3 + 1
            case 1:
                return 3 + other + 1
            case _:
                return 6 + (other + 1) % 3 + 1

    @staticmethod
    def function1(you, opponent):
        return you == opponent

    @staticmethod
    def function2(you, opponent):
        return you != opponent

    @staticmethod
    def parse_input(file_name):
        total_score1 = 0
        total_score2 = 0
        with open(file_name) as file:
            for line in file:
                values = line.strip().split(' ')
                opponent = values[0]
                you = RockPaperScissors(values[1])
                total_score1 += RockPaperScissors.function1(you, opponent)
                total_score2 += RockPaperScissors.function2(you, opponent)
        print(total_score1, total_score2)
