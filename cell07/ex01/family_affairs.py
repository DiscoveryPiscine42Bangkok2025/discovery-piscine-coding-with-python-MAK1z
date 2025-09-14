def find_the_redheads(name_dict):
    return list(filter(lambda name: name_dict[name] == "red", name_dict))

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

print(find_the_redheads(dupont_family))