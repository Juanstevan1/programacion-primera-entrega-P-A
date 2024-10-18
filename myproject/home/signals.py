#from django.db.models.signals import post_save
#from django.dispatch import receiver
#from django.contrib.auth.models import User
#from .models import Profile

# Este decorador conecta la función create_profile con la señal post_save del modelo User
# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     # Si el usuario fue creado (no actualizado)
#     if created:
#         # Crea un perfil asociado al usuario
#         Profile.objects.create(user=instance)

# Este decorador conecta la función save_profile con la señal post_save del modelo User
# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     # Guarda el perfil asociado al usuario
#     instance.profile.save()
