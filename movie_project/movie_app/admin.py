from django.contrib import admin, messages
from .models import Movie
from django.db.models import QuerySet

class RatingFilter(admin.SimpleListFilter):
    # Класс для собственных фильтров.
    title = 'Фильтр по рейтингу'
    # Название фильтра в панели.
    parameter_name = 'rating'
    # Название параметра в адресной строке.

    def lookups(self, request, model_admin):
        # Переопределим этот метод, где вернем нужные нам пункты в виде списка кортежей, где первый элемент
        # пойдет в адресную строку, а второй - в панель фильтрации.
        return [
            ('<40', 'Низкий'),
            ('от 40 до 59', 'Средний'),
            ('от 60 до 79', 'Высокий'),
            ('>=80', 'Высочайший')
        ]

    def queryset(self, request, queryset: QuerySet):
        # Переопределим и этот метод, где опишем всю логику фильтрации.
        if self.value() == '<40':
            return queryset.filter(rating__lt=40)
        if self.value() == 'от 40 до 59':
            return queryset.filter(rating__gte=40).filter(rating__lt=60)
        if self.value() == 'от 60 до 79':
            return queryset.filter(rating__gte=60).filter(rating__lt=80)
        if self.value() == '>=80':
            return queryset.filter(rating__gte=80)

@admin.register(Movie)
# Можем навесить этот декоратор на наш класс - в этом случае, нам не придется в дальнейшем регистрировать наши классы
# отдельно в этом модуле.
class MovieAdmin(admin.ModelAdmin):
    # Для организации и удобного управления базой данных в административной панели, создаем новый класс MovieAdmin,
    # наследуемый от admin.ModelAdmin. Здесь можно выставлять необходимые нам параметры вывода базы данных.
    list_display = ['name', 'rating', 'currency', 'budget', 'rating_status']
    # В этой переменной прописываются названия колонок, которые мы хотим видеть в нашей таблице. Они будут в том же
    # порядке. После заполнения этой переменной, элементы базы данных перестают быть вида, объявленного в магическом
    # методе __str__ класса нашей модели.
    list_editable = ['rating', 'currency', 'budget']
    # Те колонки, которые мы можем редактировать. Стоит учесть, что здесь не может быть первого элемента списка предыдущей
    # переменной, так как первая колонка является ссылкой на страницу редактирования элемента базы данных.
    # Если хотим исправить ошибку с тем, что нельзя сохранять пустые значения в некоторых колонках, то нам нужно перейти
    # в models.py и дополнительным аргументом к нужной колонке добавить blank=True (см. models.py).
    # ordering = ['-rating', 'name']
    # С помощью этой переменной мы можем сортировать нашу базу данных.
    list_per_page = 10
    # Пагинация - то количество элементов, которые мы хотим видеть на одной странице.
    actions = ['set_dollars', 'set_euro']
    search_fields = ['name__startswith', 'rating']
    list_filter = ['name', 'currency', RatingFilter]
    # Для того, чтобы создать фильтр по уже существующим колонкам, нужно просто добавить переменную list_filter
    # с названиями в виде списка. Но если мы хотим создать собственный фильтр, нужно создать класс (см. выше по коду).

    @admin.display(ordering='rating', description='Status')
    def rating_status(self, mov: Movie):
        if mov.rating < 50:
            return 'Зачем это смотреть?'
        if mov.rating < 70:
            return 'Разок можно глянуть'
        if mov.rating <= 85:
            return 'Зачет!'
        return 'Топчик!'

    @admin.action(description='Установить валюту в доллар')
    def set_dollars(self, request, qs: QuerySet):
        qs.update(currency=Movie.USD)

    @admin.action(description='Установить валюту в евро')
    def set_euro(self, request, qs: QuerySet):
        count_updated = qs.update(currency=Movie.EURO)
        self.message_user(
            request,
            f'Было обновлено {count_updated} записей',
            messages.ERROR
        )



# admin.site.register(Movie)
# admin.site.register(MovieAdmin)
# Та самая регистрация моделей, вместо которой мы просто навешиваем декоратор на класс.

