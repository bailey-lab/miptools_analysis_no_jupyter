import sys
sys.path.append("/opt/src")
import mip_functions as mip
import probe_summary_generator
import pickle
import json
import copy
import os
import yaml
import numpy as np
import subprocess
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from matplotlib.lines import Line2D
plt.rcParams['svg.fonttype'] = 'none'
import pandas as pd
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
import allel
wdir = "/opt/analysis/"
data_dir = "/opt/data/"
yaml_file=f'{wdir}settings.yaml'


#all_together:
yaml_settings=yaml.safe_load(open(yaml_file))
print(yaml_settings)
info_files = yaml_settings['info_files']
sample_sheets = yaml_settings['sample_sheets']
sample_groups = yaml_settings['sample_groups']
species = yaml_settings['species']
probe_sets_used = yaml_settings['probe_sets_used']
processorNumber = yaml_settings['processorNumber']
minHaplotypeBarcodes = yaml_settings['minHaplotypeBarcodes']
minHaplotypeSamples = yaml_settings['minHaplotypeSamples']
minHaplotypeSampleFraction = yaml_settings['minHaplotypeSampleFraction']
barcode_threshold = yaml_settings['barcode_threshold']
tick_label_size = yaml_settings['tick_label_size']
cbar_label_size = yaml_settings['cbar_label_size']
dpi = yaml_settings['dpi']
absent_color = yaml_settings['absent_color']
present_color = yaml_settings['present_color']
save = yaml_settings['save']
ytick_freq = yaml_settings['ytick_freq']
xtick_freq = yaml_settings['xtick_freq']
xtick_rotation = yaml_settings['xtick_rotation']
high_barcode_threshold = yaml_settings['high_barcode_threshold']
low_coverage_action = yaml_settings['low_coverage_action']
target_coverage_count = yaml_settings['target_coverage_count']
target_coverage_fraction = yaml_settings['target_coverage_fraction']
target_coverage_key = yaml_settings['target_coverage_key']
barcode_coverage_threshold = yaml_settings['barcode_coverage_threshold']
barcode_count_threshold = yaml_settings['barcode_count_threshold']
assesment_key = yaml_settings['assesment_key']
good_coverage_quantile = yaml_settings['good_coverage_quantile']
options = yaml_settings['options']
align = yaml_settings['align']
verbose = yaml_settings['verbose']
fastq_dir = yaml_settings['fastq_dir']
bam_dir = yaml_settings['bam_dir']
vcf_file = yaml_settings['vcf_file']
targets_file = yaml_settings['targets_file']
errors_file = yaml_settings['errors_file']
warnings_file = yaml_settings['warnings_file']
fastq_padding = yaml_settings['fastq_padding']
geneid_to_genename = yaml_settings['geneid_to_genename']
target_aa_annotation = yaml_settings['target_aa_annotation']
aggregate_aminoacids = yaml_settings['aggregate_aminoacids']
aggregate_nucleotides = yaml_settings['aggregate_nucleotides']
target_nt_annotation = yaml_settings['target_nt_annotation']
settings_file = yaml_settings['settings_file']
annotate = yaml_settings['annotate']
decompose_options = yaml_settings['decompose_options']
annotated_vcf = yaml_settings['annotated_vcf']
aggregate_none = yaml_settings['aggregate_none']
min_site_qual = yaml_settings['min_site_qual']
min_target_site_qual = yaml_settings['min_target_site_qual']
min_genotype_qual = yaml_settings['min_genotype_qual']
min_mean_alt_qual = yaml_settings['min_mean_alt_qual']
output_prefix = yaml_settings['output_prefix']
mutation_count_file = yaml_settings['mutation_count_file']
mutation_coverage_file = yaml_settings['mutation_coverage_file']
min_count = yaml_settings['min_count']
min_coverage = yaml_settings['min_coverage']
min_freq = yaml_settings['min_freq']
num_samples_wsaf = yaml_settings['num_samples_wsaf']
min_wsaf = yaml_settings['min_wsaf']
num_samples_umi = yaml_settings['num_samples_umi']
min_umi = yaml_settings['min_umi']

# No input below - *****this code should probably be deleted - it assumes unmerged sample sheets and would result in incorrectly merged samples sheets (counts associated with same UMI double counted).
info_files = [data_dir + i for i in info_files]
sample_sheets = [data_dir + s for s in sample_sheets]
pd.concat([pd.read_table(s) for s in sample_sheets],
         ignore_index=True).groupby(["sample_set", "probe_set"]).first()

## extra bwa options for haplotype alignment
# use "-a" for getting all alignments
# use "-L 500" to penalize soft clipping 
# use "-t" to set number of available processors
bwaExtra = ["-t", str(processorNumber)]

# RUN

# copy the template settings file
temp_settings_file = "/opt/resources/templates/analysis_settings_templates/settings.txt"
subprocess.call(["scp", temp_settings_file, "/opt/analysis/template_settings.txt"])

# extract the settings template
temp_settings = mip.get_analysis_settings("/opt/analysis/template_settings.txt")

# update bwa settings with the options set above
bwaOptions = temp_settings["bwaOptions"]
try:
    bwaOptions.extend(bwaExtra)
except AttributeError:
    bwaOptions = [bwaOptions]
    bwaOptions.extend(bwaExtra)

# Create a list from the probe_sets string
mipSetKey = probe_sets_used.split(",") + [""]

# create a dictionary for which settings should be updated
# using the user specified parameters.
update_keys = {"processorNumber": processorNumber,
               "bwaOptions": bwaOptions,
               "species": species,
               "mipSetKey" : mipSetKey}
# update the settings
for k, v in update_keys.items():
    temp_settings[k] = v
# create a settings file in the analysis directory.
settings_file = "settings.txt"
settings_path = os.path.join(wdir, settings_file)
mip.write_analysis_settings(temp_settings, settings_path)
settings = mip.get_analysis_settings(wdir + settings_file)
# create probe sets dictionary
try:
    mip.update_probe_sets("/opt/project_resources/mip_ids/mipsets.csv",
                         "/opt/project_resources/mip_ids/probe_sets.json")
except IOError:
    pass





# RUN - ***** again, this code should be deleted - sample sheets should be merged prior to wrangling
if len(info_files) > 1:
    mip.combine_info_files(wdir,
                           settings_file, 
                           info_files,
                           sample_sheets,
                           settings["mipsterFile"],
                           sample_sets=sample_groups)
else:
    mip.process_info_file(wdir,
                          settings_file, 
                          info_files,
                          sample_sheets,
                          settings["mipsterFile"],
                          sample_sets=sample_groups)





# OPTIONAL USER INPUT
# filter haplotype sequences based on the number of total supporting UMIs
settings["minHaplotypeBarcodes"] = minHaplotypeBarcodes
# filter haplotype sequences based on the number of samples they were observed in
settings["minHaplotypeSamples"] = minHaplotypeSamples
# filter haplotype sequences based on the fraction of samples they were observed in
settings["minHaplotypeSampleFraction"] = minHaplotypeSampleFraction

# ***** - there needs to be a statement here that writes these updated settings
#to the new location. e.g. mip.write_analysis_settings(settings, settings_path)


#RUN
mip.map_haplotypes(settings)
mip.get_haplotype_counts(settings)

#***** - I think some output files will be generated by this step. These output
#files should be explicitly stated here so that users know which steps generate
#which outputs. Ideally, these steps would be replaced by snakemake rules.





# OPTIONAL USER INPUT
barcode_counts = pd.read_csv(wdir + "barcode_counts.csv",
            header = [0,1], index_col = 0)
mip.plot_performance(barcode_counts,
                     barcode_threshold=barcode_threshold,
                     tick_label_size=tick_label_size,
                     cbar_label_size=cbar_label_size,
                     dpi=dpi,
                     absent_color=absent_color,
                     present_color=present_color,
                     save=save,
                     ytick_freq=ytick_freq,
                     xtick_freq=xtick_freq,
                     xtick_rotation=xtick_rotation)
# ***** - this plotting script could be replaced with plotly



# RUN - ***** - can delete, this won't do anything in a non-interactive script
#or could change to print statements or output files.
sample_summary = pd.read_csv(wdir + "sample_summary.csv")
sample_summary.head()





# RUN - ***** - this needs to be redone as a plotly graph
f = sns.pairplot(data = sample_summary,
                x_vars = "Barcode Count",
                y_vars = "targets_with_10_barcodes",
                plot_kws={"s": 10})
f.fig.set_size_inches(5,5)
f.fig.set_dpi(150)
_ = plt.xticks(rotation=45)





# RUN
meta = pd.read_csv(wdir + "run_meta.csv")
data_summary = pd.merge(sample_summary, meta)
mip.repool(wdir, 
           data_summary, 
           high_barcode_threshold, 
           target_coverage_count=target_coverage_count, 
           target_coverage_fraction=target_coverage_fraction, 
           target_coverage_key=target_coverage_key,
           barcode_coverage_threshold=barcode_coverage_threshold,
           barcode_count_threshold=barcode_count_threshold, 
           low_coverage_action=low_coverage_action,
           assesment_key=assesment_key,
           good_coverage_quantile=good_coverage_quantile,
           output_file='repool.csv')





# RUN
pd.read_csv(wdir + "repool.csv").head()



# OPTIONAL USER INPUT

# freebayes caller creates fastq files from the haplotype sequences
# by default 20 bp flanking sequence from the reference genome is added
# to ensure correct deletion calls when they are towards the ends.
# This assumes the 20 bp flank is wild type, however the sequence
# is given a quality of 1, which should help avoiding some issues.
# If this is not desired, set the below parameter to 0
fastq_padding = 20

# RUN
r = mip.freebayes_call(
        settings=settings,
        options=options,
        align=align,
        verbose=verbose,
        fastq_dir=fastq_dir,
        bam_dir=bam_dir,
        vcf_file=vcf_file,
        targets_file=targets_file,
        bam_files=None,
        errors_file=errors_file,
        warnings_file=warnings_file,
        fastq_padding=fastq_padding)





# RUN

# input vcf file
vcf_file = vcf_file.split("/")[-1]
mip.vcf_to_tables_fb(
     vcf_file,
     settings=settings,
     settings_file=settings_file,
     annotate=annotate,
     geneid_to_genename=geneid_to_genename,
     target_aa_annotation=target_aa_annotation,
     aggregate_aminoacids=aggregate_aminoacids,
     target_nt_annotation=target_nt_annotation, 
     aggregate_nucleotides=aggregate_nucleotides, 
     decompose_options=decompose_options,
     annotated_vcf=annotated_vcf,
     aggregate_none=aggregate_none,
     min_site_qual=min_site_qual,
     min_target_site_qual=min_target_site_qual,
     min_genotype_qual=min_genotype_qual,
     min_mean_alt_qual=min_mean_alt_qual,
     output_prefix=output_prefix)





mutation_counts = pd.read_csv(mutation_count_file,
                              header=list(range(6)),
                              index_col=0)
mutation_counts.head()





# RUN
mutation_coverage = pd.read_csv(mutation_coverage_file,
                                index_col=0,
                                header=list(range(6)))
mutation_coverage.head()





# RUN

# import the PCA module which has genotype calling and
# filtering functions 
import PCA

gt_calls = PCA.call_genotypes(mutation_counts, mutation_coverage,
                              min_count, min_coverage, min_freq)
gt_calls.keys()





# RUN
filtered_mutation_counts = gt_calls["filtered_mutation_counts"]
filtered_mutation_counts.head()





# RUN
filtered_mutation_coverage = gt_calls["filtered_mutation_coverage"]
filtered_mutation_coverage.head()





# RUN
freq = gt_calls["wsaf"]
freq.head()





# RUN
genotypes = gt_calls["genotypes"]
genotypes.head()





# RUN
prevalences = gt_calls["prevalences"]
prevalences.head()





wsaf_filter = ((freq > min_wsaf).sum()) >= num_samples_wsaf
print(("{} of {} variants will remain after the wsaf filter").format(
    wsaf_filter.sum(), freq.shape[1]))





# RUN
umi_filter = ((filtered_mutation_counts >= min_umi).sum()) > num_samples_umi
print(("{} of {} variants will remain after the UMI filter").format(
    umi_filter.sum(), freq.shape[1]))





# RUN
targ = freq.columns.get_level_values("Targeted") == "Yes"





variant_mask = targ | (wsaf_filter & umi_filter)
print(("{} variants will remain in the final call set.\n"
       "{} variants were targeted and will be kept; and {} will be removed by "
       "the combined UMI and WSAF filters.").format(
    variant_mask.sum(), targ.sum(), (wsaf_filter & umi_filter).sum()))





filtered_genotypes = genotypes.loc[:, variant_mask]
filtered_genotypes.head()





filtered_prevalences = prevalences.loc[:, variant_mask]
filtered_prevalences.head()
