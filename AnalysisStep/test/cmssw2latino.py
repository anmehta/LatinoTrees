#!/bin/env python
import os
import ROOT
import sys
import optparse
import pdb

# transform the root file tree structure to have a simple "latino" one

def probe2latino(chans,ifile,ofile):

  ROOT.gROOT.cd()
  latino = ROOT.TChain('probe_tree')
  for chan in chans:
    tree2add = ifile+'/'+chan+'Tree/probe_tree'
    latino.Add(tree2add)
    print ' - ',latino.GetEntries(),tree2add

  latino.SetName('latino')
  latino.SetTitle('latino')
  latino.Merge(ofile)
  latino.SetDirectory(0x0)

from optparse import OptionParser
usage='''
 %prog

 Converts step3 trees into standard latino files

'''

parser = OptionParser(usage=usage)
parser.add_option('-d', dest='odir', help='output directory')

(opts, args) = parser.parse_args()


filenames = args
odir=''


chans=['']

if opts.odir:
    odir = opts.odir
    os.system('mkdir -p '+odir)

for f in filenames:
    ofile = os.path.join(odir,'latino_'+os.path.basename(f).replace('tree_',''))

    print ofile

    probe2latino(chans,f,ofile)

print '...and done'
