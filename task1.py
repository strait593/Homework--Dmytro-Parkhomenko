def get_info(filename: str) -> list[float]:

    with open(filename, "r") as file:

        return file.readlines()

def get_salaries(salaries: float) -> list[float]:

    return [float(sal.strip().split(",")[1]) for sal in salaries]

raw_data = get_info("C:\\Users\\dparh\\Desktop\\Data Science\\module4\\homework_mdl4\\salaries\\salaries.txt")
salaries = get_salaries(raw_data)

sum_up = sum(salaries)
average = sum(salaries) / len(salaries)

print(f"Sum of all salaries is {sum_up} and the average is {average}")