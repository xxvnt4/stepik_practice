from django.contrib import admin, messages
from .models import Movie, Director, Actor
from django.db.models import QuerySet


class RatingFilter(admin.SimpleListFilter):
    title = 'Фильтр по рейтингу'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('<40', 'Низкий'),
            ('от 40 до 59', 'Средний'),
            ('от 60 до 79', 'Высокий'),
            ('>=80', 'Высочайший')
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<40':
            return queryset.filter(rating__lt=40)
        if self.value() == 'от 40 до 59':
            return queryset.filter(rating__gte=40).filter(rating__lt=60)
        if self.value() == 'от 60 до 79':
            return queryset.filter(rating__gte=60).filter(rating__lt=80)
        if self.value() == '>=80':
            return queryset.filter(rating__gte=80)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # fields = ['name', 'rating']
    exclude = ['budget']
    readonly_fields = ['year']
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'rating', 'director', 'budget', 'rating_status']
    # Поле actors нельзя добавлять в эту переменную - выскочит ошибка. Это поле является ManyToMany.
    list_editable = ['rating', 'director', 'budget']
    filter_horizontal = ['actors']
    # Данная переменная позволяет добавлять актеров в фильмы более удобным способом. Есть горизонтальный и вертикальный
    # варианты.
    list_per_page = 10
    actions = ['set_dollars', 'set_euro']
    search_fields = ['name__startswith', 'rating']
    list_filter = ['name', 'currency', RatingFilter]

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
admin.site.register(Director)
admin.site.register(Actor)
# Не забыть зарегистрировать модель!