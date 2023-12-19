from django.db import models

# Create your models here.
class Slide(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название"

    )
    descriptions = models.CharField(
        max_length=255,
        verbose_name="Описание"
    )
    image = models.ImageField(
        upload_to="main_photo",
        verbose_name='Фото'
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Настройки'
        verbose_name_plural = "Настройка"
    
class Settings(models.Model):
    logo = models.ImageField(
        upload_to="Logo",
        verbose_name="Логотип"
    )
    one_page = models.ImageField(
        upload_to="photo",
        verbose_name='Логотип_2'
    )
    week = models.CharField(
        max_length = 255,
        verbose_name = "Дни когда ты в гиксе"
    )
    week_of = models.CharField(
        max_length = 255,
        verbose_name = "дни когда ты не в гиксе"
    )
    time = models.CharField(
        max_length = 255,
        verbose_name = "С сколько до скольки ты в гиксе"
    )
    number = models.CharField(
        max_length = 255,
        verbose_name = "Номер телефона",
        blank=True, null=True
    )
    email = models.CharField(
        max_length = 255,
        verbose_name = "Email адресс",
        blank=True, null=True
    )
    
    class Meta:
        verbose_name = 'Настройки ',
        verbose_name_plural = "Настройка лаготипа"

class About_me(models.Model):
    about_me = models.TextField(
        verbose_name='Обо мне'
    )
    my_goul = models.TextField(
        verbose_name ='Моя цель'
    )
    my_advantages = models.TextField(
        verbose_name ='Мои премущества'
    )
    
    my_guarantee =models.TextField(
        verbose_name ='Моя гарантия'
    )
    my_image = models.ImageField(
        upload_to="My image"
    )

    def __str__(self):
        return self.about_me
    
    class Meta:
        verbose_name = 'Инфорамация обо мне'
        verbose_name_plural = "Настройка информации"

class Mentor(models.Model):
    zvanie = models.CharField(
        max_length=255,
        verbose_name ='Звание'
    )
    mentor_name = models.CharField(
        max_length=255,
        verbose_name = 'Имя ментора'
    )
    about_mentor = models.TextField(
        verbose_name = 'Информация о менторе'
    )
    quote = models.TextField(
        verbose_name = 'Цитата ментора'
    )
    mentor_image = models.ImageField(
        upload_to="Mentor image"
    )
    insgram = models.URLField(
        max_length=255, 
        blank=True, null=True
    )
    fonbb = models.ImageField(
        upload_to="Mentor Фон"
    )

    def __str__(self):
        return self.mentor_name
    
    class Meta:
        verbose_name = 'Инфорамация о менторе'
        verbose_name_plural = "Настройка ментора"

class Card(models.Model):
    name_card = models.CharField(
         max_length=255,
         verbose_name = 'Название карточки'
    )
    dis_card = models.TextField(
        verbose_name = 'Описание карточки'
    )

    def __str__(self):
        return self.name_card
    
    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = "Настройка карты"


class Friend(models.Model):
    friend_name= models.CharField(
        max_length =255,
        verbose_name = "Имя"
    )
    friend_direction = models.CharField(
        max_length = 255,
        verbose_name = "Напровление"
    )
    friend_quote = models.TextField(
        verbose_name = "Цитата"
    )
    friend_image = models.ImageField(
        upload_to="Фото"
    )
    def __str__(self):
        return self.friend_name
    
    class Meta:
        verbose_name = 'Настройки раздела друзья'
        verbose_name_plural = "Настройка раздела друзья"

class Teacher(models.Model):
    teach_image = models.ImageField(
        upload_to="Teacher Foto",
        verbose_name = "Фото учителя"
    )
    teach_name = models.CharField(
        max_length =255,
        verbose_name = "Имя учителя"
    )
    teach_month = models.CharField(
        max_length = 255,
        verbose_name = "Месяц который он обучал"
    )
    insgram = models.URLField(
        max_length=255, 
        blank=True, 
        null=True
    )
    def __str__(self):
        return self.teach_name
    
    class Meta:
        verbose_name = 'Настройки раздела учетиля'
        verbose_name_plural = "Настройка учителей"


class Blogpost(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = "Название"
    )
    descriptions = models.TextField(
        verbose_name = "Описание"
    )
    image = models.ImageField(
        upload_to="Blog_image"
    )
    created = models.DateField(
        auto_now_add = True,
        blank = True,null = True
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Новость '
        verbose_name_plural = "Новости"

class Mypro(models.Model):
        projects = models.CharField(
            max_length = 255,
            verbose_name = "Число проектов"
        )
        hours_work = models.CharField(
            max_length = 255,
            verbose_name = "Число время работ"
        )
        ofiices = models.CharField(
            max_length = 255,
            verbose_name = "Число офицов"
        )
        clients= models.CharField(
            max_length = 255,
            verbose_name = "Число клиентов"
        )
        def __str__(self):
            return self.projects
    
        class Meta:
            verbose_name = 'Мои успехи'
            verbose_name_plural = "Мои успехи"


class Mytpoject(models.Model):
        image = models.ImageField(
            upload_to="Image My projects"
        )
        title = models.CharField(
            max_length = 255,
            verbose_name = "Навазние проекта"
        )
        descriptions = models.TextField(
            verbose_name = "Описание"
        )
        def __str__(self):
            return self.title
    
        class Meta:
            verbose_name = 'Мои проекты'
            verbose_name_plural = "Мои проекты"
