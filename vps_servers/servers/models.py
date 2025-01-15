from django.db import models


class VPS(models.Model):
    """Модель виртуальных серверов."""
    STARTED = "Started"
    BLOCKED = "Blocked"
    STOPPED = "Stopped"

    STATUS_CHOICES = (
        (STARTED, "Started"),
        (BLOCKED, "Blocked"),
        (STOPPED, "Stopped"),
    )

    uid = models.CharField(unique=True, max_length=32)
    cpu = models.IntegerField()
    ram = models.IntegerField()
    hdd = models.IntegerField()
    status = models.CharField(
        max_length=7,
        choices=STATUS_CHOICES
        )

    def __str__(self):
        return self.uid
