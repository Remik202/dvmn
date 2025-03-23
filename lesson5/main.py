import file_operations
from faker import Faker
import random
import os

SKILLS_FILE = 'skills.txt'
LETTERS_MAPPING = {
    "Стремительный прыжок": "С͒т͒р̋͠е͠м͒͠ит͒е͠л̋͠ь̋н͒ы̋͠й͒͠ п̋͠р̋͠ы̋͠ж͒о̋к̋̋",
    "Электрический выстрел": "Э͒͠л̋͠е͠к̋̋т͒р̋͠ич̋͠е͠с͒к̋̋ий͒͠ в͒͠ы̋͠с͒т͒р̋͠е͠л̋͠",
    "Ледяной удар": "Л̋͠е͠д̋я̋н͒о̋й͒͠ у͒͠д̋а͠р̋͠",
    "Стремительный удар": "С͒т͒р̋͠е͠м͒͠ит͒е͠л̋͠ь̋н͒ы̋͠й͒͠ у͒͠д̋а͠р̋͠",
    "Кислотный взгляд": "К̋̋ис͒л̋͠о̋т͒н͒ы̋͠й͒͠ в͒͠з̋̋г͒͠л̋͠я̋д̋",
    "Тайный побег": "Т͒а͠й͒͠н͒ы̋͠й͒͠ п̋͠о̋б̋е͠г͒͠",
    "Ледяной выстрел": "Л̋͠е͠д̋я̋н͒о̋й͒͠ в͒͠ы̋͠с͒т͒р̋͠е͠л̋͠",
    "Огненный заряд": "О̋г͒͠н͒е͠н͒н͒ы̋͠й͒͠ з̋̋а͠р̋͠я̋д̋"
}

fake = Faker("ru_RU")

def load_skills():
    with open(SKILLS_FILE, 'r', encoding='utf8') as file:
        return [skill.strip() for skill in file.readlines()]

def create_files(num_files, skills):
    os.makedirs("result", exist_ok=True)

    for _ in range(num_files):
        selected_skills = random.sample(skills, 3)
        runic_skills = [LETTERS_MAPPING.get(skill, skill) for skill in selected_skills]
        
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

        while True:
            output_file_path = f"{base_name}{counter}.svg"
            if not os.path.exists(output_file_path):
                break
            counter += 1

        file_operations.render_template("src/template.svg", output_file_path, context)
        print(f"Файл создан: {output_file_path}")

def main():
    skills = load_skills()  

    while True:
        try:
            user_input = input("Сколько файлов вы хотите создать? ")
            num_files = int(user_input)
            if num_files <= 0:
                print("Пожалуйста, введите положительное число.")
                continue
            create_files(num_files, skills) 
            break
        except ValueError:
            print("Неверные данные. Пожалуйста, введите целое положительное число.")

if __name__ == "__main__":
    main()