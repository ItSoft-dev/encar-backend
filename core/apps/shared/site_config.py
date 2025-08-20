from core.apps.shared.models import SiteConfig


def get_email_config():
    config = SiteConfig.objects.first()
    if not config:
        return {}
    return {
        "EMAIL_HOST": config.email_host,
        "EMAIL_PASSWORD": config.email_host_password,
        "MANAGER": config.manager,
        "BOT_TOKEN": config.bot_token,
        "CHANNEL_USERNAME": config.channel_username,
    }