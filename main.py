import datetime
from application.db.people import get_employees
from application.salary import calculate_salary
import Wikipedia2PDF

if __name__ == '__main__':
    print(datetime.datetime.now().strftime('%Y-%m-%d'))
    get_employees()
    calculate_salary(0)

    # without specifying a filename
    Wikipedia2PDF.Wikipedia2PDF("https://en.wikipedia.org/wiki/Yuri_Gagarin")
    # output: Yuri_Gagarin.pdf
