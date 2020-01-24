from django.contrib import admin
from matrix.models import signup,local_bodies_id,Node,comment
# Register your models here.
admin.site.register(signup)
admin.site.register(local_bodies_id)
admin.site.register(Node)
admin.site.register(comment)