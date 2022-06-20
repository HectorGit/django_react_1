from django.db import models

# Create your models here.

class Notes(models.Model):
    title = models.CharField(max_length=60)
    content = models.CharField(max_length=120)

    def __str__(self):
        return self.title

# Possible models we will ---NEED--- to define : 

# bike_user_data 
# automatic column (id)
# user_id int4 
# hour int4
# date date 
# time_bike int4
# distance float4
# calories float4
# power float4
# timestamp timestamp

# Primary Key : user_id + hour + date

#------------------------------------------------------

# Models that would be ---NICE TO HAVE--- to define :