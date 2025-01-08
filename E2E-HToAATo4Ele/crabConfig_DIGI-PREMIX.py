from CRABClient.UserUtilities import config
config = config()

Mass = '4Ele'#14

inputProcess_ = {
'WJets':'WJets_digiraw.txt'
,'4Ele':'HAA4Ele_gen_sim.txt'
,'3p7': "/HToAATo4Tau_hadronic_tauDecay_M3p7_Run3_2023/lpcml-crab_GEN_SIM_HToAATo4Tau_tauDecay_M3p7-dcbefa18cc6f5cfd3c8d2c66024d0c0c/USER"
,'4': "/HToAATo4Tau_hadronic_tauDecay_M4_Run3_2023/lpcml-crab_GEN_SIM_HToAATo4Tau_tauDecay_M4-65fda359da575d58201444a7a8375d6b/USER"
,'5': "/HToAATo4Tau_hadronic_tauDecay_M5_Run3_2023/lpcml-crab_GEN_SIM_HToAATo4Tau_tauDecay_M5-eb1606952c4e09f97648e0927768ea7f/USER"
,'6': "/HToAATo4Tau_hadronic_tauDecay_M6_Run3_2023/lpcml-crab_GEN_SIM_HToAATo4Tau_tauDecay_M6-8c4e993c2f7de8c3cb712019877abf5a/USER"
}.get(Mass, None)

#config.section_('General')
config.General.requestName = '%s_DIGI-Premix_8Gb_ignoreLocality'%Mass
config.General.workArea = 'crab_triggerCheck'
config.General.transferOutputs = True
config.General.transferLogs = True

#config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step2_DIGI-RAW-HLT_pileupFileList_cfg.py'
config.JobType.maxMemoryMB = 8000
config.JobType.numCores = 4 

config.Data.inputDBS = 'phys03'
config.JobType.allowUndistributedCMSSW = True
#config.Data.inputDataset = inputProcess_

config.Data.userInputFiles = open('%s'%inputProcess_).readlines()
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1 
config.Data.outputPrimaryDataset = 'HToAATo4Ele_Run3_2023' 

#config.Data.outLFNDirBase = '/store/group/phys_diffraction/rchudasa/MCGeneration'
#config.Site.storageSite = 'T2_CH_CERN'
config.Data.ignoreLocality = True
config.Site.whitelist = [
    'T2_US_Caltech', 'T2_US_MIT', 'T2_US_Nebraska', 'T2_US_Purdue', 'T2_US_UCSD', 'T2_US_Wisconsin','T2_CH_CERN',
    'T2_AT_Vienna', 'T2_BE_IIHE', 'T2_BE_UCL', 'T2_BR_SPRACE', 'T2_BR_UERJ'
] 
config.Data.outLFNDirBase = '/store/group/lpcml/rchudasa/MCGenerationRun3'
config.Site.storageSite = 'T3_US_FNALLPC'
config.Data.publication = True 
config.Data.outputDatasetTag = config.General.requestName
