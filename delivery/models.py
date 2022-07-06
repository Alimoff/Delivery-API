from django.db import models
from django.forms import CheckboxInput
from django import forms

# Create your models here.

# Category Of Regions
class Region(models.Model):
    region_name = models.CharField("Choose Your Region:", max_length=200)

    def __str__(self):
        return self.region_name

    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regions"


# Category Of Meals
class Food(models.Model):
    type_of_meal = models.CharField("Choose Type Of Meal:", max_length=250)

    def __str__(self):
        return self.type_of_meal

    class Meta:
        verbose_name = "Food"


# Main Class
class Orders(models.Model):
    name = models.CharField("Enter Your name:", max_length=200)
    type_of_meal = models.ForeignKey(
        Food, on_delete=models.CASCADE, null=True, related_name="Food", default=True
    )
    order = models.CharField("Enter meal:", max_length=250)
    count_diners = models.IntegerField("Number of diners:")
    phone = models.IntegerField("Enter Phone Number: ")

    region_name = models.ForeignKey(
        Region, on_delete=models.CASCADE, null=True, related_name="Region", default=True
    )

    adress = models.CharField("Enter adress:", max_length=250)

    time = models.TimeField("Delivery Time:", auto_now=False)

    comment = models.TextField("Additional Information:", null=True, blank=True)

    # More Info

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            str(self.id)
            + ")   "
            + str(self.name)
            + "    |    "
            + str(self.order)
            + "    |   "
            + str(self.count_diners)
            + "    |   "
            + str(self.time)
        )

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class Cook(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name="Orders")

    checkbox = CheckboxInput(attrs={"class": "Order accepted by Cook"})

    def __str__(self):
        return str(self.order)

    class Meta:
        verbose_name = "Order to Cook"
        verbose_name_plural = "Orders to Cook"


class Taxis(models.Model):
    order = models.ForeignKey(Cook, on_delete=models.CASCADE, related_name="Taxi")

    def __str__(self):
        return str(self.order)

    class Meta:
        verbose_name = "Order to Taxi"
        verbose_name_plural = "Orders to Taxi"
