from typing import List


def generate_parens(n: int) -> List[str]:
    if n == 0:
        return [""]
    if n == 1:
        return ["()"]
    result = []
    for i in range(n):
        for left in generate_parens(i):
            for right in generate_parens(n - i - 1):
                result.append(f"({left}){right}")
    return result


# print(generate_parens(3))
