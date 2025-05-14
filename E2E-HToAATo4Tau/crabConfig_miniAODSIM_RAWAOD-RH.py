from CRABClient.UserUtilities import config
config = config()
Mass = '14'#14

inputProcess_ = {
#'3p7': "/HToAATo4Tau_M3p7_Run3_2023/phys_diffraction-3p7_AODSIM-1aff9968d58b5116c6a273898fab2d56/USER"
#, '14': "/HToAATo4Tau_M14_Run3_2023/phys_diffraction-14_AODSIM-1aff9968d58b5116c6a273898fab2d56/USER"
#'3p7': "/HToAATo4Tau_hadronic_tauDecay_M3p7_Run3_2023/phys_diffraction-3p7_AODSIM_hadronic-1aff9968d58b5116c6a273898fab2d56/USER"
#,'14': "/HToAATo4Tau_hadronic_tauDecay_M14_Run3_2023/phys_diffraction-14_AODSIM_hadronic-1aff9968d58b5116c6a273898fab2d56/USER"
'3p7': "/HToAATo4Tau_hadronic_tauDecay_M3p7_Run3_2023/lpcml-3p7_AODSIM_newBigProd-953b1873547799e513f8a43f2c57e3b2/USER"
,'8': "/HToAATo4Tau_hadronic_tauDecay_M8_Run3_2023/lpcml-signal_Mass_8_AODSIM_multiThreads-953b1873547799e513f8a43f2c57e3b2/USER"
,'14': "/HToAATo4Tau_hadronic_tauDecay_M14_Run3_2023/lpcml-signal_Mass_14_AODSIM_multiThreads-953b1873547799e513f8a43f2c57e3b2/USER"
}.get(Mass, None)

#config.section_('General')
config.General.requestName = '%s_miniAODSIM_RAWAOD-RHv4'%Mass
config.General.workArea = 'crab_projects_RAWAOD-RH'
config.General.transferOutputs = True
config.General.transferLogs = True

#config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step4_miniAOD_with_RAWAOD_RecHit_cfg.py'
config.JobType.maxMemoryMB = 4000

config.Data.inputDBS = 'phys03'
config.JobType.allowUndistributedCMSSW = True
#config.Data.inputDataset = inputProcess_
config.Data.userInputFiles = open('H2AA4Tau_hadronic_tauDecay_M14_AOD.txt').readlines()

config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1 
config.Data.totalUnits = 10
config.JobType.numCores = 4
config.Data.outputPrimaryDataset = 'HToAATo4Tau_hadronic_tauDecay_M14_Run3_2023' 
config.Site.whitelist = [
    'T2_US_Caltech', 'T2_US_Nebraska', 'T2_US_Purdue', 'T2_US_UCSD', 'T2_US_Wisconsin','T2_CH_CERN',
    'T2_AT_Vienna', 'T2_BE_IIHE', 'T2_BE_UCL', 'T2_BR_SPRACE', 'T2_BR_UERJ','T3_US_FNALLPC'
]


config.Data.outLFNDirBase = '/store/group/phys_diffraction/rchudasa/MCGeneration'
config.Site.storageSite = 'T2_CH_CERN'
config.Data.publication = True 
config.Data.outputDatasetTag = config.General.requestName
