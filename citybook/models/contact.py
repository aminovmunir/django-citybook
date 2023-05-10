from django.db import models


class Contact(models.Model):

    phone = models.CharField("Номер телефона", max_length=12)
    email = models.EmailField("Почта", max_length=50, null=True, blank=True)
    additional_phone=models.CharField("Доп.номер телефона", max_length=12, null=True, blank=True)
    work_schedule=models.CharField("Режим работы", max_length=100, null=True, blank=True)
    img=models.CharField("Фотография", max_length=100, null=True, blank=True)
    place = models.OneToOneField("citybook.place", related_name="contacts", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self) -> str:
        return self.phone
