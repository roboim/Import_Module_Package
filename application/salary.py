from application.db.people import workers

tax = 13
def calculate_salary(id_request):
    for worker in workers:
        if id_request == 0 or id_request == worker['id']:
            print(f"Сотрудник {worker['name']} получает после вычета налога "
                  f"{worker['gross_salary']*(100-tax)/100} руб.\n")


if __name__ == '__main__':
    calculate_salary(0)