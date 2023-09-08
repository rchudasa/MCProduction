# Auto generated configuration file
# using:
# Revision: 1.19
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v
# with command line options: Configuration/GenProduction/python/HIG-RunIISummer20UL18GEN-00066-fragment.py --python_filename gen_HIG_RunIISummer20UL18_00066_1_cfg.py --eventcontent RAWSIM --datatier GEN --fileout file:Gen_HIG_RunIISummer20UL18_00066.root --conditions 106X_upgrade2018_realistic_v15_L1v1 --step GEN --geometry DB:Extended --beamspot Realistic25ns13TeVEarly2018Collision --era Run2_2018 --runUnscheduled --no_exec --mc -n 1000
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2018_cff import Run2_2018

process = cms.Process('GEN',Run2_2018)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic25ns13TeVEarly2018Collision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

# process.MessageLogger = cms.Service("MessageLogger",
#         destinations   = cms.untracked.vstring('detailedInfo'),
#         categories      = cms.untracked.vstring('eventNumber'),
#         detailedInfo    = cms.untracked.PSet(eventNumber = cms.untracked.PSet(reportEvery = cms.untracked.int32(10000))),
# )

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True)

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('HIG-RunIISummer20UL18GEN-00066-fragment.py nevts:1000'),
    # annotation = cms.untracked.string('Configuration/GenProduction/python/HIG-RunIISummer20UL18GEN-00066-fragment.py nevts:1000'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(1),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(20971520),
    # fileName = cms.untracked.string('file:/eos/user/b/bhbam/H_AA_4tau/GEN_HIG_RunIISummer20UL18_00066.root'), # uncomment for production in local
    fileName = cms.untracked.string('file:GEN-SIM_HToAAToTauTau_M3p6_2018UL.root'), # uncomment when crab submission
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '106X_upgrade2018_realistic_v4', '')


# process.oniafilter = cms.EDFilter("PythiaFilter",
#     MaxEta = cms.untracked.double(1000.0),
#     MinEta = cms.untracked.double(-1000.0),
#     MinPt = cms.untracked.double(30.0),
#     ParticleID = cms.untracked.int32(35),
#     Status = cms.untracked.int32(2)
# )
# # #

process.genHToAATo4TauFilter = cms.EDFilter("GenHToAATo4TauFilter",
   src       = cms.InputTag("genParticles"), #GenParticles collection as input
   nHiggs    = cms.double(1),    #Number of H->AA->4Tau candidates
   tauPtCut  = cms.double(10.0), #at least a GenTau with this minimum pT
   tauEtaCut = cms.double(2.4),    #GenTau eta max value
   taudRCut  = cms.double(0.4)   #GenTauTau dR max value for merged taus
   # taudRCut  = cms.double(0.4)   #GenTauTau dR min value for not merged taus
)

# process.generator = cms.EDFilter("Pythia8ConcurrentGeneratorFilter",
process.generator = cms.EDFilter("Pythia8GeneratorFilter",
    PythiaParameters = cms.PSet(
        parameterSets = cms.vstring(
            'pythia8CommonSettings',
            'pythia8CP5Settings',
            'pythia8PSweightsSettings',
            'processParameters'
        ),
        processParameters = cms.vstring(
            'Higgs:useBSM = on',
            'HiggsBSM:gg2H2 = on',
            '35:m0 = 125.',  # Higgs mass
            '35:onMode = off', # turn off all Higgs decay mode
            '35:onIfMatch = 25 25', # higgs to A A decay mode on
            '25:mMin = 3.6', # min mass of A
            '25:m0 = 3.6', # mass of A
            '25:onMode = off', # # turn off A all decay mode
            '25:onIfMatch = 15 -15', # A decay to tau tau mode on
            # Hadronic tau mode selection only
            '15:onMode  = on',
            '15:offIfAny = 11 -11 13 -13',


            # '-15:offIfAny = -11 -13',
            # '15:onMode = off' ,#tau decay off
            # '-15:onMode = off', # tau_bar decay off
            # '15:onIfMatch = 16 -24', # tau decay into tau_neutrino and W- boson
            # '-15:onIfMatch = -16 24' ,# tau decay into tau_anti_neutrino and W+ boson
            # leptonic tau decay turn off
            # '15:offIfMatch = 11 -12 16',
            # '15:offIfMatch = 13 -13 16',
            # '-15:offIfMatch = -11 12 -16',
            # '-15:offIfMatch = -13 13 -16',


        ),
        pythia8CP5Settings = cms.vstring(
            'Tune:pp 14',
            'Tune:ee 7',
            'MultipartonInteractions:ecmPow=0.03344',
            'MultipartonInteractions:bProfile=2',
            'MultipartonInteractions:pT0Ref=1.41',
            'MultipartonInteractions:coreRadius=0.7634',
            'MultipartonInteractions:coreFraction=0.63',
            'ColourReconnection:range=5.176',
            'SigmaTotal:zeroAXB=off',
            'SpaceShower:alphaSorder=2',
            'SpaceShower:alphaSvalue=0.118',
            'SigmaProcess:alphaSvalue=0.118',
            'SigmaProcess:alphaSorder=2',
            'MultipartonInteractions:alphaSvalue=0.118',
            'MultipartonInteractions:alphaSorder=2',
            'TimeShower:alphaSorder=2',
            'TimeShower:alphaSvalue=0.118',
            'SigmaTotal:mode = 0',
            'SigmaTotal:sigmaEl = 21.89',
            'SigmaTotal:sigmaTot = 100.309',
            'PDF:pSet=LHAPDF6:NNPDF31_nnlo_as_0118'
        ),
        pythia8CommonSettings = cms.vstring(
            'Tune:preferLHAPDF = 2',
            'Main:timesAllowErrors = 10000',
            'Check:epTolErr = 0.01',
            'Beams:setProductionScalesFromLHEF = off',
            'SLHA:keepSM = on',
            'SLHA:minMassSM = 1000.',
            'ParticleDecays:limitTau0 = on',
            'ParticleDecays:tau0Max = 10',
            'ParticleDecays:allowPhotonRadiation = on'
        ),
        pythia8PSweightsSettings = cms.vstring(
            'UncertaintyBands:doVariations = on',
            'UncertaintyBands:List = {isrRedHi isr:muRfac=0.707,fsrRedHi fsr:muRfac=0.707,isrRedLo isr:muRfac=1.414,fsrRedLo fsr:muRfac=1.414,isrDefHi isr:muRfac=0.5,fsrDefHi fsr:muRfac=0.5,isrDefLo isr:muRfac=2.0,fsrDefLo fsr:muRfac=2.0,isrConHi isr:muRfac=0.25,fsrConHi fsr:muRfac=0.25,isrConLo isr:muRfac=4.0,fsrConLo fsr:muRfac=4.0,fsr_G2GG_muR_dn fsr:G2GG:muRfac=0.5,fsr_G2GG_muR_up fsr:G2GG:muRfac=2.0,fsr_G2QQ_muR_dn fsr:G2QQ:muRfac=0.5,fsr_G2QQ_muR_up fsr:G2QQ:muRfac=2.0,fsr_Q2QG_muR_dn fsr:Q2QG:muRfac=0.5,fsr_Q2QG_muR_up fsr:Q2QG:muRfac=2.0,fsr_X2XG_muR_dn fsr:X2XG:muRfac=0.5,fsr_X2XG_muR_up fsr:X2XG:muRfac=2.0,fsr_G2GG_cNS_dn fsr:G2GG:cNS=-2.0,fsr_G2GG_cNS_up fsr:G2GG:cNS=2.0,fsr_G2QQ_cNS_dn fsr:G2QQ:cNS=-2.0,fsr_G2QQ_cNS_up fsr:G2QQ:cNS=2.0,fsr_Q2QG_cNS_dn fsr:Q2QG:cNS=-2.0,fsr_Q2QG_cNS_up fsr:Q2QG:cNS=2.0,fsr_X2XG_cNS_dn fsr:X2XG:cNS=-2.0,fsr_X2XG_cNS_up fsr:X2XG:cNS=2.0,isr_G2GG_muR_dn isr:G2GG:muRfac=0.5,isr_G2GG_muR_up isr:G2GG:muRfac=2.0,isr_G2QQ_muR_dn isr:G2QQ:muRfac=0.5,isr_G2QQ_muR_up isr:G2QQ:muRfac=2.0,isr_Q2QG_muR_dn isr:Q2QG:muRfac=0.5,isr_Q2QG_muR_up isr:Q2QG:muRfac=2.0,isr_X2XG_muR_dn isr:X2XG:muRfac=0.5,isr_X2XG_muR_up isr:X2XG:muRfac=2.0,isr_G2GG_cNS_dn isr:G2GG:cNS=-2.0,isr_G2GG_cNS_up isr:G2GG:cNS=2.0,isr_G2QQ_cNS_dn isr:G2QQ:cNS=-2.0,isr_G2QQ_cNS_up isr:G2QQ:cNS=2.0,isr_Q2QG_cNS_dn isr:Q2QG:cNS=-2.0,isr_Q2QG_cNS_up isr:Q2QG:cNS=2.0,isr_X2XG_cNS_dn isr:X2XG:cNS=-2.0,isr_X2XG_cNS_up isr:X2XG:cNS=2.0}',
            'UncertaintyBands:nFlavQ = 4',
            'UncertaintyBands:MPIshowers = on',
            'UncertaintyBands:overSampleFSR = 10.0',
            'UncertaintyBands:overSampleISR = 10.0',
            'UncertaintyBands:FSRpTmin2Fac = 20',
            'UncertaintyBands:ISRpTmin2Fac = 1'
        )
    ),
    comEnergy = cms.double(13000.0),
    crossSection = cms.untracked.double(1),
    filterEfficiency = cms.untracked.double(1.0),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(0)
)


process.ProductionFilterSequence = cms.Sequence(process.generator)
# process.ProductionFilterSequence = cms.Sequence(process.generator + process.oniafilter)

# Path and EndPath definitions
# process.generation_step = cms.Path(process.pgen)
# process.generation_step = cms.Path(process.pgen  + process.genHToAATo4TauFilter)
process.generation_step = cms.Path(process.pgen  + process.genHToAATo4TauFilter)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)

process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.endjob_step,process.RAWSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path).insert(0, process.ProductionFilterSequence)

#do not add changes to your config after this point (unless you know what you are doing)
from FWCore.ParameterSet.Utilities import convertToUnscheduled
process=convertToUnscheduled(process)


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
