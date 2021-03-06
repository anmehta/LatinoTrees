import os
from WMCore.Configuration import Configuration
config = Configuration()

pyCfgParams = ['outputFile=stepB_MC.root', 'doNoFilter=True', 'doMuonIsoId=True', 'doEleIsoId=True', 'doGen=True', 'doBTag=True', 'doLHE=False', 'runPUPPISequence=False']

config.section_('General')
config.General.transferLogs = True
config.General.workArea     = 'crab_projects_13May'  # Make sure you set this parameter


config.section_('JobType')
config.JobType.pluginName  = 'Analysis'
config.JobType.psetName    = '../stepB.py'
config.JobType.outputFiles = ['stepB_MC.root']
config.JobType.allowUndistributedCMSSW = True

config.section_('Data')    
config.Data.inputDBS      = 'global'
config.Data.splitting     = 'FileBased'
config.Data.unitsPerJob   = 1
config.Data.outLFNDirBase = '/store/group/phys_higgs/cmshww/amassiro/RunII/test/'

config.section_('Site')
config.Site.storageSite = 'T2_CH_CERN'


import sys

if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand

    def submit(config):
        print " to do: ",config
        res = crabCommand('submit', config = config)

    ######### From now on this is what users should modify. It is the a-la-CRAB2 configuration part.
   
    print sys.argv
    if len(sys.argv) <= 1 :
       print "no arguments?"
       print "Usage: python multicrab_template.py test.py"
       exit()
       

    samples = {}
    SamplesFile = sys.argv[1]
    print " SamplesFile = ", SamplesFile
    
    if os.path.exists(SamplesFile):
       handle = open(SamplesFile,'r')
       exec(handle)
       handle.close()
                
    # samples to be analysed
                   
    for key, value in samples.iteritems():
        print key, ' -> ', value
        
        config.General.requestName = key
        config.Data.inputDataset = value[0]
        config.JobType.pyCfgParams = list(pyCfgParams)
        config.JobType.pyCfgParams.extend(value[1])
        submit(config)

