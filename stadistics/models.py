from django.db import models
#ForeignKey ?
from Users.models import users

# Create your models here.
class Watersample(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField()
    ph = models.FloatField()
    termo = models.FloatField()
    condu = models.FloatField()
    otroSensor = models.FloatField()
    #Relacion uno
    user = models.ForeignKey(users, on_delete=models.CASCADE, related_name='watersamples')


    def __str__(self):
        return str(self.user) + " - Watersample"
    
    def save(self, *args, **kwargs):
        attributes = ['ph', 'termo', 'condu', 'otroSensor']
        repeated_values = []
        for attribute in attributes:
            attribute_value = getattr(self, attribute)
            count = Watersample.objects.filter(**{attribute: attribute_value}).count()
            if count >= 4:
                repeated_values.append((attribute, attribute_value))

        if repeated_values:
            model_profile = Modelprofile.objects.first()
            for attribute, value in repeated_values:
                setattr(model_profile, attribute, value)
            model_profile.save()

        super().save(*args, **kwargs)

class Modelprofile(models.Model):
    ph = models.FloatField(default=0.0)
    termo = models.FloatField(default=0.0)
    condu = models.FloatField(default=0.0)
    otroSensor = models.FloatField(default=0.0)

    def __str__(self):
        return self.name