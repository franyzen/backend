from django.db import models

from django.conf import settings


class Owner(models.Model):
    """
    Perfil de dueño/propietario. Relación OneToOne con User y campos propios del negocio.
    """
    # OneToOne hacia el usuario (relación principal)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='owner_profile',
        help_text="Usuario asociado al perfil de dueño"
    )

    # Campos específicos del owner
    company_name = models.CharField(
        max_length=200,
        blank=True,
        default='',
        help_text="Nombre de la empresa o negocio"
    )
    business_address = models.TextField(
        blank=True,
        default='',
        help_text="Dirección del negocio"
    )
    tax_id = models.CharField(
        max_length=50,
        unique=True,        # Suponemos que el ID fiscal es único
        blank=True,
        null=True,          # Podría no estar disponible al crear
        help_text="Número de identificación fiscal"
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        default='',
        help_text="Teléfono de contacto del negocio"
    )
    is_verified = models.BooleanField(
        default=False,
        help_text="Indica si el dueño ha sido verificado"
    )

    # Marca de tiempo
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'owner'
        verbose_name = 'Dueño'
        verbose_name_plural = 'Dueños'
        # Índices
        indexes = [
            models.Index(fields=['user']),       # búsquedas por usuario
            models.Index(fields=['tax_id']),     # búsquedas por ID fiscal
            models.Index(fields=['company_name']),
        ]
        # Orden por defecto
        ordering = ['company_name']

    def __str__(self):
        return f"Owner: {self.company_name or self.user.username}"
