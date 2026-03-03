#Exercises Level 1
#No1
empty_list = []

#No2
numbers = [1, 2, 3, 4, 5, 6, 7]

#No3
print(len(numbers))

#No4
first_item = numbers[0]
middle_item = numbers[len(numbers)//2]
last_item = numbers[-1]
print(first_item, middle_item, last_item)

#No5
mixed_data_types = ["Lewis", 20, 5.7, "Single", "Yangon"]

#No6
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

#No7
print(it_companies)

#No8
print(len(it_companies))

#No9
print(it_companies[0])
print(it_companies[len(it_companies)//2])
print(it_companies[-1])

#No10
it_companies[1] = "Alphabet"
print(it_companies)

#No11
it_companies.append("Intel")
print(it_companies)

#No12
it_companies.insert(len(it_companies)//2, "Tesla")
print(it_companies)

#No13
it_companies[0] = it_companies[0].upper()
print(it_companies)

#No14
joined_companies = "#;  ".join(it_companies)
print(joined_companies)

#No15
print("Google" in it_companies)

#No16
it_companies.sort()
print(it_companies)

#No17
it_companies.reverse()
print(it_companies)

#No18
print(it_companies[:3])

#No19
print(it_companies[-3:])

#No20
middle_index = len(it_companies)//2
print(it_companies[middle_index:middle_index+1])

#No21
it_companies.pop(0)
print(it_companies)

#No22
middle_index = len(it_companies)//2
it_companies.pop(middle_index)
print(it_companies)

#No23
it_companies.pop()
print(it_companies)

#No24
it_companies.clear()
print(it_companies)

#No25
del it_companies

#No26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
joined_list = front_end + back_end
print(joined_list)

#No27
full_stack = joined_list.copy()
redux_index = full_stack.index("Redux")
full_stack.insert(redux_index + 1, "Python")
full_stack.insert(redux_index + 2, "SQL")
print(full_stack)

#Exercises Level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_age = min(ages)
max_age = max(ages)
print(ages)
print(min_age, max_age)
ages.append(min_age)
ages.append(max_age)
print(ages)
ages.sort()
n = len(ages)
if n % 2 == 0:
    median = (ages[n//2 - 1] + ages[n//2]) / 2
else:
    median = ages[n//2]
print(median)
average = sum(ages) / len(ages)
print(average)
age_range = max(ages) - min(ages)
print(age_range)
print(abs(min_age - average))
print(abs(max_age - average))
#No1
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
length = len(countries)
middle = length // 2
if length % 2 == 0:
    print(countries[middle-1:middle+1])
else:
    print(countries[middle])
#No2
first_half = countries[:(len(countries)+1)//2]
second_half = countries[(len(countries)+1)//2:]
print(first_half)
print(second_half)
#No3
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
country1, country2, country3, *scandic_countries = countries
print(country1)
print(country2)
print(country3)
print(scandic_countries)