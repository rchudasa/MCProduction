from CRABClient.UserUtilities import config
config = config()

#config.section_('General')
config.General.requestName = 'GJet_Pt-20to40_DoubleEMEnriched_DIGI-RECO-v2'
config.General.workArea = 'crab_mc'
config.General.transferOutputs = True
config.General.transferLogs = True

#config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'digiToRecoStep_withPU_cfg.py'
config.JobType.maxMemoryMB = 4000

config.Data.inputDBS = 'phys03'
config.JobType.allowUndistributedCMSSW = True
config.Data.inputDataset ='/GJet_Pt-20to40_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_pythia8/lpcml-crab_GJet_Pt-20to40_DoubleEMEnriched_GEN-SIM-v2-486ef3f8d8f2f08cc5ce0d088bdf04c0/USER'
#config.Data.userInputFiles = open('GJet_Pt-20to40_DoubleEMEnriched_GEN-SIM_999.txt').readlines()
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1 
#config.Data.outputPrimaryDataset = 'GJet_Pt-20to40_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_pythia8'

config.Data.outLFNDirBase = '/store/group/lpcml/rchudasa/MCGeneration'
config.Data.publication = True 
config.Site.storageSite = 'T3_US_FNALLPC'
config.Data.outputDatasetTag = config.General.requestName
