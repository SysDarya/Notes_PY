import json
import datetime

notes = []

def save_notes():
    with open('notes.json','w') as file:
        json.dump(notes, file)

def add_note():
    title = input("Введите заголовок заметки: ")
    text = input("Введите текст заметки: ")
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {'id': len(notes)+1, 'title': title, 'text': text, 'date': date}
    notes.append(note)
    save_notes()
    print("Заметка успешно добавлена.")

def load_notes():
    global notes
    try:
        with open('notes.json', 'r') as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []

def edit_note():
    id = int(input("Введите ID заметки для редактирования: "))
    for note in notes:
        if note['id'] == id:
            note['title'] = input("Введите новый заголовок заметки: ")
            note['text'] = input("Введите новый текст заметки: ")
            note['date'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes()
            print("Заметка успешно отредактирована.")
            return     
    print("Ошибка: Заметка с таким ID не найдена, попробуйте снова.")

def delete_note():
    id = int(input("Введите ID заметки для удаления: "))
    for note in notes:
        if note['id'] == id:
            notes.remove(note)
            save_notes()
            print("Заметка успешно удалена.")
            return
    print("Ошибка: Заметка с таким ID не найдена, попробуйте снова.")

def list_notes():
    filter_date = input("Введите дату для фильтрации в формате - гггг-мм-дд: ")
    for note in notes:
        if filter_date in note['date']:
            print(f"ID: {note['id']}, Заголовок: {note['title']}, Текст: {note['text']}, Дата: {note['date']}")
    print("Ошибка: Заметок с такой датой не найдено.")

def prog():
    load_notes

while True:
    print("1. Добавить заметку")
    print("2. Редактировать заметку")
    print("3. Удалить заметку")
    print("4. Список заметок")
    print("5. Выход")
        
    choice = input("Выберите действие: ")
    if choice == '1':
        add_note()
    elif choice == '2':
        edit_note()
    elif choice == '3':
        delete_note()
    elif choice == '4':
        list_notes()
    elif choice == '5':
        break
    else:
        print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__prog__":
    prog()