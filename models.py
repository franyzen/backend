from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


class Role(models.Model):
    """
    Tabla de roles. Ej: 'admin', 'cliente', 'dueño'.
    """
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

    class Meta:
        db_table = 'role'
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
        # Índice por nombre (aparte del unique ya implícito)
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name


class User(AbstractUser):
    """
    Usuario personalizado. Relación FK a Role y OneToOne con Owner (éste desde la app owner).
    """
    # FK a Role (se permite null para usuarios sin rol definido)
    role = models.ForeignKey(
        Role,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='users',
        help_text="Rol asignado al usuario"
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
        db_table = 'auth_user'  # podemos mantener el nombre clásico
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        # Índices adicionales
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['role']),
        ]
        # Restricción extra: username también único (ya lo hereda de AbstractUser,
        # pero podemos explicitarlo si queremos; no es necesario)

    def __str__(self):
        return self.username