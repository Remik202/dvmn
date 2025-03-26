import file_operations
from faker import Faker
import random
import os

skills_files = 'skills.txt'

letters_mapping = {
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

def convert_to_runic(skill):
    return ''.join(letters_mapping.get(char, char) for char in skill)

def load_skills():
    with open(skills_files, 'r', encoding='utf8') as file:
        return [skill.strip() for skill in file]

def create_files(num_files, skills, fake):
    os.makedirs("result", exist_ok=True)

    for _ in range(num_files):
        selected_skills = random.sample(skills, 3)
        runic_skills = [convert_to_runic(skill) for skill in selected_skills]

        context = {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "job": fake.job(),
            "town": fake.city(),
            "strength": random.randint(3, 18),
            "agility": random.randint(3, 18),
            "endurance": random.randint(3, 18),
            "intelligence": random.randint(3, 18),
            "luck": random.randint(3, 18),
            "skill_1": runic_skills[0],
            "skill_2": runic_skills[1],
            "skill_3": runic_skills[2]
        }

        base_name = "result/form_"
        counter = 1
        while os.path.exists(f"{base_name}{counter}.svg"):
            counter += 1

        output_file_path = f"{base_name}{counter}.svg"

        file_operations.render_template("src/template.svg", output_file_path, context)
        print(f"Файл создан: {output_file_path}")

def main():
    fake = Faker("ru_RU")
    skills = load_skills()

    create_files(10, skills, fake)

if __name__ == "__main__":
    main()
