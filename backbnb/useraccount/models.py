import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models


class CustomizeUserManager(UserManager):
    """
    Gestionnaire personnalisé pour le modèle User.
    
    Cette classe permet de définir des méthodes spécifiques pour 
    créer des utilisateurs et des super-utilisateurs.
    """

    def _create_user(self, name, email, password, **extra_fields):
        """
        Crée un utilisateur avec un email et un mot de passe.

        :param name: Nom de l'utilisateur (optionnel)
        :param email: Adresse email de l'utilisateur (obligatoire)
        :param password: Mot de passe de l'utilisateur
        :param extra_fields: Champs supplémentaires pour l'utilisateur
        :return: Objet User créé
        """
        if not email:
            raise ValueError("Vous devez spécifier une adresse email valide.")

        email = self.normalize_email(email)  # Normalisation de l'email
        user = self.model(name=name, email=email, **extra_fields)  # Création de l'utilisateur
        user.set_password(password)  # Hachage du mot de passe
        user.save(using=self.db)  # Sauvegarde de l'utilisateur en base de données
        return user

    def create_user(self, name=None, email=None, password=None, **extra_fields):
        """
        Crée un utilisateur normal (non administrateur).

        :param name: Nom de l'utilisateur (optionnel)
        :param email: Adresse email de l'utilisateur (obligatoire)
        :param password: Mot de passe de l'utilisateur
        :param extra_fields: Champs supplémentaires
        :return: Objet User créé
        """
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(name, email, password, **extra_fields)

    def create_superuser(self, name=None, email=None, password=None, **extra_fields):
        """
        Crée un super-utilisateur avec tous les droits d'administration.

        :param name: Nom du super-utilisateur (optionnel)
        :param email: Adresse email (obligatoire)
        :param password: Mot de passe
        :param extra_fields: Champs supplémentaires
        :return: Objet User créé
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(name, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Modèle personnalisé pour les utilisateurs.

    Ce modèle remplace le modèle User par défaut de Django et utilise
    l'email comme identifiant principal au lieu du nom d'utilisateur.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    """Identifiant unique de l'utilisateur basé sur UUID."""

    email = models.EmailField(
        unique=True
    )
    """Adresse email unique utilisée comme identifiant."""

    name = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    """Nom de l'utilisateur (optionnel)."""

    avatar = models.ImageField(
        upload_to="uploads/avatars",
        blank=True,
        null=True
    )
    """Image de profil de l'utilisateur, stockée dans uploads/avatars/."""

    is_active = models.BooleanField(default=True)
    """Indique si l'utilisateur est actif (peut se connecter)."""

    is_superuser = models.BooleanField(default=False)
    """Indique si l'utilisateur est un super-utilisateur (admin)."""

    is_staff = models.BooleanField(default=False)
    """Indique si l'utilisateur peut accéder à l'interface d'administration."""

    objects = CustomizeUserManager()
    """Définit le gestionnaire personnalisé pour ce modèle."""

    USERNAME_FIELD = 'email'
    """Définit l'email comme champ utilisé pour l'authentification."""

    EMAIL_FIELD = 'email'
    """Champ principal pour l'email."""

    REQUIRED_FIELDS = []
    """Champs requis lors de la création d'un super-utilisateur (hormis USERNAME_FIELD)."""

    def __str__(self):
        """
        Retourne une représentation lisible de l'utilisateur.

        :return: Nom de l'utilisateur ou email si le nom n'est pas défini.
        """
        return self.name if self.name else self.email
