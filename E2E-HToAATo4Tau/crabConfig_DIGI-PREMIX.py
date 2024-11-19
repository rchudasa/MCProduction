from CRABClient.UserUtilities import config
config = config()
#Mass = '14'#14
Mass = '3p7'#14

inputProcess_ = {
#'3p7': "/HToAATo4Tau_M3p7_Run3_2023/phys_diffraction-crab_GEN_SIM_HToAATo4Tau_M3p7-2b4ddcb85c0e2aa1bf748c03bd100e09/USER"
#, '14': "/HToAATo4Tau_M14_Run3_2023/phys_diffraction-crab_GEN_SIM_HToAATo4Tau_M14-738957dcd9af83922b6477ca7ce39cf9/USER"
'3p7': "/HToAATo4Tau_hadronic_tauDecay_M3p7_Run3_2023/phys_diffraction-crab_GEN_SIM_HToAATo4Tau_hadronic_tauDecay_M3p7-dcbefa18cc6f5cfd3c8d2c66024d0c0c/USER"
, '14': "/HToAATo4Tau_hadronic_tauDecay_M14_Run3_2023/phys_diffraction-crab_GEN_SIM_HToAATo4Tau_hadronic_tauDecay_M14_v2-86d29732f27943385419c19318645e94/USER"
}.get(Mass, None)

#config.section_('General')
config.General.requestName = '%s_DIGI-Premix_hadronicNew'%Mass
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

#config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step2_DIGI-RAW-HLT_cfg.py'
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
