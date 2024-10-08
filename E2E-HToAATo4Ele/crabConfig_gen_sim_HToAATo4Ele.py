from CRABClient.UserUtilities import config
config = config()
# See parameter defintions here: https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile#CRAB_configuration_parameters
Mass='4' # Mass of A is generally integer but put as string if need decimal.
# Local job directory will be created in:
config.General.requestName = 'GEN_SIM_HToAATo4Ele_M%s'%Mass
config.General.workArea = 'crab_MC'
config.General.transferOutputs = True
config.General.transferLogs = True

# CMS cfg file goes here:
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'GEN_SIM_HToAATo4Ele_M%sGeV_cfg.py'%Mass
config.Data.outputPrimaryDataset = 'HToAATo4Ele_M%s_Run3_2023'%Mass

#config.JobType.maxMemoryMB = 2800

# Define units per job here:
config.JobType.allowUndistributedCMSSW = True
config.JobType.eventsPerLumi=500
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 1100 # units: large number is given because HToaaTo4Tau has filters about 8 % eff
NJOBS = 100
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.publication = True

# Output files will be stored in config.Site.storageSite at directory:
config.Data.outLFNDirBase = '/store/group/phys_diffraction/rchudasa/MCGeneration'
config.Site.storageSite = 'T2_CH_CERN'
