'''
This is the main import file to create a common namespace.
'''
import logging
import logging.config
import ConfigParser
import src.importTools as importTools
from Force.models import *

#==================================================#
# Initialize the Django settings etc
#==================================================#

#==================================================#
# Open the config file and read contents
#==================================================#
config = ConfigParser.ConfigParser()  #For general configs
config.readfp(open('catamiPortalConfigs.cfg'))

logging.config.fileConfig('logging.cfg') # For logging configs
logging=logging.getLogger('catamiPortal')

#loggingLevel=config.get('defaults','loggingLevel')

#if loggingLevel=='DEBUG':
#    logLevel=logging.DEBUG

#==================================================#
# Set up the log file.
#==================================================#
#logging.basicConfig(filename='log/catamiPortal.log', level=logLevel,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')



