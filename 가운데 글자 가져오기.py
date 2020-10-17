

"""단어 s의 가운데 글자를 반환하는 함수, solution을
만들어보세여 단어의 길이가 짝수라면 가운데 두글자를 반환"""

def solution(str):
    if len(str) % 2:
        return str[len(str) // 2]
    else:
        return str[(len(str) // 2) - 1: len(str) // 2 + 1]

    return str

print(solution("power"))