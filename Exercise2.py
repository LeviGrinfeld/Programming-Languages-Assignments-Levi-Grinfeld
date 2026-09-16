# 315407403
# לוי גרינפלד

import math
import time
from functools import reduce
from datetime import datetime, timedelta


# שאלה 1

# 1.1 פונקציית למבדה לינארית
linear_function = lambda x: (x / 2) + 2

# יצירת רשימה מ-0 עד 10000 באמצעות פונקציית העל map
linear_list = list(map(linear_function, range(10001)))

# 1.2 סכימת איברי הרשימה בעזרת פונקציית על
sum_higher_order = reduce(lambda acc, x: acc + x, linear_list)

# 1.3 השוואת זמני ריצה בין פונקציית על לשיטה אימפרטיבית
def compare_times():
    start_ho = time.perf_counter()
    reduce(lambda acc, x: acc + x, linear_list)
    time_ho = time.perf_counter() - start_ho

    start_imp = time.perf_counter()
    sum_imp = 0
    for val in linear_list:
        sum_imp += val
    time_imp = time.perf_counter() - start_imp

    return time_ho, time_imp

# 1.4 סכימה וקריאה ללמבדה בפונקציית על אחת בלבד
one_liner_functional = reduce(lambda acc, x: acc + linear_function(x), range(10001), 0)




# שאלה 2

# חלוקה לרשימות זוגיים ואי-זוגיים באמצעות פונקציית העל filter
even_numbers = list(filter(lambda x: x % 2 == 0, range(1, 1001)))
odd_numbers = list(filter(lambda x: x % 2 != 0, range(1, 1001)))

# 2.1 הגדרת שתי פונקציות למבדה
even_lambda = lambda acc, next_val: acc * next_val
# שימוש בחילוק שלמים // כדי למנוע גלישה של float בחישובים גדולים
odd_lambda = lambda acc, next_val: (acc // 2 + 2) + next_val + 2

# 2.2 הרצת הפונקציה המתאימה עבור כל אחת מהרשימות בעזרת פונקציית העל
even_result = reduce(even_lambda, even_numbers)
odd_result = int(reduce(odd_lambda, odd_numbers))

# 2.3 סכימת תוצאת הרשימות באמצעות פונקציית על
total_even_odd_sum = reduce(lambda a, b: a + b, [even_result, odd_result])



# שאלה 3

def is_armstrong(n: int) -> bool:
    if not isinstance(n, int) or n <= 0:
        return False
    digits = str(n)
    k = len(digits)
    return sum(map(lambda d: int(d) ** k, digits)) == n


def armstrong_range(n1: int, n2: int) -> list:
    return list(filter(is_armstrong, range(n1, n2)))



# שאלה 4

def generate_dates(start_date_str: str, num_dates: int, skip_days: int) -> list:
    base_date = datetime.strptime(start_date_str, "%d/%m/%Y")
    return list(map(
        lambda i: (base_date + timedelta(days=i * skip_days)).strftime("%d/%m/%Y"),
        range(num_dates)
    ))



# שאלה 5

# 5.א Closure המחזיר פונקציית חזקה לפי המעריך
def power_function(exp: int):
    return lambda base: base ** exp


# 5.ב החזרת אובייקט map של פונקציות חזקה
def generate_power_funcs(n: int):
    return map(power_function, range(n))


# 5.ג קירוב טיילור ל-e^x ללא לולאות וללא רשימות
def taylor_e_x(x: float, n: int) -> float:
    funcs_map = generate_power_funcs(n)
    # שימוש ב-enumerate על גבי האיטרטור ללא יצירת רשימה
    return reduce(
        lambda acc, item: acc + (item[1](x) / math.factorial(item[0])),
        enumerate(funcs_map),
        0.0
    )



# שאלה 6

def task_manager():
    tasks = {}

    def add_task(task: str, status: str = "incomplete"):
        tasks[task] = status

    def get_tasks():
        return tasks.copy()

    def complete_task(task: str):
        if task in tasks:
            tasks[task] = "complete"

    return {
        'add_task': add_task,
        'get_tasks': get_tasks,
        'complete_task': complete_task
    }



# שאלה 7

# 7.א פונקציות טהורות לעיבוד טקסט
def clean_spaces(text: str) -> str:
    return text.strip()


def capitalize_text(text: str) -> str:
    return text.title()


def add_stars(text: str) -> str:
    return f"***{text}***"


# 7.ב ניהול ה-Pipeline
def create_pipeline():
    return lambda x: x


def add_to_pipeline(pipeline_fn, new_fn):
    return lambda x: new_fn(pipeline_fn(x))



# סקריפטים ראשיים (Main)

if __name__ == "__main__":
    # להרצת שאלה 3:
    # num_input = input("enter number:\n").strip()
    # if not num_input.isdigit() or int(num_input) <= 0:
    #     print("invalid input")
    # else:
    #     print(armstrong_range(1, int(num_input)))

    # להרצת שאלה 5:
    # n = int(input("Enter number of powers:\n"))
    # result = generate_power_funcs(n)
    # print(type(result))
    # base = int(input("Enter base:\n"))
    # print(tuple(map(lambda f: f(base), result)))

    # להרצת שאלה 7:
    # pipeline = create_pipeline()
    # pipeline = add_to_pipeline(pipeline, clean_spaces)
    # pipeline = add_to_pipeline(pipeline, capitalize_text)
    # pipeline = add_to_pipeline(pipeline, add_stars)
    # text_input = input("enter text:\n")
    # if not text_input.strip():
    #     print("invalid input")
    # else:
    #     print(pipeline(text_input))
    pass