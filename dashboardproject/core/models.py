from django.db import models

# Create your models here.

class Notes(models.Model):
    title = models.CharField(max_length=60)
    content = models.CharField(max_length=120)

    def __str__(self):
        return self.title

# Possible models we will ---NEED--- to define : 

# bike_user_data (Primary Key (compound) : user_id + hour + date)
# automatic column (id)
# user_id int4 
# hour int4
# date date 
# time_bike int4
# distance float4
# calories float4
# power float4
# timestamp timestamp



#------------------------------------------------------

# Models that would be ---NICE TO HAVE--- to define :

# challenges (Primary Key : id )
# challenge_id int4
# challenge_name varchar
# task_id int4
# task_name varchar
# task varchar
# completion_condition varchar

# custom_challenge (Primary Key : id)
# user_id int4
# custom_title varchar 
# custom_des varchar
# position varchar
# amount int4
# units varchar
# recurrence varchar