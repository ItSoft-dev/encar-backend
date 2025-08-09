import requests

from django.db.models.signals import post_save
from django.dispatch import receiver

from config.env import env
from core.apps.cars.models import Car


@receiver(post_save, sender=Car)
def send_car_to_channel(sender, instance, created, **kwargs):
    # if not created:
    #     return

    caption = (
        f"🚗 Новое объявление:\n\n" 

        f"{instance.name}\n"

        f"Цена в рублях: {instance.price}\n"
        f"Год выпуска: {instance.year}\n" 
        f"Пробег: {instance.miliage}\n"
        f"Объем двигателя: {instance.engine_capacity}\n"
        f"Трансмиссия: {instance.transmission.name}\n" 
        f"Цвет: {instance.color.name}\n"
        f"Топливо: {instance.fuel_type.name}\n"
        f"Тип кузова: {instance.body_type.name}\n"
        f"Страны: {instance.region.name}\n"
        f"Полная информация об автомобиле на сайте "
        f"<a href='https://gm-car.vercel.app/cars/{instance.id}'>сайте</a>\n\n"
        f"🌐 На сайте <a href='https://gm-car.vercel.app/search-auto?brand={instance.brand.id}'>сайте</a> "
        f"вы можете создать подписку и получать через бота или на почту только те авто, "
        f"которые соответствуют выбранным критериям.\n\n"
        f"❓ Запросить дополнительную информацию по автомобилю можно у нашего менеджера "
        f"<a href='https://t.me/user_py'>менеджера</a>"
    )

    if instance.car_medias.exists():
        image_url = instance.car_medias.first().media.url
        full_image_url = f"{env.str("DOMAIN")}{image_url}"
        telegram_url = f"https://api.telegram.org/bot{env.str('BOT_TOKEN')}/sendPhoto"
        data = {
            "chat_id": env.str('CHANNEL_USERNAME'),
            "photo": full_image_url,
            "caption": caption,
            "parse_mode": "HTML"
        }
    else:
        telegram_url = f"https://api.telegram.org/bot{env.str('BOT_TOKEN')}/sendMessage"
        data = {
            "chat_id": env.str('CHANNEL_USERNAME'),
            "text": caption,
            "parse_mode": "HTML"
        }

    try:
        res = requests.post(telegram_url, data=data, timeout=5)
    except requests.exceptions.RequestException as e:
        print(f"Telegramga yuborishda xatolik: {e}")
    print(f'{res.json()}-----------------------------------------')