from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLES = [
        ('Etudiant', 'Étudiant'),
        ('Enseignant', 'Enseignant'),
    ]
    EXPERIENCES = [
        ('Débutant', 'Débutant'),
        ('Intermédiaire', 'Intermédiaire'),
        ('Avancé', 'Avancé'),
    ]
    SPECIALITES = [
        ('Développement Web', 'Développement Web'),
        ('Développement Mobile', 'Développement Mobile'),
        ('Développement Logiciel', 'Développement Logiciel'),
        ('Développement Jeux Vidéo', 'Développement Jeux Vidéo'),
        ('Développement Réseau', 'Développement Réseau'),
        ('Développement Système', 'Développement Système'),
        ('Développement Embarqué', 'Développement Embarqué'),
        ('Développement IA', 'Développement IA'),
        ('Développement IoT', 'Développement IoT'),
        ('Développement Cloud', 'Développement Cloud'),
        ('Développement Big Data', 'Développement Big Data'),
        ('Développement Blockchain', 'Développement Blockchain'),
        ('Développement Sécurité', 'Développement Sécurité'),
        ('Développement DevOps', 'Développement DevOps'),
        ('Développement Autre', 'Développement Autre'),
    ]

    # Ajoutez les champs supplémentaires ici
    role = models.CharField(max_length=50, choices=ROLES, default='Etudiant')
    experience = models.CharField(max_length=50, choices=EXPERIENCES, default='Débutant')
    diplomes = models.CharField(max_length=255, blank=True, null=True)
    specialite = models.CharField(max_length=100, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return self.username
