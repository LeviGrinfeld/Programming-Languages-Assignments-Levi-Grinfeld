# 315407403
# לוי גרינפלד

# שאלה 1

def get_penta_num(n: int) -> int:
    return (n * (3 * n - 1)) // 2


def pentaNumRange(n1: int, n2: int) -> list:
    return [get_penta_num(i) for i in range(n1, n2)]



# שאלה 2

def sum_digit(n) -> int | str:
    str_n = str(n).strip()

    # בדיקת תקינות של מספר שלם (תומך גם בשלמים שליליים)
    if not (str_n.isdigit() or (str_n.startswith('-') and str_n[1:].isdigit())):
        return "invalid input"

    clean_digits = str_n.lstrip('-')
    return sum(int(digit) for digit in clean_digits)



# שאלה 3

def normalize_text(text: str) -> str:
    # הסרת רווחים, המרה לאותיות קטנות ומיון לפי ASCII
    return "".join(sorted(text.replace(" ", "").lower()))


def are_anagrams(text1: str, text2: str) -> bool:
    return normalize_text(text1) == normalize_text(text2)



# שאלה 4

GEMATRIA_DICT = {
    'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9,
    'י': 10, 'כ': 20, 'ך': 20, 'ל': 30, 'מ': 40, 'ם': 40, 'נ': 50, 'ן': 50,
    'ס': 60, 'ע': 70, 'פ': 80, 'ף': 80, 'צ': 90, 'ץ': 90, 'ק': 100, 'ר': 200,
    'ש': 300, 'ת': 400
}


def gematria(word: str) -> int:
    return sum(GEMATRIA_DICT.get(char, 0) for char in word)



# שאלה 5

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    # בדיקה יעילה בקפיצות של 6 (מדלג על כפולות של 2 ו-3)
    return all(n % i != 0 and n % (i + 2) != 0 for i in range(5, int(n ** 0.5) + 1, 6))


def get_twin_prime(p: int):
    if not is_prime(p):
        return None
    if is_prime(p + 2):
        return p + 2
    if is_prime(p - 2):
        return p - 2
    return None


def twin_primes_dict(n: int) -> dict:
    return {
        p: get_twin_prime(p)
        for p in range(2, n + 1)
        if is_prime(p) and get_twin_prime(p) is not None
    }



# שאלה 6

def add_3_dicts(d1: dict, d2: dict, d3: dict) -> dict:
    all_keys = set(d1.keys()) | set(d2.keys()) | set(d3.keys())

    # שמירה על ייחודיות הערכים ללא כפילויות תוך שמירה על סדר הופעתם המקורי
    return {
        key: tuple(dict.fromkeys(d[key] for d in (d1, d2, d3) if key in d))
        for key in all_keys
    }



# שאלה 7:

def multiply_by_2(x):
    return x * 2


def square(x):
    return x ** 2


def inverse(x):
    return 1 / x if x != 0 else None


math_functions = [multiply_by_2, square, inverse]


def apply_functions_to_collection(numbers, funcs: list) -> dict:
    return {
        func.__name__: [func(num) for num in numbers]
        for func in funcs
    }



# סקריפטים ראשיים (Main)

if __name__ == "__main__":
    # להרצת שאלה 2:
    # user_input = input("enter number:\n")
    # print(sum_digit(user_input))

    # להרצת שאלה 3:
    # t1 = input("enter first text:\n")
    # t2 = input("enter second text:\n")
    # if not t1.strip() or not t2.strip():
    #     print("invalid input")
    # else:
    #     print(are_anagrams(t1, t2))

    # להרצת שאלה 5:
    # user_input = input("enter number:\n").strip()
    # if not (user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit())):
    #     print("invalid input")
    # else:
    #     num = int(user_input)
    #     twin = get_twin_prime(num)
    #     print(twin if twin is not None else "invalid input")
    pass