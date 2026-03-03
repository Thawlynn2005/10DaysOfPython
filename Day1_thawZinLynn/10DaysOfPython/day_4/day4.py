#Exercises Day 4
#No1
result = 'Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python'
print(result)

#No2
result = 'Coding' + ' ' + 'For' + ' ' + 'All'
print(result)

#No3 #No4
company = "Coding For All"
print(company)

#No5
print(len(company))

#No6
print(company.upper())

#No7
print(company.lower())

#No8
print(company.capitalize())
print(company.title())
print(company.swapcase())

#No9
print(company[7:])

#No10
print(company.find("Coding"))
print(company.index("Coding"))

#No11
print(company.replace("Coding", "Python"))

#No12
text = "Python for Everyone"
print(text.replace("Everyone", "All"))

#No13
print(company.split())

#No14
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(", "))

#No15
print(company[0])

#No16
print(len(company) - 1)

#No17
print(company[10])

#No18
text = "Python For Everyone"
acronym = ''.join(word[0] for word in text.split())
print(acronym)

#No19
text = "Coding For All"
acronym = ''.join(word[0] for word in text.split())
print(acronym)

#No20
print(company.index("C"))

#No21
print(company.index("F"))

#No22
text = "Coding For All People"
print(text.rfind("l"))

#No23
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.find("because"))

#No24
print(sentence.rindex("because"))

#No25 #No26
start = sentence.find("because")
end = sentence.rindex("because") + len("because")
print(sentence[start:end])

#No27
print(company.startswith("Coding"))

#No28
print(company.endswith("coding"))

#No29
text = "   Coding For All      "
print(text.strip())

#No30
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

#No31
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("# ".join(libraries))

#No32
print("I am enjoying this challenge.\nI just wonder what is next.")

#No33
print("Name\tAge\tCountry")
print("Asabeneh\t250\tFinland")

#No34
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

#No35
a, b = 8, 6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")