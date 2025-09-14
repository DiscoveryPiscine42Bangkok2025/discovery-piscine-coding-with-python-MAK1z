def array_of_names(name_dict):
    name_list = []
    for name, last in name_dict.items():
        full = f"{name.capitalize()} {last.capitalize()}"
        name_list.append(full)
    return name_list

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}

print(array_of_names(persons))