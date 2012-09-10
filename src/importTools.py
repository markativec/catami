import catamiWebPortal
import os
from django.core import serializers
from Force.models import users
import json
#==================================================#
# Created Dan marrable 5/09/2012
# d.marrable@ivec.org
#
# Edits :: Name : Date : description
#
#--------------------------------------------------#
# This module is adds functions for ingesting metadata
# files directly from a console - for now.  Files
# include .json .xml .yaml but must conform to 
# catami metadata datamodel
#==================================================#

class importMetaData():

    @staticmethod
    def importUsersFromFile(file):
        '''
        @brief This function reads in a metadta file that includes users information.
        @param file The file that holds the metata data.  formats include .json todo:-> .xml .yaml
        '''
        catamiWebPortal.logging.info("Importing metadata from " + file)
        fileName, fileExtension = os.path.splitext(file)
        
        
        if fileExtension == '.json':
            data = json.load(open(file))
            userModel = users(**data)
            userModel.save()
