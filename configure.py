#!/usr/bin/env python3
import pandas as pd
import os
import subprocess
import shlex
import glob
import shutil

curr_dir = os.path.dirname(__file__)

# Read registery file
def read_registry():
    out_path = os.path.join(curr_dir, 'data')
    reg_file = os.path.join(curr_dir, 'registry.csv')
    reg_tab  = pd.read_csv(reg_file)
    paths    = reg_tab['path']
    ftypes   = reg_tab['type']

    # Make output dir
    shutil.rmtree(out_path, ignore_errors=True)
    os.mkdir(out_path)

    print('>> Processing registry.')
    # Iterate
    for indx_t, path_t in enumerate(paths):
        abs_path_t = os.path.join(curr_dir, path_t)
        if not os.path.isdir(abs_path_t):
            print('>> Path "{}" doesnot exit !!'.format(abs_path_t))
            continue
        # endif
        tgt_path_t = os.path.join(out_path, os.path.basename(os.path.normpath(path_t)) + '.' + ftypes[indx_t])
        cmd_str    = "cat {}/* > {}".format(abs_path_t, tgt_path_t)
        if ftypes[indx_t] in ['pkl']:
            print('>> {}'.format(cmd_str))
            subprocess.call(cmd_str, shell=True)
        else:
            print('>> Unsupported file type "{}" for path "{}" !!'.format(ftypes[indx_t], path_t))
        # endif
    # endfor
# enddef

if __name__ == '__main__':
    read_registry()
# endif
