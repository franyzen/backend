from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    name = models.CharField(
        max_length=50,
        unique=True,
        help_text="Nombre único del rol"
    )
    description = models.TextField(
        blank=True,
        default='',
        help_text="Descripción opcional del rol"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    ROLE_CHOICES = [
       ('OWNER', 'Owner'),
       ('RECEPTIONIST', 'Receptionist'),
       ('VET', 'Vet'),
       ('TECH_VET', 'Tech Vet'),
       ('MANAGER', 'Manager'),
   ]
    role = models.CharField(
       max_length=20,
       choices=ROLE_CHOICES,
       blank=True,
       default='',
   )
    # Campos adicionales de ejemplo
    phone_number = models.CharField(
        max_length=15,
        blank=True,
        default='',
        help_text="Número de teléfono"
    )

    # Email único (el username sigue siendo el campo de login por defecto,
    # pero aseguramos unicidad del email)
    email = models.EmailField(
        unique=True,
        help_text="Correo electrónico único"
    )

    class Meta:
        db_table = 'users'  # podemos mantener el nombre clásico
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        # Índices adicionales
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['name']),
            models.Index(fields=['role']),
        ]
        # Restricción extra: username también único (ya lo hereda de AbstractUser,
        # pero podemos explicitarlo si queremos; no es necesario)

    def __str__(self):
        return self.user
