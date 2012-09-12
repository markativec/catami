import catamiWebPortal
import os
from django.core import serializers
from Force.models import *
import json
from django.contrib.gis.geos import GEOSGeometry

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
#--------------------------------------------------#
# @todo Include more import file formats.
# @todo Include more deployment types
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
            dataModel = users(**data)
            dataModel.full_clean()
            dataModel.save()
        else:
            catamiWebPortal.logging.error("No supported fileformat found.  Data not logged :: file extension :: " + fileExtension)

    @staticmethod
    def importImageFromFile(file):
        '''
        @brief This function reads in a metadta file that includes users information.
        @param file The file that holds the metata data.  formats include .json todo:-> .xml .yaml
        '''
        catamiWebPortal.logging.info("Importing metadata from " + file)
        fileName, fileExtension = os.path.splitext(file)
                
        if fileExtension == '.json':
            data = json.load(open(file))
            dataModel = image(**data)
            dataModel.full_clean()
            dataModel.save()
        else:
            catamiWebPortal.logging.error("No supported fileformat found.  Data not logged :: file extension :: " + fileExtension)

    @staticmethod
    def importStereoImagesFromFile(file):
        '''
        @brief This function reads in a metadta file that includes users information.
        @param file The file that holds the metata data.  formats include .json todo:-> .xml .yaml
        '''
        catamiWebPortal.logging.info("Importing metadata from " + file)
        fileName, fileExtension = os.path.splitext(file)
                
        if fileExtension == '.json':
            data = json.load(open(file))
            dataModel = stereoImages(**data)
            dataModel.full_clean()
            dataModel.save()
        else:
            catamiWebPortal.logging.error("No supported fileformat found.  Data not logged :: file extension :: " + fileExtension)

            

    @staticmethod
    def importCampaignFromFile(file):
        '''
        @brief This function reads in a metadta file that includes campaign information.
        @param file The file that holds the metata data.  formats include .json todo:-> .xml .yaml
        '''
        catamiWebPortal.logging.info("Importing metadata from " + file)
        fileName, fileExtension = os.path.splitext(file)
        
        
        if fileExtension == '.json':
            data = json.load(open(file))
            dataModel = campaign(**data)
            dataModel.full_clean()
            dataModel.save()
        else:
            catamiWebPortal.logging.error("No supported fileformat found.  Data not logged :: file extension :: " + fileExtension)

            

    @staticmethod
    def importDeploymentFromFile(file):
        '''
        @brief This function reads in a metadta file that includes campaign information.  Destinction between deployment types is made on the fine name.  <type><deployment>.<supported text> auvdeployment.json
        @param file The file that holds the metata data.  formats include .json todo:-> .xml .yaml
        '''
        catamiWebPortal.logging.info("Importing metadata from " + file)
        fileName, fileExtension = os.path.splitext(file)

        if fileExtension == '.json':
            if os.path.basename(fileName.upper()) == 'AUVDEPLOYMENT':
                catamiWebPortal.logging.info("Found valid deployment file")
                data = json.load(open(file))
                dataModel = auvDeployment(**data)
                try:
                    dataModel.full_clean()
                except Exception as e:
                    catamiWebPortal.logging.warning("Possible validation error :: " + str(e))
                    
                dataModel.save()
            else:
                catamiWebPortal.logging.error("No supported filname found.  Data not logged :: filename :: " + file)
        else:
            catamiWebPortal.logging.error("No supported fileformat found.  Data not logged :: file extension :: " + fileExtension)
