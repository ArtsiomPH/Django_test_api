from django.db import models


# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    birth_date = models.DateField()
    age = models.PositiveIntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(age__gte=0), name='age_gte_0'),
        ]
        db_table = 'Users'
