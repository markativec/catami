from django.db import models
from django_postgresql.fields.arrays import ArrayField
from django_postgresql.manager import PgManager
from django.contrib.gis.db import models

class campaign(models.Model):
    '''
    @brief A campain describes a field campaign that has many deployments.
    '''
    #==================================================#
    # description <Text> : is a general description of the campaign
    # associateResearchers <array> :
    # associatedPublications <array> :
    # associatedResearchGrant <array> :
    # deployments <unique id> :
    # date start <dateTime> :
    # date End <dateTime> : 
    #==================================================#

    description=models.TextField()
    associatedResearchers=ArrayField(dbtype='text',null=True)
    associatedPublications=ArrayField(dbtype='text',null=True)
    associatedResearchGrant=ArrayField(dbtype='text',null=True)
    deployments=models.UniqueField()

class users(models.Model):
    '''
    @breif contains all of the information for the database users
    '''
    #==================================================#
    # name <Char> : The name of the usr
    # title <Char> : Mr, Mrs etc
    # Organisation <Char> : Name of the organisation the user works for
    # email <email> : The users email
    #==================================================#

    name=models.CharField(max_length=200)
    title=models.CharField(max_length=200)
    organisation=models.CharField(max_length=200)
    email=models.EmailField()
 
class auvDeployment(modles.Model):
    '''
    @brief AUV meta data
    '''
    #==================================================#
    # StartPosition : <point>
    # distanceCovered : <double>
    # startTimeStamp : <dateTime>
    # endTimeStamp : <dateTime>
    # transectShape : <>
    # missionAim : <Text>
    # minDepth : <double>
    # maxDepth : <double> 
    #==================================================#

    startPosition=models.PointField()
    distanceCovered=models.DoubleField()
    startTimeStamp=models.DateTimeField()
    endTimeStamp=models.DateTimeField()
    transectShape=models.PolygonField()
    missionAim=models.TextField()
    minDepth=models.DoubleField()
    maxDepth=models.DoubleField()
