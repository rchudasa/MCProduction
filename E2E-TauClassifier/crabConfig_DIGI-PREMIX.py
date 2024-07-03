from CRABClient.UserUtilities import config
config = config()
#Process = 'DYTauTau'
#Process = 'QCD'
#Process = 'WJets'
Process = 'TTbar'

inputProcess_ ={
        'DYTauTau': "DYToTauTau_M-50_13TeV-powheg_pythia8_GEN-SIM.txt",
        'QCD': "QCD_Pt-15to7000_TuneCP5_Flat.txt",
        'WJets': "WJetsToLNu_TuneCP5_13TeV_madgraphMLM-pythia8_GEN-SIM.txt",
        'TTbar': "TTToHadronic_TuneCP5_13TeV_powheg-pythia8_GEN-SIM.txt"
        }.get(Process, None)

outputDataset_ = {
        'DYTauTau':'DYToTauTau_M-50_13TeV-powheg_pythia8',
        'QCD':'QCD_Pt-15to7000_TuneCP5_Flat_13TeV_pythia8',
        'WJets':'WJetsToLNu_TuneCP5_13TeV_madgraphMLM-pythia8',
        'TTbar':'TTToHadronic_TuneCP5_13TeV_powheg-pythia8'
        }.get(Process, None)

#config.section_('General')
config.General.requestName = '%s_DIGI-Premix'%Process
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

#config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step2_DIGIPremix_cfg.py'
config.JobType.maxMemoryMB = 4000

config.Data.inputDBS = 'phys03'
config.JobType.allowUndistributedCMSSW = True
config.Data.userInputFiles = open('%s'%inputProcess_).readlines()
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1 
config.Data.outputPrimaryDataset = outputDataset_ 

config.Data.outLFNDirBase = '/store/group/lpcml/rchudasa/MCGeneration'
config.Data.publication = True 
config.Site.storageSite = 'T3_US_FNALLPC'
config.Data.outputDatasetTag = config.General.requestName
