#GEN-Run3Summer23BPixwmLHEGS-00489 
from CRABClient.UserUtilities import config
config = config()

#config.section_('General')
config.General.requestName = 'WJetsToLNu_GEN-SIM'
config.General.workArea = 'crab_MC'
config.General.transferOutputs = True
config.General.transferLogs = True

#config.section_('JobType')
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'GEN-SIM_WJets_cfg.py'
config.Data.outputPrimaryDataset = 'WtoLNu-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8'

config.JobType.allowUndistributedCMSSW = True
config.JobType.maxMemoryMB = 8000
config.JobType.numCores = 8
#config.JobType.eventsPerLumi=100
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob =2000
NJOBS = 1000
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS

config.Data.outLFNDirBase = '/store/group/lpcml/rchudasa/MCGenerationRun3'
#config.Data.publication = False 
#config.Data.publication = True 
config.Site.storageSite = 'T3_US_FNALLPC'
