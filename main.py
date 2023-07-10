import calendar
import datetime

year = datetime.date.today().year

get_month = calendar.Calendar(firstweekday=0).monthdays2calendar

months = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август', 9: 'Сентябрь ', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}

week_header = "Понедельник	Вторник	Среда	Четверг	Пятница	Суббота	Воскресенье"

empty_week = [[(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]]

with open("calendar.tsv", 'w') as file:
	for i in range(1, 13, 4):
		first, second, third, fourth = i, i + 1, i + 2, i + 3
		month_row = f'{"	" * 3}{months[first]}{"	" * 8}{months[second]}{"	" * 8}{months[third]}{"	" * 8}{months[fourth]}'
		weeks_row = f'{week_header}		' * 4

		first_month = get_month(year, first)
		second_month = get_month(year, second)
		third_month = get_month(year, third)
		fourth_month = get_month(year, fourth)

		number_of_weeks = max(len(x) for x in (first_month, second_month, third_month, fourth_month))

		first_month += empty_week if len(first_month) < number_of_weeks else []
		second_month += empty_week if len(second_month) < number_of_weeks else []
		third_month += empty_week if len(third_month) < number_of_weeks else []
		fourth_month += empty_week if len(fourth_month) < number_of_weeks else []

		head = month_row + "\n" + weeks_row + '\n'

		file.write(head)

		for i in range(number_of_weeks):
			row_first = "".join("	" if x[0] == 0 else str(x[0])+"	" for x in first_month[i])
			row_second = "".join("	" if x[0] == 0 else str(x[0])+"	" for x in second_month[i])
			row_third = "".join("	" if x[0] == 0 else str(x[0])+"	" for x in third_month[i])
			row_fourth = "".join("	" if x[0] == 0 else str(x[0])+"	" for x in fourth_month[i])
			file.write(f'{row_first}	{row_second}	{row_third}	{row_fourth}\n\n')
		file.write("\n" * 5)