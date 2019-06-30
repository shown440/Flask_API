import ast

my_dict = {
    "name": "SHIFULLAH",
    "designation": "VP",
    "manager_id": "7839",
    "date_of_birth": "16-03-1988",
    "salary": "5000",
    "commission": "2000",
    "department_no": "10"
}

my_text = str(my_dict)
print(my_text)
print(type(my_text))

text_to_dict = ast.literal_eval(my_text)
print(text_to_dict)
print(type(text_to_dict))