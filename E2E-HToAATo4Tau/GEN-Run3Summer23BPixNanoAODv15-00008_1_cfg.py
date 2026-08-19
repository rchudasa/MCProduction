# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: --eventcontent NANOEDMAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier NANOAODSIM --conditions 150X_mcRun3_2023_realistic_postBPix_v1 --step NANO --era Run3_2023,run3_nanoAOD_pre142X --python_filename GEN-Run3Summer23BPixNanoAODv15-00008_1_cfg.py --fileout file:GEN-Run3Summer23BPixNanoAODv15-00008.root --filein dbs:/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4-130X_mcRun3_2023_realistic_postBPix_v2-v3/MINIAODSIM --number 1763 --number_out 1763 --no_exec --mc
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_2023_cff import Run3_2023
from Configuration.Eras.Modifier_run3_nanoAOD_pre142X_cff import run3_nanoAOD_pre142X

process = cms.Process('NANO',Run3_2023,run3_nanoAOD_pre142X)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('PhysicsTools.NanoAOD.nano_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1763),
    output = cms.untracked.int32(1763)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/07c16fbb-6b0a-4ca0-a5eb-6092a975cb30.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/09b19128-716a-4770-83b4-88d80e1abb02.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/0d79ad17-1c61-424e-91f8-4017fd49727d.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/0e5e69d3-0369-4043-8ad6-b228010483cc.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/1022aea9-3234-421d-81f1-0204a9c8bcac.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/10a50733-877a-470e-80e0-260985f432af.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/1328984d-2f68-4beb-b5a4-6b4c69563f03.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/14dc6fa5-7dba-4a07-8b45-a6f905e7dd0c.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/150904eb-db90-495a-8e9b-4d00586f4f60.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/185a391e-9c2e-4886-9f36-c16653030489.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/1916f882-7076-4e08-8c3f-486b99242f12.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/195be649-36d4-43bb-8f78-d33db66ce4bb.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/1ae80a19-3164-4929-8f7b-eb63cd535d7e.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/1d404247-326a-4710-9e2e-0bf9bf466ed4.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/1dd82f8a-239c-4d4a-99a5-6e9159b9613c.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/1eed521a-8f8e-4b91-99cf-69c65b318376.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/22ae2c19-1016-43ba-900d-1bf6e0212f19.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/231eb254-c618-462d-b005-c203557f37c9.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/264da17b-6240-495f-bd80-08cf9ea9901a.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/271ddc2e-15ca-4594-9368-fd20e6b21f30.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/295fdce6-0928-4431-8a1f-d177941ce00f.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/29c36a54-6871-41a5-afc3-db92598b802a.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/2fb78d41-0184-43f9-9cce-cf94e7675bca.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/30e6cad8-6be5-4e63-bc7a-0f93bba9464f.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/325b9515-9a08-4dae-a4b1-7c216fec9963.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/332c8605-7a20-4904-b3e3-22fe29fbb6f6.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/35a28451-cd57-4359-9ba2-3e7ddfd8ec44.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/36af6490-116c-49f5-b83e-587346fe9af6.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/371ea9f0-f23f-41a7-9f94-5827b1e3efec.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/37caab80-116f-4879-b421-2ca36d330bd4.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/3d4f5e71-de9e-4f62-b82d-340ed2033c9f.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/3eb12b72-89f3-4d2a-a5bc-356c2875f624.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/3eccf791-4bf0-4a76-a3d2-6bf2d7462cea.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/4735c151-ce84-4c18-8c95-4b40c408a9f4.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/495fe8f0-96c4-4d6e-9757-ad3b5c51979f.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/4a2d8b3a-9bc9-470f-9096-4a28bdb4520a.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/53d89eb0-9114-4f4f-a3a6-00179a25ebc2.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/567f26f9-2c22-4213-868a-b342b4be33a9.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/57bd222e-9887-4053-bc2b-d3aad725400b.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/58f0997e-0e28-4a5e-b1d6-541830480667.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/5abe0db1-8286-4382-a58e-99d2c8aa05a7.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/5bf6fa7f-16a1-4594-a99a-4d436ec298cd.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/5dda841a-901b-468e-a1b3-ce4821d6986f.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/6273beb5-5103-4a17-b808-05023373c1e4.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/636a22b4-4eed-4e14-b288-010e51a158d4.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/6493f369-2857-4680-9900-918420efd4b6.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/682d5cb8-26ec-45b3-a1ca-c41fbd49a938.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/70f242c6-eae0-4cdb-bffe-74797c593503.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/7160b1fb-9026-4485-95cc-51bcfad72fbe.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/71f88cfb-bfcd-430f-9f27-008ff3e0ebe5.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/7260af11-6aea-4d23-bdf0-360fccf6f00e.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/7530e7b8-729f-4a15-bfb0-ffd8af630682.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/7aa85b85-8eb7-465d-bca8-c654ae01c2e9.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/7eef8110-837b-4c08-af49-10d551c99d1f.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/80498932-4ab5-4b8e-a45e-5ed3569867e0.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/81481b9c-24cc-4a55-8a22-df0a3c317512.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/85a214fa-8649-463a-8397-2bb0baaf8d9b.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/8891b9a1-fb42-495b-9c28-9d2a5c838b3f.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/90171005-9a78-46a4-b38b-d03e1ee12b52.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/908c1472-65e3-4648-ae7b-11f24615602f.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/9194888c-32c2-4f71-a13b-060da4e0d50e.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/970799b7-6b5f-4c2c-b54a-7c1f361ff438.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/97ec48fe-9628-4d66-897e-f08a08c8d43c.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/986c608c-c035-48cc-a4a9-fa1f050e44fb.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/99be741a-fb21-4f35-9f5b-b581fa37907c.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/9a56075a-8fbe-4c74-bb77-bfb80caa3f37.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/9bb49a7d-917d-47d9-bce4-4bb0d73be1a8.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/a575ffd5-414a-4325-876a-bad7d5798893.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/a5e64e34-d0aa-4264-a683-9560d7aeb632.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/a6f1b2b0-5249-42d4-ac34-c4caef2cdd6f.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/a9fd3a24-9d76-4d3f-a222-e2545b4b8e16.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/ab6d6344-9e87-4c40-a4b8-096e534c1d0c.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/ac340fef-6f1f-4023-b8c0-9bd4966e977b.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/adbee747-62a0-4f30-aa64-a7f333753db8.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/adf5608c-0cdc-4b75-af35-129a0613b836.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/ae978e65-ed13-4ffe-806e-850871b7f64f.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/b2dbda35-cfb8-4887-a5ba-bf9521872b74.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/b730e0ca-8eca-4dc0-b331-0715b5816b96.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/b7d41696-ae9f-43d1-ae8a-8efdbac7c650.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/bbfde31e-1d5e-4470-835b-68c670cedab7.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/bdb222c7-fafe-44ea-830c-4709dd19c093.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/c444a494-58f1-4983-a78f-8438ec5877b7.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/c7d1cac3-06de-4392-a59f-958b03a58be2.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/ca0eb8f6-91c9-43a1-979b-67f16431593a.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/cd34afee-ce86-408f-9720-5b7c5134ff60.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/ceabdfda-a7b7-437a-a4a1-6519b0be77d5.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/d12b3735-755c-446b-96c1-ae5ad2f70bbf.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/d23afb22-76d6-4b76-95a7-4bf8a5377bec.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/d27600b5-1f50-45dd-b286-5c0479610098.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/d48ba813-72c7-41b7-8cf5-a040d42b7d4c.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/d4b78846-0bf1-4dad-97c9-cabf4958048f.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/d7e32d7b-292e-42bc-907e-7304d8db2b49.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/dedf0ce7-46f7-4b65-9a80-3e5bf19ae416.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/e03aa20d-f269-415f-97d2-27145c4d018b.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/e58378a4-faa0-41f5-92de-f45d3a6ff37b.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/e6839be8-ec27-4e25-a066-09521d4787c5.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/eb51b192-143a-43f9-b4d9-d3b102c3eb78.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/ecea5c1d-c80e-480f-b16a-1a4f2387c730.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/f0806350-2f89-4047-bce1-8e7a1a45466e.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/f23155cf-29ad-48c6-beaf-3c0703e037f5.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/fa42cdf0-2e67-4adc-a374-6f3becfaa18a.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/fd074464-f9a3-4c8d-9e36-b6584de8cce0.root',
        '/store/mc/Run3Summer23BPixMiniAODv4/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/40000/fee4c4b7-098c-434c-a61e-15e95303da69.root'
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    TryToContinue = cms.untracked.vstring(),
    accelerators = cms.untracked.vstring('*'),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    holdsReferencesToDeleteEarly = cms.untracked.VPSet(),
    makeTriggerResults = cms.obsolete.untracked.bool,
    modulesToCallForTryToContinue = cms.untracked.vstring(),
    modulesToIgnoreForDeleteEarly = cms.untracked.vstring(),
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('--eventcontent nevts:1763'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.NANOEDMAODSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('NANOAODSIM'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:GEN-Run3Summer23BPixNanoAODv15-00008.root'),
    outputCommands = process.NANOAODSIMEventContent.outputCommands
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '150X_mcRun3_2023_realistic_postBPix_v1', '')

# Path and EndPath definitions
process.nanoAOD_step = cms.Path(process.nanoSequenceMC)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.NANOEDMAODSIMoutput_step = cms.EndPath(process.NANOEDMAODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.nanoAOD_step,process.endjob_step,process.NANOEDMAODSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# Automatic addition of the customisation function from PhysicsTools.NanoAOD.nano_cff
from PhysicsTools.NanoAOD.nano_cff import nanoAOD_customizeCommon 

#call to customisation function nanoAOD_customizeCommon imported from PhysicsTools.NanoAOD.nano_cff
process = nanoAOD_customizeCommon(process)

# End of customisation functions


# Customisation from command line

process.source.delayReadingEventProducts = cms.untracked.bool(False)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
