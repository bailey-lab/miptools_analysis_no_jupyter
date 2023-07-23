# miptools_analysis_no_jupyter

This is a snakemake pipeline for running a modified analysis_template_with_qual
notebook (from miptools analysis). It consists of two parts:

 - check_run_stats: checks which samples and mips worked and at what levels
 - variant_calling: calls variants and generates output tables

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
 - Edit the  file using the instructions in the comments. Use a text editor that outputs unix line endings (e.g. vscode, notepad++, gedit, micro, emacs, vim, vi, etc.)
 - If snakemake is not your active conda environment, activate snakemake with:
```bash
conda activate snakemake
```
 - Run snakemake with:
```bash
snakemake -s wrangle_data.smk --cores [your_desired_core_count]

## Not Implemented yet

check_run_stats eventually needs to output recapture/repooling info tables. This
should be an easy addition, but hasn't yet been implemented.
