from faker import Faker
import random
import os


FAKE = Faker("ru_RU")

SKILLS = [
    "Стремительный прыжок",
    "Электрический выстрел",
    "Ледяной удар",
    "Стремительный удар",
    "Кислотный взгляд",
    "Тайный побег",
    "Ледяной выстрел",
    "Огненный заряд",
]

LETTERS = {
    'а': 'а͠',
    'б': 'б̋',
    'в': 'в͒͠', 
    'г': 'г͒͠', 
    'д': 'д̋',
    'е': 'е͠', 
    'ё': 'ё͒͠', 
    'ж': 'ж͒', 
    'з': 'з̋̋', 
    'и': 'и',
    'й': 'й͒͠', 
    'к': 'к̋̋', 
    'л': 'л̋͠', 
    'м': 'м͒͠', 
    'н': 'н͒',
    'о': 'о̋', 
    'п': 'п̋͠', 
    'р': 'р̋͠', 
    'с': 'с͒', 
    'т': 'т͒',
    'у': 'у͒͠', 
    'ф': 'ф̋̋', 
    'х': 'х͒͠', 
    'ц': 'ц̋', 
    'ч': 'ч̋͠',
    'ш': 'ш͒͠', 
    'щ': 'щ̋', 
    'ъ': 'ъ̋͠', 
    'ы': 'ы̋͠', 
    'ь': 'ь̋',
    'э': 'э͒͠', 
    'ю': 'ю̋͠', 
    'я': 'я̋', 
    'А': 'А͠', 
    'Б': 'Б̋',
    'В': 'В͒͠', 
    'Г': 'Г͒͠', 
    'Д': 'Д̋', 
    'Е': 'Е', 
    'Ё': 'Ё͒͠',
    'Ж': 'Ж͒', 
    'З': 'З̋̋', 
    'И': 'И', 
    'Й': 'Й͒͠', 
    'К': 'К̋̋',
    'Л': 'Л̋͠', 
    'М': 'М͒͠', 
    'Н': 'Н͒', 
    'О': 'О̋', 
    'П': 'П̋͠',
    'Р': 'Р̋͠', 
    'С': 'С͒', 
    'Т': 'Т͒', 
    'У': 'У͒͠', 
    'Ф': 'Ф̋̋',
    'Х': 'Х͒͠', 
    'Ц': 'Ц̋', 
    'Ч': 'Ч̋͠', 
    'Ш': 'Ш͒͠', 
    'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 
    'Ы': 'Ы̋͠', 
    'Ь': 'Ь̋', 
    'Э': 'Э͒͠', 
    'Ю': 'Ю̋͠',
    'Я': 'Я̋', 
    ' ': ' '
}


def read_file(filename):
    with open(filename, encoding="utf8") as file_:
        return file_.read()


def write_to_file(filename, content):
    with open(filename, "w", encoding="utf8") as file_:
        return file_.write(content)


def render_template(template_path, output_path, context):
    content = read_file(template_path)

    for key, value in context.items():
        content = content.replace("{%s}" % key, str(value))

    write_to_file(output_path, content)


def main():
    os.makedirs("result", exist_ok=True)
    for i in range(1, 11):
        sampled_skills = random.sample(SKILLS, 3)
        runic_skills = []
        for skill in sampled_skills:
            for letter in skill:
                skill = skill.replace(letter, LETTERS[letter])
            runic_skills.append(skill)
        context = {
            "first_name": FAKE.first_name_male(),
            "last_name": FAKE.last_name_male(),
            "job": FAKE.job(),
            "town": FAKE.city(),
            "strength": random.randint(3, 18),
            "agility": random.randint(3, 18),
            "endurance": random.randint(3, 18),
            "intelligence": random.randint(3, 18),
            "luck": random.randint(3, 18),
            "skill_1": runic_skills[0],
            "skill_2": runic_skills[1],
            "skill_3": runic_skills[2],
        }
        render_template(
            "src/template.svg", "result/form_{}.svg".format(i), context
        )


if __name__ == "__main__":
    main()
