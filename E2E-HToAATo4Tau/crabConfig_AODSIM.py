from CRABClient.UserUtilities import config
config = config()
#Mass = 'DYto2L'
Mass = 'QCD'
#Mass = 'TTbar'
#Mass = 'HTauTau'

inputDataset_ ={
'QCD':'/QCD_PT-15to7000_TuneCP5_13p6TeV_pythia8/Run3Summer23DRPremix-castor_130X_mcRun3_2023_realistic_v14-v1/GEN-SIM-RAW'
,'TTbar':'/TT_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixDRPremix-130X_mcRun3_2023_realistic_postBPix_v2-v2/GEN-SIM-RAW'
,'HTauTau':'/GluGluHToTauTau_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixDRPremix-130X_mcRun3_2023_realistic_postBPix_v2-v2/GEN-SIM-RAW'
}.get(Mass, None)


inputProcess_ = {
#'3p7': "/HToAATo4Tau_M3p7_Run3_2023/phys_diffraction-3p7_DIGI-Premix-c017b2c35ae16f5766f4c67c30206b8e/USER"
#, '14': "/HToAATo4Tau_M14_Run3_2023/phys_diffraction-14_DIGI-Premix-c017b2c35ae16f5766f4c67c30206b8e/USER"
'3p7': "/HToAATo4Tau_hadronic_tauDecay_M3p7_Run3_2023/phys_diffraction-3p7_DIGI-Premix_hadronic-c017b2c35ae16f5766f4c67c30206b8e/USER"
,'14':"/HToAATo4Tau_hadronic_tauDecay_M14_Run3_2023/phys_diffraction-14_DIGI-Premix_hadronic-c017b2c35ae16f5766f4c67c30206b8e/USER"
,'DYto2L':"DYto2L_RAW.txt"
,'QCD':['/QCD_PT-15to7000_TuneCP5_13p6TeV_pythia8/Run3Summer23DRPremix-castor_130X_mcRun3_2023_realistic_v14-v1/GEN-SIM-RAW#de0ee2c4-0322-45a5-85df-40033b0f4432']
,'TTbar':['/TT_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixDRPremix-130X_mcRun3_2023_realistic_postBPix_v2-v2/GEN-SIM-RAW#0583f9a4-1e1e-46f6-b2b3-da4538afb308']
,'HTauTau':['/GluGluHToTauTau_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixDRPremix-130X_mcRun3_2023_realistic_postBPix_v2-v2/GEN-SIM-RAW#5c39c6b8-d0db-4b6f-ae14-a11529c0e9e9']
}.get(Mass, None)

outputDataset_ = {
        '3p7':'HToAATo4Tau_hadronic_tauDecay_M3p7_Run3_2023',
        '14' : 'HToAATo4Tau_hadronic_tauDecay_M14_Run3_2023',
        'DYto2L':'DYto2L_M-50_TuneCP5_13p6TeV_pythia8',
        'QCD':'QCD_PT-15to7000_TuneCP5_13p6TeV_pythia8',
        'TTbar':'TT_TuneCP5_13p6TeV_powheg-pythia8'
}.get(Mass, None)

#config.section_('General')
config.General.requestName = '%s_AODSIM_oneBlock_multiThreads_8Gb_new'%Mass
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.Data.inputDataset =inputDataset_
config.Data.inputBlocks =inputProcess_
#config.section_('JobType')
#config.JobType.pluginName = 'PrivateMC'
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step3_AODSIM_cfg.py'
#config.JobType.maxMemoryMB = 4000
config.JobType.maxMemoryMB = 8000
config.JobType.numCores = 8 

config.Data.inputDBS = 'global'
#config.Data.inputDBS = 'phys03'
config.JobType.allowUndistributedCMSSW = True
#config.Data.inputDataset = inputProcess_

#config.Data.userInputFiles = open('%s'%inputProcess_).readlines()
#config.Data.splitting = 'EventBased'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1 
#config.Data.totalUnits = 500000 
#config.Data.outputPrimaryDataset = outputDataset_ 

#config.Site.whitelist = ['T2_IN_TIFR']
config.Data.outLFNDirBase = '/store/group/lpcml/rchudasa/MCGenerationRun3'
#config.Site.storageSite = 'T2_CH_CERN'
config.Site.storageSite = 'T3_US_FNALLPC'
config.Data.publication = True 
config.Data.outputDatasetTag = config.General.requestName
