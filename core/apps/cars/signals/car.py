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
        f"🚗 Yangi mashina qo‘shildi:\n\n"
        f"🆔 ID: {instance.id}\n"
        f"📌 Nomi: {instance.name}\n"
        f"💰 Narxi: {instance.price if hasattr(instance, 'price') else 'Nomaʼlum'}"
    )

    if instance.image:
        image_url = instance.image.url
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