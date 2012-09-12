from Force.models import auvDeployment
from django.contrib import admin

class AuvDeploymentAdmin(admin.ModelAdmin):
	list_display = ('startTimeStamp','endTimeStamp','distanceCovered','minDepth','maxDepth','missionAim')

admin.site.register(auvDeployment,AuvDeploymentAdmin)
