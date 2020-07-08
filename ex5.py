revenue = int(input('Введите вашу выручку >>> '))
costs = int(input('Введите ваши издержки >>> '))
if revenue > costs:
    profitability = (((revenue - costs)/revenue) * 1000) // 10
    num_of_employees = int(input('Введите количество сотрудиков >>> '))
    profit_per_emp = (revenue - costs) / num_of_employees
    print(f"фирма получает прибыль, рентабельность фирмы - {profitability} %, прибыль фирмы в расчете на одного " +
          f"сотрудника = {profit_per_emp}")
else:
    print('фирма несёт убытки')

