# 315407403
# לוי גרינפלד

import sys
import time
import itertools

# הגדלת עומק הרקורסיה עבור יצירה וסכימה של 1000 איברים
sys.setrecursionlimit(3000)


# שאלה 1

# 1.1 רקורסיה רגילה
def build_numbers(n: int = 1000) -> tuple:
    if n < 1:
        return ()
    return build_numbers(n - 1) + (n,)


# 1.2 רקורסיה זנבית
def build_numbers_tail(n: int = 1000, current: int = 1, acc: tuple = ()) -> tuple:
    if current > n:
        return acc
    return build_numbers_tail(n, current + 1, acc + (current,))



# שאלה 2

# 2.1 רקורסיה רגילה
def sum_values(values: tuple) -> int:
    if not values:
        return 0
    return values[0] + sum_values(values[1:])


# 2.2 רקורסיה זנבית
def sum_values_tail(values: tuple, acc: int = 0) -> int:
    if not values:
        return acc
    return sum_values_tail(values[1:], acc + values[0])



# שאלה 3

# 3.1 רקורסיה רגילה בעזרת אלגוריתם אוקלידס
def gcd(a: int, b: int) -> int:
    return a if b == 0 else gcd(b, a % b)


def lcm(a: int, b: int) -> int:
    return (a * b) // gcd(a, b)


# 3.2 רקורסיה זנבית
def lcm_tail(a: int, b: int, candidate: int = 0) -> int:
    step = max(a, b)
    if candidate == 0:
        candidate = step
    if candidate % a == 0 and candidate % b == 0:
        return candidate
    return lcm_tail(a, b, candidate + step)



# שאלה 4

# 4.1 רקורסיה רגילה
def is_palindrome_number(n: int) -> bool:
    s = str(abs(n))
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome_number(int(s[1:-1])) if len(s[1:-1]) > 0 else True


# 4.2 רקורסיה זנבית
def reverse_number_tail(n: int, acc: int = 0) -> int:
    if n == 0:
        return acc
    return reverse_number_tail(n // 10, acc * 10 + (n % 10))


def is_palindrome_number_tail(n: int) -> bool:
    n = abs(n)
    return n == reverse_number_tail(n, 0)



# שאלה 5

FINAL_LETTERS = {
    'ך': 'כ',
    'ם': 'מ',
    'ן': 'נ',
    'ף': 'פ',
    'ץ': 'צ'
}

def normalize_char(ch: str) -> str:
    lower_ch = ch.lower()
    return FINAL_LETTERS.get(lower_ch, lower_ch)


def clean_text(text: str) -> str:
    if not text:
        return ""
    head = normalize_char(text[0]) if text[0].isalnum() else ""
    return head + clean_text(text[1:])


# 5.1 רקורסיה רגילה
def is_clean_palindrome(text: str) -> bool:
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return is_clean_palindrome(text[1:-1])


def is_palindrome_alphanumeric(text: str) -> bool:
    return is_clean_palindrome(clean_text(text))


# 5.2 רקורסיה זנבית
def is_clean_palindrome_tail(text: str, left: int = 0, right: int = None) -> bool:
    if right is None:
        right = len(text) - 1
    if left >= right:
        return True
    if text[left] != text[right]:
        return False
    return is_clean_palindrome_tail(text, left + 1, right - 1)


def is_palindrome_alphanumeric_tail(text: str) -> bool:
    cleaned = clean_text(text)
    return is_clean_palindrome_tail(cleaned)



# שאלה 6

def sortedzip(list_of_lists: list):
    # מיון הרשימות לפי הדרישה המפורשת (sorted ולא sort)
    sorted_lists = [sorted(sub) for sub in list_of_lists]

    def zip_rec(lists):
        if not lists or any(len(sub) == 0 for sub in lists):
            return []
        heads = tuple(sub[0] for sub in lists)
        tails = [sub[1:] for sub in lists]
        return [heads] + zip_rec(tails)

    return zip_rec(sorted_lists)



# שאלה 7

# 7.1 רקורסיה רגילה
def count_repeats(text: str, ch: str) -> int:
    if not text or text[0] != ch:
        return 0
    return 1 + count_repeats(text[1:], ch)


def encode_rle(text: str) -> str:
    if not text:
        return ""
    count = count_repeats(text, text[0])
    return f"{text[0]}{count}" + encode_rle(text[count:])


# 7.2 רקורסיה זנבית
def count_repeats_tail(text: str, ch: str, acc: int = 0) -> int:
    if not text or text[0] != ch:
        return acc
    return count_repeats_tail(text[1:], ch, acc + 1)


def encode_rle_tail(text: str, acc: str = "") -> str:
    if not text:
        return acc
    count = count_repeats_tail(text, text[0])
    return encode_rle_tail(text[count:], acc + f"{text[0]}{count}")



# גנרטורים - שאלה 1

# 1.א יצירת מערך 0-10000
def create_numbers_eager():
    start = time.perf_counter()
    arr = list(range(10001))
    elapsed = time.perf_counter() - start
    return arr, elapsed, sys.getsizeof(arr)


def create_numbers_lazy():
    start = time.perf_counter()
    gen = (i for i in range(10001))
    elapsed = time.perf_counter() - start
    return gen, elapsed, sys.getsizeof(gen)


# 1.ב לקיחת 5000 האיברים הראשונים
def take_first_half_eager(numbers):
    start = time.perf_counter()
    sliced = numbers[:5000]
    elapsed = time.perf_counter() - start
    return sliced, elapsed, sys.getsizeof(sliced)


def take_first_half_lazy(numbers_gen):
    start = time.perf_counter()
    sliced = (x for x in itertools.islice(numbers_gen, 5000))
    elapsed = time.perf_counter() - start
    return sliced, elapsed, sys.getsizeof(sliced)



# גנרטורים - שאלה 2

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    return all(n % i != 0 and n % (i + 2) != 0 for i in range(5, int(n ** 0.5) + 1, 6))


def primes_generator():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1



# גנרטורים - שאלה 3

def taylor_generator(x: float):
    n = 0
    current_term = 1.0
    total_sum = 1.0
    yield total_sum

    while True:
        n += 1
        current_term *= x / n
        total_sum += current_term
        yield total_sum



# סקריפטים ראשיים (Main)

if __name__ == "__main__":
    # להרצת שאלה 5:
    # text_input = input("enter text:\n")
    # if not text_input.strip():
    #     print("invalid input")
    # else:
    #     print(is_palindrome_alphanumeric(text_input))

    # להרצת שאלה 7:
    # text_input = input("enter text:\n")
    # if not text_input.strip():
    #     print("invalid input")
    # else:
    #     print(encode_rle(text_input))

    # להרצת גנרטורים שאלה 3:
    # gen = taylor_generator(2)
    # for _ in range(8):
    #     print(next(gen))
    pass