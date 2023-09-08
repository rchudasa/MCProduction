from CRABClient.UserUtilities import config
config = config()

#config.section_('General')
config.General.requestName = 'DYToTauTau_M-50_13TeV-powheg_pythia8_GEN-SIM-v2'
config.General.workArea = 'crab_mc'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.inputFiles  = ['/eos/user/r/rchudasa/e2e_project/Z_slc7_amd64_gcc700_CMSSW_10_6_28_my_ZTauTau-v2.tgz']
config.JobType.pyCfgParams = ['gridpack=../Z_slc7_amd64_gcc700_CMSSW_10_6_28_my_ZTauTau-v2.tgz']

#config.section_('JobType')
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'DYToTauTau_M-50_13TeV-powheg_pythia8_GEN-SIM_cfg.py'
config.Data.outputPrimaryDataset = 'DYToTauTau_M-50_13TeV-powheg_pythia8'

config.JobType.allowUndistributedCMSSW = True
#config.JobType.numCores = 8
#config.JobType.eventsPerLumi=100
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob =2000
NJOBS =2000
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS

config.Data.outLFNDirBase = '/store/group/lpcml/rchudasa/MCGeneration'
#config.Data.publication = False 
#config.Data.publication = True 
config.Site.storageSite = 'T3_US_FNALLPC'
