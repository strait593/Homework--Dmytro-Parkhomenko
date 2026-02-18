def load_data(filename: str) -> list:
    with open(filename, 'r') as infos:

        return infos.readlines()

def clean_data(data: str) -> dict:

    id_codes = [str(id_code.split(",")[0]) for id_code in data]
    names = [str(name.split(",")[1]) for name in data]
    ages = [int(age.split(",")[2]) for age in data]

    return {
        "id":id_codes,
        "name":names,
        "age":ages
    }

info_cats = load_data("C:\\Users\\dparh\\Desktop\\Data Science\\module4\\homework_mdl4\\salaries\\cats_data.txt")

cleaned_data = clean_data(info_cats)

print(cleaned_data)