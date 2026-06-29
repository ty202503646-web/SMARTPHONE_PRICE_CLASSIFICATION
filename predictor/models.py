from django.db import models

class Prediction(models.Model):
    battery_power = models.FloatField()
    blue = models.IntegerField()
    clock_speed = models.FloatField()
    dual_sim = models.IntegerField()
    fc = models.FloatField()
    four_g = models.IntegerField()
    int_memory = models.FloatField()
    m_dep = models.FloatField()
    mobile_wt = models.FloatField()
    n_cores = models.FloatField()
    pc = models.FloatField()
    px_height = models.FloatField()
    px_width = models.FloatField()
    ram = models.FloatField()
    sc_h = models.FloatField()
    sc_w = models.FloatField()
    talk_time = models.FloatField()
    three_g = models.IntegerField()
    touch_screen = models.IntegerField()
    wifi = models.IntegerField()

    prediction = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prediction #{self.id} - Class {self.prediction}"