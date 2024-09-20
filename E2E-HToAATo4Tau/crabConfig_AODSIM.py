from CRABClient.UserUtilities import config
config = config()
Mass = '3p7'#14

inputProcess_ = {
'3p7': "/HToAATo4Tau_M3p7_Run3_2023/phys_diffraction-3p7_DIGI-Premix-c017b2c35ae16f5766f4c67c30206b8e/USER"
, '14': "/HToAATo4Tau_M14_Run3_2023/phys_diffraction-14_DIGI-Premix-c017b2c35ae16f5766f4c67c30206b8e/USER"
}.get(Mass, None)

#config.section_('General')
config.General.requestName = '%s_AODSIM'%Mass
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

#config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step3_AODSIM_cfg.py'
config.JobType.maxMemoryMB = 4000

config.Data.inputDBS = 'phys03'
config.JobType.allowUndistributedCMSSW = True
config.Data.inputDataset = inputProcess_

#config.Data.userInputFiles = open('%s'%inputProcess_).readlines()
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1 
#config.Data.outputPrimaryDataset = outputDataset_ 

config.Data.outLFNDirBase = '/store/group/phys_diffraction/rchudasa/MCGeneration'
config.Site.storageSite = 'T2_CH_CERN'
config.Data.publication = True 
config.Data.outputDatasetTag = config.General.requestName
