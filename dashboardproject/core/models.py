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

# monthly_bike_data (Primary Key : id )
# user_id int4
# time_bike int4
# distance float4
# calories float4
# power float4
# timestamp timestamp

# desk_user_data (Primary Key (compound) : user_id + hour + date)
# user_id int4 
# hour int4
# date date 
# time_active int4
# time_total int4
# calories float4
# timestamp timestamp
# movements int4

# monthly_desk_data (Primary Key : id)
# user_id int4
# time_active int4
# time_total float4
# calories float4
# timestamp timestamp
# movements int4

# user_devices (Primary Key (compound) : user_id + peripheral_name)
# user_id int4 
# device_name varchar
# peripheral_name varchar
# peripheral_uuid varchar
# last_date timestamp
# is_autoconnection bool
# last_connected_device varchar
# desk_firmware_vesrion varchar
# last_connected_device_version varchar

# user settings (Primary Key : id)
# photo_url varchar
# about_me varchar
# last_seen timestamp
# height float4
# weight float4
# dob timestamp
# init_deskheight varchar
# sitting_preset float4
# biking_preset float4
# standing_preset float4
# is_metric bool
# is_birthday bool
# name varchar
# gender varchar
# notifications int4
# privacy int4
# vibration bool
# accelerometer bool

# user_table (Primary Key : id)
# username varchar
# email varchar
# password_hash varchar
# role varchar
# user_created timestamp
# shipping_id varchar

#------------------------------------------------------

# Models that would be ---NICE TO HAVE--- to define :

# desk_presets (Primary Key : id)
# user_id int4
# preset_id int4
# preset_name varchar
# preset_height int4

# desk_routines (Primary Key : id)
# routine_id int4
# routine_name varchar
# active_min int4
# rest_min int4
# active_height int4
# rest_height int4
# is_favourite bool
# is_auto bool
# auto_endtime timestamp
# user_id int4

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

# user_challenges (Primary Key : id)
# challenge_id int4
# user_id int4 
# completed_date timestamp
# task_id int4
# is_favourite bool

#------------------------------------------------------

# Models that would be ---NICE TO AUGMENT--- :
