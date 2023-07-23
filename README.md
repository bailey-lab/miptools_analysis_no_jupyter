# miptools_analysis_no_jupyter

This is a snakemake pipeline for running a modified analysis_template_with_qual
notebook (from miptools analysis). It consists of two parts:

 - check_run_stats: checks which samples and mips worked and at what levels
 - variant_calling: calls variants and generates output tables

Currently the first part (check_run_stats) needs to be run before the second
part (variant_calling) can be run, and the output folder of check_run_stats
needs to match the output folder of variant_calling.

check_run_stats eventually needs to output recapture/repooling info tables. This
should be an easy addition, but hasn't yet been implemented

## Installation

 - Install conda: https://github.com/conda-forge/miniforge#unix-like-platforms-mac-os--linux.
You'll need to follow the instructions to 'initialize' the conda environment at the end of the
installer, then sign out and back in again.
 - Create a conda environment and install snakemake there:
```bash
mamba create -c conda-forge -c bioconda -n snakemake snakemake
conda activate snakemake
```

### Setup your environment:
 - Change directory to a folder where you want to run the analysis
 - Download the files of this repository into that folder

## Usage:
 - Edit the singularity_profile/config.yaml file to point to your files. Use a text editor that outputs unix line endings (e.g. vscode, notepad++, gedit, micro, emacs, vim, vi, etc.)
 - Edit the variant_calling/variant_calling.yaml file to point to your files.
 - Edit the check_run_stats/check_run_stats.yaml file to point to your files.
 - If snakemake is not your active conda environment, activate snakemake with:
```bash
conda activate snakemake
```
 - Change directory to check_run_stats and run check_run_stats with:
```bash
snakemake -s check_run_stats.smk --profile ../singularity_profile
```
 - Change directory to variant_calling and run variant_calling with:
```bash
snakemake -s variant_calling.smk --profile ../singularity_profile
```
