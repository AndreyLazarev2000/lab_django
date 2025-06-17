from django import forms
import os
from django.conf import settings
from datetime import date

class UserForm(forms.Form):
    name = forms.CharField(label="Имя клиента")
    age = forms.IntegerField(label="Возраст клиента")


class SampleForm(forms.Form):
    # 1. BooleanField
    buy = forms.BooleanField(
        label="Положить товар в корзину?",
        required=False
    )

    # 2. NullBooleanField
    go = forms.NullBooleanField(
        label="Вы поедете в Сочи на новогодние праздники?",
        required=False
    )

    # 3. CharField
    name = forms.CharField(
        label="Имя клиента",
        max_length=15,
        help_text="ФИО не более 15 символов"
    )

    # 4. EmailField
    email = forms.EmailField(
        label="Электронный адрес"
    )

    # 5. RegexField
    code = forms.RegexField(
        label="Введите код",
        regex=r'^[A-Z]{3}\d{3}$',
        help_text="Пример: ABC123"
    )

    # 6. URLField
    url_text = forms.URLField(
        label="Введите URL"
    )

    # 7. FilePathField
    file_path = forms.FilePathField(
        label="Выберите файл из папки",
        path=r"C:\Users\Predator\Desktop\lab_django\files"
    )

    # 8. FileField
    file = forms.FileField(
        label="Файл"
    )

    # 9. ImageField для загрузки изображений
    avatar = forms.ImageField(
        label="Ваше фото",
        help_text="Загрузите ваш аватар (JPG/PNG)",
        required=False
    )

    # 10. DateField для ввода даты (с виджетом календаря)
    birth_date = forms.DateField(
        label="Дата рождения",
        widget=forms.DateInput(attrs={'type': 'date'}),
        initial=date.today,
        help_text="Выберите дату"
    )

    # 11. DateTimeField для ввода даты и времени
    meeting_datetime = forms.DateTimeField(
        label="Дата и время встречи",
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        help_text="Выберите дату и время"
    )

    # 12. IntegerField с ограничениями
    age = forms.IntegerField(
        label="Ваш возраст",
        min_value=18,
        max_value=100,
        help_text="Введите число от 18 до 100",
        error_messages={
            'min_value': "Возраст должен быть не менее 18 лет",
            'max_value': "Возраст должен быть не более 100 лет"
        }
    )

    # 13. ChoiceField с выпадающим списком
    EDUCATION_CHOICES = [
        ('HS', 'Среднее образование'),
        ('COL', 'Среднее специальное'),
        ('UNI', 'Высшее образование'),
        ('PHD', 'Ученая степень'),
    ]
    education = forms.ChoiceField(
        label="Образование",
        choices=EDUCATION_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        initial='UNI'
    )

    # Дополнительные улучшения:

    # Множественный выбор с CheckboxSelectMultiple
    LANGUAGES = [
        ('RU', 'Русский'),
        ('EN', 'Английский'),
        ('DE', 'Немецкий'),
        ('FR', 'Французский'),
    ]
    languages = forms.MultipleChoiceField(
        label="Какими языками владеете?",
        choices=LANGUAGES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    # DecimalField для дробных чисел
    salary_expectation = forms.DecimalField(
        label="Ожидаемая зарплата",
        max_digits=8,
        decimal_places=2,
        help_text="Укажите сумму в рублях"
    )