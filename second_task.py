def get_cats_info(path):
    cats = []
    with open(path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                cat_id, name, age = line.split(',')
                cats.append({
                    'id': cat_id,
                    'name': name,
                    'age': int(age)
                })
    return cats
print(get_cats_info("test_2.txt"))