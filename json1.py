import json
json_string = '{"name":"gulu","age":19}'

python_object = json.loads(json_string)
print(type(python_object))
print(python_object)