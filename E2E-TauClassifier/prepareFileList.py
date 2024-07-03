import os
import sys
inputDirList = ['/eos/uscms/store/group/lpcml/rchudasa/MCGeneration/TTToHadronic_TuneCP5_13TeV_powheg-pythia8/crab_TTToHadronic_TuneCP5_13TeV_powheg-pythia8_GEN-SIM/240620_192204/0000/','/eos/uscms/store/group/lpcml/rchudasa/MCGeneration/TTToHadronic_TuneCP5_13TeV_powheg-pythia8/crab_TTToHadronic_TuneCP5_13TeV_powheg-pythia8_GEN-SIM/240620_192204/0001/']

#inputDirList =['/eos/uscms/store/group/lpcml/rchudasa/MCGeneration/DYToTauTau_M-50_13TeV-powheg_pythia8/crab_DYToTauTau_M-50_13TeV-powheg_pythia8_GEN-SIM/230227_114053/0000/','/eos/uscms/store/group/lpcml/rchudasa/MCGeneration/DYToTauTau_M-50_13TeV-powheg_pythia8/crab_DYToTauTau_M-50_13TeV-powheg_pythia8_GEN-SIM/230227_114053/0001/','/eos/uscms/store/group/lpcml/rchudasa/MCGeneration/DYToTauTau_M-50_13TeV-powheg_pythia8/crab_DYToTauTau_M-50_13TeV-powheg_pythia8_GEN-SIM/240620_193248/0000/','/eos/uscms/store/group/lpcml/rchudasa/MCGeneration/DYToTauTau_M-50_13TeV-powheg_pythia8/crab_DYToTauTau_M-50_13TeV-powheg_pythia8_GEN-SIM/240620_193248/0001/','/eos/uscms/store/group/lpcml/rchudasa/MCGeneration/DYToTauTau_M-50_13TeV-powheg_pythia8/crab_DYToTauTau_M-50_13TeV-powheg_pythia8_GEN-SIM/240620_193248/0002/']

#i#inputDir ='/eos/uscms/store/group/lpcml/rchudasa/MCGeneration/DYToTauTau_M-50_13TeV-powheg_pythia8/crab_DYToTauTau_M-50_13TeV-powheg_pythia8_GEN-SIM/230227_114053/0000/'
#inputDir2 ='/eos/uscms/store/group/lpcml/rchudasa/MCGeneration/DYToTauTau_M-50_13TeV-powheg_pythia8/crab_DYToTauTau_M-50_13TeV-powheg_pythia8_GEN-SIM/230227_114053/0001/'
#inputDir3 ='/eos/uscms/store/group/lpcml/rchudasa/MCGeneration/DYToTauTau_M-50_13TeV-powheg_pythia8/crab_DYToTauTau_M-50_13TeV-powheg_pythia8_GEN-SIM/240620_193248/0000/'
#inputDir4 ='/eos/uscms/store/group/lpcml/rchudasa/MCGeneration/DYToTauTau_M-50_13TeV-powheg_pythia8/crab_DYToTauTau_M-50_13TeV-powheg_pythia8_GEN-SIM/240620_193248/0001/'
#inputDir5 ='/eos/uscms/store/group/lpcml/rchudasa/MCGeneration/DYToTauTau_M-50_13TeV-powheg_pythia8/crab_DYToTauTau_M-50_13TeV-powheg_pythia8_GEN-SIM/240620_193248/0002/'
#inputDir ='/eos/uscms/store/group/lpcml/rchudasa/MCGeneration/QCD_Pt-15to7000_TuneCP5_Flat_13TeV_pythia8/crab_QCD_Pt-15to7000_TuneCP5_13TeV_Flast_pythia8_GEN-SIM/230208_100328/0000/'

#fileName='DYToTauTau_M-50_13TeV-powheg_pythia8_GEN-SIM.txt'
fileName='TTToHadronic_TuneCP5_13TeV_powheg-pythia8_GEN-SIM.txt'
for i in inputDirList:
    filtered_files = [file for file in os.listdir(i) if file.endswith('root')]
    split_prefix = i.split('/')[3:-1]
    prefix = "/".join(split_prefix)
    print(i)
    print(prefix)
    lines = ["/"+prefix+"/"+file+'\n' for file in filtered_files]

    if os.path.exists(fileName):
        with open(fileName, 'a') as f: 
            f.writelines(lines)
    else:
        with open(fileName, 'w') as f:
            f.writelines(lines)

'''
all_files = os.listdir(inputDir)+os.listdir(inputDir2)+os.listdir(inputDir3)+os.listdir(inputDir4)+os.listdir(inputDir5)

print("Len of files:", len(all_files))

filtered_files = [file for file in all_files if file.endswith('root')]

split_string = inputDir.split('/')[3:-1]
print("/".join(split_string))

prefix = '/store/group/lpcml/rchudasa/MCGeneration/DYToTauTau_M-50_13TeV-powheg_pythia8/crab_DYToTauTau_M-50_13TeV-powheg_pythia8_GEN-SIM/230227_114053/0000'

print(prefix)
lines = [prefix+file+'\n' for file in filtered_files]

fileName='DYToTauTau_M-50_13TeV-powheg_pythia8_GEN-SIM.txt'
#fileName='QCD_Pt-15to7000_TuneCP5_Flat.txt'

#with open(fileName, 'w') as file:
#    file.writelines(lines)
'''
