from CRABClient.UserUtilities import config
from CRABAPI.RawCommand import crabCommand

#masses = ['4', '5', '6', '8']
masses = ['3p7', '4', '5', '6', '8']

inputProcesses = {
    '3p7': "/HToAATo4Tau_hadronic_tauDecayNoFilter_M3p7_Run3_2023/lpcml-3p7_miniAODSIM_tauNoFilter-f2508c1b00fdd2cc2fdf87ba946bfa33/USER",

    '4': "/HToAATo4Tau_hadronic_tauDecayNoFilter_M4_Run3_2023/lpcml-4_miniAODSIM_tauNoFilter-f2508c1b00fdd2cc2fdf87ba946bfa33/USER",

    '5': "/HToAATo4Tau_hadronic_tauDecayNoFilter_M5_Run3_2023/lpcml-5_miniAODSIM_tauNoFilter-f2508c1b00fdd2cc2fdf87ba946bfa33/USER",

    '6': "/HToAATo4Tau_hadronic_tauDecayNoFilter_M6_Run3_2023/lpcml-6_miniAODSIM_tauNoFilter-f2508c1b00fdd2cc2fdf87ba946bfa33/USER",

    '8': "/HToAATo4Tau_hadronic_tauDecayNoFilter_M8_Run3_2023/lpcml-8_miniAODSIM_tauNoFilter-f2508c1b00fdd2cc2fdf87ba946bfa33/USER"
}

for Mass in masses:

    cfg = config()

    # General
    cfg.General.requestName = f'{Mass}_nanoAODSIM-v15_tauNoFilter'
    cfg.General.workArea = 'crab_bigProduction'
    cfg.General.transferOutputs = True
    cfg.General.transferLogs = True

    # JobType
    cfg.JobType.pluginName = 'Analysis'
    cfg.JobType.psetName = 'step5_NanoAODv15_cfg.py'
    #cfg.JobType.psetName = 'step5_NanoAOD_v2_cfg.py'
    #cfg.JobType.maxMemoryMB = 8000
    cfg.JobType.numCores = 1 
    cfg.JobType.allowUndistributedCMSSW = True

    # Data
    cfg.Data.inputDBS = 'phys03'
    cfg.Data.inputDataset = inputProcesses[Mass]

    cfg.Data.splitting = 'FileBased'
    cfg.Data.unitsPerJob = 1

    cfg.Data.ignoreLocality = True

    cfg.Data.outLFNDirBase = '/store/group/lpcml/rchudasa/MCGenerationRun3'
    cfg.Data.publication = True
    cfg.Data.outputDatasetTag = cfg.General.requestName

    # Site
    cfg.Site.whitelist = [
        'T2_US_Caltech',
        'T2_US_MIT',
        'T2_US_Nebraska',
        'T2_US_Purdue',
        'T2_US_UCSD',
        'T2_US_Wisconsin',
        'T2_CH_CERN',
        'T2_AT_Vienna',
        'T2_BE_IIHE',
        'T2_BE_UCL',
        'T2_BR_SPRACE',
        'T2_BR_UERJ'
    ]

    cfg.Site.storageSite = 'T3_US_FNALLPC'

    print(f"Submitting job for mass {Mass}")

    try:
        crabCommand('submit', config=cfg)
    except Exception as e:
        print(f"Failed for {Mass}")
        print(e)
