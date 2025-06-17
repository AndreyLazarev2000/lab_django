from django import forms

class UserForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()

class SampleForm(forms.Form):
    # 1. BooleanField
    buy = forms.BooleanField(
        label="Положить товар в корзину?",
        required=False
    )

    # 2. NullBooleanField
    go = forms.NullBooleanField(
        label="Вы поедете в Сочи?",
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