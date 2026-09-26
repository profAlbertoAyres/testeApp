import os
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

from .models import FotoExercicio


@receiver(post_delete, sender=FotoExercicio)
def apagar_arquivo_ao_deletar(sender, instance, **kwargs):
    if instance.imagem and os.path.isfile(instance.imagem.path):
        instance.imagem.delete(save=False)


@receiver(pre_save, sender=FotoExercicio)
def apagar_arquivo_antigo_ao_trocar(sender, instance, **kwargs):
    if not instance.pk:
        return
    try:
        antiga = FotoExercicio.objects.get(pk=instance.pk).imagem
    except FotoExercicio.DoesNotExist:
        return
    nova = instance.imagem
    if antiga and antiga != nova and os.path.isfile(antiga.path):
        antiga.delete(save=False)