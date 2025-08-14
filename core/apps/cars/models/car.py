from django.db import models

from core.apps.shared.models import BaseModel
from core.apps.cars.models.feture import (
    Brand, Model, Generation, FuelType, BodyType, Transmission, Color
)

class Region(BaseModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'страна'
        verbose_name_plural = 'страны'


class Car(BaseModel):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='cars')
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='cars')
    generation = models.ForeignKey(Generation, on_delete=models.CASCADE, related_name='cars')
    fuel_type = models.ForeignKey(FuelType, on_delete=models.CASCADE, related_name='cars')
    body_type = models.ForeignKey(BodyType, on_delete=models.CASCADE, related_name='cars')
    transmission = models.ForeignKey(Transmission, on_delete=models.CASCADE, related_name='cars')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='cars')
    price = models.PositiveBigIntegerField()
    year = models.CharField(max_length=4, null=True)
    month = models.CharField(max_length=2, null=True)
    engine_capacity = models.PositiveIntegerField()
    miliage = models.PositiveBigIntegerField()
    name = models.CharField(max_length=200)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, related_name='cars', null=True)
    is_sold = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'автомобил'
        verbose_name_plural = 'автомобили'
        

class CarMedia(BaseModel):
    media = models.ImageField(upload_to='car/media/')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car_medias')

    def __str__(self):
        return f'{self.car} media {self.media.name}'
    
    class Meta:
        verbose_name = 'изображение автомобиля'
        verbose_name_plural = 'изображения автомобилей'


class CarInteryer(BaseModel):
    side_airbag = models.BooleanField(default=False, verbose_name="Боковая подушка безопасности")
    curtain_airbag = models.BooleanField(default=False, verbose_name="Шторка безопасности")
    abs = models.BooleanField(default=False, verbose_name="Система антиблокировки тормозов (ABS)")
    traction_control = models.BooleanField(default=False, verbose_name="Система контроля тяги (TCS)")
    esc = models.BooleanField(default=False, verbose_name="Система электронной стабилизации (ESC)")
    tpms = models.BooleanField(default=False, verbose_name="Система контроля давления в шинах (TPMS)")
    ldws = models.BooleanField(default=False, verbose_name="Система предупреждения о выходе из полосы (LDWS)")
    rear_view_camera = models.BooleanField(default=False, verbose_name="Камера заднего вида")
    car = models.OneToOneField(Car, on_delete=models.CASCADE, related_name='car_interyer')

    def __str__(self):
        return f'{self.car} interyer'
    
    class Meta:
        verbose_name = 'Экстерьер/Интерьер'
        verbose_name_plural = 'Экстерьер/Интерьер'


class CarSafety(BaseModel):
    epb = models.BooleanField(default=False, verbose_name="Электронный стояночный тормоз (EPB)")
    automatic_ac = models.BooleanField(default=False, verbose_name="Автоматический кондиционер")
    smart_key = models.BooleanField(default=False, verbose_name="Умный ключ")
    wireless_door_lock = models.BooleanField(default=False, verbose_name="Беспроводной замок двери")
    rain_sensor = models.BooleanField(default=False, verbose_name="Датчик дождя")
    auto_light = models.BooleanField(default=False, verbose_name="Автоматический свет")
    navigation = models.BooleanField(default=False, verbose_name="Навигация")
    bluetooth = models.BooleanField(default=False, verbose_name="Bluetooth")
    usb_port = models.BooleanField(default=False, verbose_name="USB-порт")
    car = models.OneToOneField(Car, on_delete=models.CASCADE, related_name='car_safety')

    def __str__(self):
        return f'{self.car} safety'
    
    class Meta:
        verbose_name = 'Безопасность'
        verbose_name_plural = 'Безопасность'


class CarMultimedia(BaseModel):
    cruise_control = models.BooleanField(
        default=False, verbose_name='Круиз-контроль (обычный/адаптивный)'
    ) 
    leather_seats = models.BooleanField(default=False, verbose_name='Кожаные сиденья')
    seat_electric_adjustment_front = models.BooleanField(
        default=False, verbose_name='Электрорегулировка сидений (водитель/пассажир)'
    )
    seat_electric_adjustment_rear = models.BooleanField(
        default=False, verbose_name='Электрорегулировка сидений (задний ряд)'
    )
    seat_heating_front_rear = models.BooleanField(
        default=False, verbose_name='Подогрев сидений (передних/задних)'
    )
    seat_memory_front = models.BooleanField(
        default=False, verbose_name='Память сидений (водитель/пассажир)'
    )
    seat_ventilation_front = models.BooleanField(
        default=False, verbose_name='Вентилируемые сиденья (водитель/пассажир)'
    )
    seat_ventilation_rear = models.BooleanField(
        default=False, verbose_name='Вентилируемые сиденья (задний ряд)'
    )
    massage_seats = models.BooleanField(default=False, verbose_name='Массажные сиденья')
    abs_system = models.BooleanField(
        default=False, verbose_name='Система антиблокировки тормозов (ABS)'
    )
    rear_av_monitor = models.BooleanField(
        default=False, verbose_name='AV-монитор задних сидений'
    )
    cd_player = models.BooleanField(default=False, verbose_name='CD-плеер')
    usb_port = models.BooleanField(default=False, verbose_name='USB-порт')
    aux_port = models.BooleanField(default=False, verbose_name='AUX-порт')
    car = models.OneToOneField(Car, on_delete=models.CASCADE, related_name='car_multimedia')

    def __str__(self):
        return f'{self.car} multimedia' 
    
    class Meta:
        verbose_name = 'Удобство / Мультимедиа'
        verbose_name_plural = 'Удобство / Мультимедиа'


class CarSeats(BaseModel):
    seat_leather = models.BooleanField(default=False, verbose_name='Кожаные сиденья')
    seat_electric_adjustment_driver_passenger = models.BooleanField(
        default=False, verbose_name='Электрорегулировка сидений (водитель/пассажир)'
    )
    seat_electric_adjustment_rear_seats = models.BooleanField(
        default=False, verbose_name='Электрорегулировка сидений (задний ряд)'
    )
    seat_heating_all = models.BooleanField(
        default=False, verbose_name='Подогрев сидений (передних/задних)'
    )
    seat_memory_all = models.BooleanField(
        default=False, verbose_name='Память сидений (водитель/пассажир)'
    ) 
    seat_ventilation_driver_passenger = models.BooleanField(
        default=False, verbose_name='Вентилируемые сиденья (водитель/пассажир)'
    )
    seat_ventilation_back = models.BooleanField(
        default=False, verbose_name='Вентилируемые сиденья (задний ряд)'
    )
    seat_massage = models.BooleanField(
        default=False, verbose_name='Массажные сиденья'
    )
    car = models.OneToOneField(Car, on_delete=models.CASCADE, related_name='car_seats')

    def __str__(self):
        return f'{self.car} seats'
    
    class Meta:
        verbose_name = 'Сиденья'
        verbose_name_plural = 'Сиденья'


class CarPricing(BaseModel):
    agent_service = models.PositiveBigIntegerField(verbose_name='Услуги агента')
    car_cost = models.PositiveBigIntegerField(verbose_name='Стоимость авто')
    expences_in_korea = models.PositiveBigIntegerField(verbose_name='расходы в Корее')
    custom_dutie = models.PositiveBigIntegerField(verbose_name='Таможенные платежи')
    utilsbor = models.PositiveBigIntegerField(verbose_name='Утильсбор')
    custom_broker = models.PositiveBigIntegerField(verbose_name='Таможенный брокер')
    car_transporter = models.PositiveBigIntegerField(verbose_name='Автовоз')
    car = models.OneToOneField(Car, on_delete=models.CASCADE, related_name='car_pricing')

    def __str__(self):
        return f"{self.car} pricing"

    class Meta:
        verbose_name = 'расчет цены'
        verbose_name_plural = 'расчет цены'


class CarInspection(BaseModel):
    car = models.OneToOneField(Car, on_delete=models.CASCADE, related_name="car_inspections")
    inspection_date = models.DateTimeField(null=True, blank=True, verbose_name='Дата инспекции')
    diagnosis_date = models.DateTimeField(null=True, blank=True, verbose_name='Дата диагностики')
    vin = models.CharField(max_length=100, null=True, blank=True, verbose_name='VIN')
    engine_type = models.CharField(max_length=100, null=True, blank=True, verbose_name='Тип мотора')
    incidents = models.CharField(max_length=255, null=True, blank=True, verbose_name='Инциденты')
    year = models.CharField(max_length=10, null=True, blank=True, verbose_name='Год модели')
    usage_type = models.CharField(max_length=255, null=True, blank=True, verbose_name='Тип использования')
    front_left_door = models.CharField(max_length=50, null=True, blank=True, verbose_name='Передняя левая дверь')
    front_right_door = models.CharField(max_length=50, null=True, blank=True, verbose_name='Передняя правая дверь')
    rear_left_door = models.CharField(max_length=50, null=True, blank=True, verbose_name='Задняя левая дверь')
    rear_right_door = models.CharField(max_length=50, null=True, blank=True, verbose_name='Задняя правая дверь')
    hood = models.CharField(max_length=50, null=True, blank=True, verbose_name='Капот')
    trunk = models.CharField(max_length=50, null=True, blank=True, verbose_name='Крышка багажника')

    def __str__(self):
        return f"{self.car} inspection"
    
    class Meta:
        verbose_name = 'Проверка авто'
        verbose_name_plural = 'Проверка авто'


class CarInspectionIncident(BaseModel):
    inspection = models.ForeignKey(CarInspection, on_delete=models.CASCADE, related_name="car_incidents")
    name = models.CharField(max_length=255)  
    value = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Страховые случаи"
        verbose_name_plural = "Страховые случаи"


class InspectionSection(BaseModel):
    inspection = models.ForeignKey(CarInspection, on_delete=models.CASCADE, related_name="sections")
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Внутренняя инспекция'
        verbose_name_plural = 'Внутренняя инспекция'


class InspectionField(BaseModel):
    section = models.ForeignKey(InspectionSection, on_delete=models.CASCADE, related_name="fields")
    name = models.CharField(max_length=255)  
    status = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Внутренняя инспекция"
        verbose_name_plural = "Внутренняя инспекция"