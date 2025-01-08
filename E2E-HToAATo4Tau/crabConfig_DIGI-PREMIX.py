from CRABClient.UserUtilities import config
config = config()
#Mass = '14'#14
Mass = '3p7'#14
#Mass = 'WJets'

inputProcess_ = {
#'3p7': "/HToAATo4Tau_M3p7_Run3_2023/phys_diffraction-crab_GEN_SIM_HToAATo4Tau_M3p7-2b4ddcb85c0e2aa1bf748c03bd100e09/USER"
#, '14': "/HToAATo4Tau_M14_Run3_2023/phys_diffraction-crab_GEN_SIM_HToAATo4Tau_M14-738957dcd9af83922b6477ca7ce39cf9/USER"
#'3p7': "/HToAATo4Tau_hadronic_tauDecay_M3p7_Run3_2023/phys_diffraction-crab_GEN_SIM_HToAATo4Tau_hadronic_tauDecay_M3p7-dcbefa18cc6f5cfd3c8d2c66024d0c0c/USER"
#, '14': "/HToAATo4Tau_hadronic_tauDecay_M14_Run3_2023/phys_diffraction-crab_GEN_SIM_HToAATo4Tau_hadronic_tauDecay_M14_v2-86d29732f27943385419c19318645e94/USER"
'WJets':'WJets_digiraw.txt'
,'3p7': "/HToAATo4Tau_hadronic_tauDecay_M3p7_Run3_2023/lpcml-crab_GEN_SIM_HToAATo4Tau_tauDecay_M3p7-dcbefa18cc6f5cfd3c8d2c66024d0c0c/USER"
,'4': "/HToAATo4Tau_hadronic_tauDecay_M4_Run3_2023/lpcml-crab_GEN_SIM_HToAATo4Tau_tauDecay_M4-65fda359da575d58201444a7a8375d6b/USER"
,'5': "/HToAATo4Tau_hadronic_tauDecay_M5_Run3_2023/lpcml-crab_GEN_SIM_HToAATo4Tau_tauDecay_M5-eb1606952c4e09f97648e0927768ea7f/USER"
,'6': "/HToAATo4Tau_hadronic_tauDecay_M6_Run3_2023/lpcml-crab_GEN_SIM_HToAATo4Tau_tauDecay_M6-8c4e993c2f7de8c3cb712019877abf5a/USER"
}.get(Mass, None)

#config.section_('General')
config.General.requestName = '%s_DIGI-Premix_8Gb_ignoreLocality'%Mass
config.General.workArea = 'crab_bigProduction'
config.General.transferOutputs = True
config.General.transferLogs = True

#config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step2_DIGI-RAW-HLT_pileupFileList_cfg.py'
config.JobType.maxMemoryMB = 8000
config.JobType.numCores = 4 

config.Data.inputDBS = 'phys03'
config.JobType.allowUndistributedCMSSW = True
config.Data.inputDataset = inputProcess_

#config.Data.userInputFiles = open('%s'%inputProcess_).readlines()
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1 
#config.Data.outputPrimaryDataset = 'WtoLNu-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8' 

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
