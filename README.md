ml_data
--------------------------
This repository contains huge data for machine learning experiments, which may be otherwise difficult or time consuming to obtain on the fly.
Since, github only supports binary files of size <100 MB, we have to split large binary files into smaller chunks to commit to the repository.

Each dataset has a corresponding entry in the registry file (registry.csv) and the file type of the corresponding output file. The configuration script (configure.py) needs to know both to sucessfully generate the final data from it's chunks.
