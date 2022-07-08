from django.db import models


class Declaration(models.Model):
  _choices = (
    ("A", "Ativo"),
    ("B", "Banido"),
    ("E", "Em espera")
  )
  title = models.CharField(max_length=100, blank=False, null=False, help_text="Título bonitão", verbose_name="Título")
  url_slug = models.SlugField(max_length=100, unique=True)
  declaration = models.CharField(max_length=250, blank=False, null=False, help_text="Declaração bonitona para o seu s2", verbose_name="Declaração")
  status = models.CharField(max_length=10, choices=_choices, default="E")

  def __str__(self):
      return self.title
    
  class Meta:
    verbose_name = "Declaração"
    verbose_name_plural = "Declarações"
    