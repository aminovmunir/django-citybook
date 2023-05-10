from django.db import models


class Place(models.Model):

    name=models.CharField('Название', max_length=50)
    description=models.CharField('Описание', null=True, max_length=500)
    category=models.ForeignKey('citybook.category', on_delete=models.CASCADE,
                               related_name="places",
                               verbose_name="Категория")
    address=models.CharField("Адрес", max_length=50,)
    city=models.ForeignKey('citybook.city', on_delete=models.CASCADE,
                            related_name="places",
                            verbose_name="Город")

    class Meta:
        verbose_name = "Заведение"
        verbose_name_plural = "Заведении"

    def __str__(self) -> str:
        return self.name
