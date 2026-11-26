from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название книги: ')

    author = models.CharField(max_length=100, verbose_name='Автор книги')

    image_1 = models.ImageField(upload_to='books/list', verbose_name='Фото для библиотеки',
                                blank=True, null = True)
    image_2 = models.ImageField(upload_to='books/detail', verbose_name='Фото для страницы',
                                blank= True, null = True)
    description = models.TextField(verbose_name='Описание книги:', blank=True, null=True)

    GENRE = (
        ('Проза', 'Проза'),
        ('Фантастика', 'Фантастика'),
        ('Фэнтези', 'Фэнтези'),
        ('Детектив', 'Детектив'),
        ('Триллер', 'Триллер'),
        ('Ужасы', 'Ужасы'),
        ('Любовный роман', 'Любовный роман'),
        ('Приключения', 'Приключения'),
        ('Историческая литература', 'Историческая литература'),
        ('Биография мемуары', 'Биография мемуары'),
        ('Научпоп и справочники', 'Научпоп и справочники'),
        ('Поэзия и пьесы', 'Поэзия и пьесы'),
    )
    genre = models.CharField(max_length=100, choices=GENRE, default='Проза', verbose_name='Выберите жанр: ')

    audio_book = models.URLField(null=True, blank=True, verbose_name='Ссылка на аудио книгу: ')

    count_pages = models.PositiveIntegerField(verbose_name='Количество страниц: ', blank=True)

    created_data_book = models.IntegerField(verbose_name='Дата создания книги: ', blank=True,
                                            help_text='Если книга написана до нашей эры - напишите год со знаком минус')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} | {self.author}'

    class Meta:
        verbose_name = 'книгу'
        verbose_name_plural = 'книги'