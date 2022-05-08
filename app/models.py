from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse


class Classes(models.Model):
    name = models.CharField(max_length=300, verbose_name="Անուն")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Դասարան'
        verbose_name_plural = 'Դասարաններ'

    def get_absolute_url(self):
        return reverse('class_details', kwargs={"id": self.pk})


class Lessons(models.Model):

    cls = models.ForeignKey('Classes', on_delete=models.CASCADE, verbose_name="Դասարանը")
    title = models.CharField(verbose_name="Դասավերնագիր", max_length=255)
    description = RichTextUploadingField(verbose_name="Ամբողջական տեքստ")

    class Meta:
        verbose_name = 'Դաս'
        verbose_name_plural = 'Դասեր'

    # def get_absolute_url(self):
    #     return reverse('lesson_details', kwargs={"id": self.id})

class ContactUs(models.Model):
    first_name = models.CharField(max_length=255, verbose_name="Անուն")
    phone = models.CharField(max_length=255, verbose_name="Հեռ.")
    email = models.CharField(verbose_name="Էլ. հասցե", max_length=255)
    message = models.TextField(verbose_name="Նամակ")

    class Meta:
        verbose_name = "Հետադարձ կապի պատվեր"
        verbose_name_plural = "Հետադարձ կապի պատվերներ"
#
#
# class Gallery(models.Model):
#     image = models.FileField(verbose_name="Նկար", validators=[FileExtensionValidator(
#         allowed_extensions=['svg', 'png', 'jpg', 'jpeg'])]
#                              )
#
#     class Meta:
#         verbose_name = 'Նկար'
#         verbose_name_plural = 'Նկարներ'


# class AboutUs(models.Model):
#     large_text = RichTextUploadingField(verbose_name="Տեքստ")
#     image = models.FileField(verbose_name='Նկար')
#
#     class Meta:
#         verbose_name = 'Մեր մասին'
#         verbose_name_plural = 'Մեր մասին'