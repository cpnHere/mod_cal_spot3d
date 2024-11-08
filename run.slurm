#!/bin/bash

#SBATCH --job-name=MOD-CAL-629
#SBATCH --output=slurm-MOD-CAL-6m-%J.out
#SBATCH --partition=cpu2021
#SBATCH --qos=medium
#SBATCH --mem=32000
#SBATCH --time=24:00:00

echo ${job} $HOSTNAME
python spot_MODIS_3Deffects.py 1 31
