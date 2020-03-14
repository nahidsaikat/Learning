from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute


class UserModel(Model):
    class Meta:
        table_name = 'users'
        region = 'us-east-1'
        read_capacity_units = 5
        write_capacity_units = 5
        host = "http://localhost:4569"
    email = UnicodeAttribute(hash_key=True)
    first_name = UnicodeAttribute()
    last_name = UnicodeAttribute()

