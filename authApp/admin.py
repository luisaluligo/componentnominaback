from django.contrib import admin
from .models.user import User
from .models.empleado import Empleado
from .models.contrato import Contrato
from .models.tiponovedad import Tiponovedad
from .models.novedad import Novedad
from .models.nomina import Nomina

admin.site.register(User)
admin.site.register(Empleado)
admin.site.register(Contrato)
admin.site.register(Tiponovedad)
admin.site.register(Novedad)
admin.site.register(Nomina)