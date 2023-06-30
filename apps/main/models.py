# Django
from django.contrib.auth.models import User
from django.db import models


class Artist(models.Model):
    """
    Artist model.
    """
    GENDER_OTHER = 0
    GENDER_FEMALE = 1
    GENDER_MALE = 2
    GENDERS = (
        (GENDER_OTHER, 'Остальное'),
        (GENDER_FEMALE, 'Женщина'),
        (GENDER_MALE, 'Мужчина')
    )
    user = models.OneToOneField(
        to=User,
        on_delete=models.PROTECT,
        verbose_name='исполнитель',
        null=True,
        blank=True
    )
    nickname = models.CharField(
        verbose_name='псевдоним',
        default='',
        max_length=50
    )
    gender = models.PositiveSmallIntegerField(
        choices=GENDERS,
        verbose_name='гендер',
        default=GENDER_OTHER
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'музыкант'
        verbose_name_plural = 'музыканты'

    def __str__(self) -> str:
        if not self.nickname:
            return 'Noname'

        return f'Artist: {self.nickname}'


class City:
    '''
    Cities
    '''

    name = models.CharField(
        verbose_name='название',
        default='',
        max_length=50
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'город'
        verbose_name_plural = 'города'

    def __str__(self) -> str:
        return f'Band: {self.name}'



class Country:
    '''
    Countries
    '''

    name = models.CharField(
        verbose_name='название',
        default='',
        max_length=50
    )

    cities = models.ManyToManyField(
        verbose_name='город',
        to=City,
        related_name='cities'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'страна'
        verbose_name_plural = 'страны'

    def __str__(self) -> str:
        return f'Band: {self.name}'




class Band(models.Model):
    """
    Band model.
    """

    COUNTRIES = (
        (0, 'Kazakhstan'),
        (1, 'German')
    )

    artist = models.ForeignKey(
        to=Artist,
        on_delete=models.PROTECT,
        verbose_name='создатель'
    )

    title = models.CharField(
        verbose_name='название',
        default='',
        max_length=50,
        null=True
    )

    datetime_created = models.DateTimeField(
        verbose_name= ("дата создания"), 
        auto_now_add=True
    )

    datetime_updated = models.DateTimeField(
        verbose_name= ("дата обновления"), 
        auto_now_add=True
    )

    datetime_deleted = models.DateTimeField(
        verbose_name= ("дата удаления"), 
        auto_now_add=True
    )

    folowers = models.IntegerField(
        verbose_name='подпищики'
    )

    country = models.ManyToManyField(
        verbose_name='страна',
        to=Country
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'группа'
        verbose_name_plural = 'группы'

    def __str__(self) -> str:
        if not self.nickname:
            return 'Noname'

        return f'Band: {self.title}'

    # 1 Band 1 Artist
    # 1 Band много Artist
    # title (nullable)
    # datetime_created
    # datetime_updated
    # datetime_deleted
    # followers
    # country