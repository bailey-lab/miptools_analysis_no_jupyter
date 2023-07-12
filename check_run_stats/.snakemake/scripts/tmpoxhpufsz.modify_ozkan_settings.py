
######## snakemake preamble start (automatically inserted, do not edit) ########
import sys; sys.path.extend(['/mnt/snakemake', '/users/asimkin/.cache/snakemake/snakemake/source-cache/runtime-cache/tmpitthjgi2/file/nfs/jbailey5/baileyweb/asimkin/github_pipelines/miptools_analysis_no_jupyter/check_run_stats/scripts', '/nfs/jbailey5/baileyweb/asimkin/github_pipelines/miptools_analysis_no_jupyter/check_run_stats/scripts']); import pickle; snakemake = pickle.loads(b'\x80\x04\x95C\t\x00\x00\x00\x00\x00\x00\x8c\x10snakemake.script\x94\x8c\tSnakemake\x94\x93\x94)\x81\x94}\x94(\x8c\x05input\x94\x8c\x0csnakemake.io\x94\x8c\nInputFiles\x94\x93\x94)\x81\x94}\x94(\x8c\x06_names\x94}\x94\x8c\x12_allowed_overrides\x94]\x94(\x8c\x05index\x94\x8c\x04sort\x94eh\x0f\x8c\tfunctools\x94\x8c\x07partial\x94\x93\x94h\x06\x8c\x19Namedlist._used_attribute\x94\x93\x94\x85\x94R\x94(h\x15)}\x94\x8c\x05_name\x94h\x0fsNt\x94bh\x10h\x13h\x15\x85\x94R\x94(h\x15)}\x94h\x19h\x10sNt\x94bub\x8c\x06output\x94h\x06\x8c\x0bOutputFiles\x94\x93\x94)\x81\x94\x8ci/nfs/jbailey5/baileyweb/asimkin/miptools/Mikalayi_TES/whole_dataset_wrangled/variant_calling/settings.txt\x94a}\x94(h\x0b}\x94\x8c\ruser_settings\x94K\x00N\x86\x94sh\r]\x94(h\x0fh\x10eh\x0fh\x13h\x15\x85\x94R\x94(h\x15)}\x94h\x19h\x0fsNt\x94bh\x10h\x13h\x15\x85\x94R\x94(h\x15)}\x94h\x19h\x10sNt\x94bh&h#ub\x8c\x06params\x94h\x06\x8c\x06Params\x94\x93\x94)\x81\x94(\x8cA/opt/resources/templates/analysis_settings_templates/settings.txt\x94K\x10]\x94(\x8c\x02-t\x94\x8c\x0216\x94e\x8c\x02pf\x94]\x94\x8c\x03IBC\x94aK\x01K\x01G?\x1a6\xe2\xeb\x1cC-\x8c\r/opt/analysis\x94e}\x94(h\x0b}\x94(\x8c\x11template_settings\x94K\x00N\x86\x94\x8c\x10processor_number\x94K\x01N\x86\x94\x8c\tbwa_extra\x94K\x02N\x86\x94\x8c\x07species\x94K\x03N\x86\x94\x8c\x0fprobe_sets_used\x94K\x04N\x86\x94\x8c\x16min_haplotype_barcodes\x94K\x05N\x86\x94\x8c\x15min_haplotype_samples\x94K\x06N\x86\x94\x8c\x1dmin_haplotype_sample_fraction\x94K\x07N\x86\x94\x8c\x04wdir\x94K\x08N\x86\x94uh\r]\x94(h\x0fh\x10eh\x0fh\x13h\x15\x85\x94R\x94(h\x15)}\x94h\x19h\x0fsNt\x94bh\x10h\x13h\x15\x85\x94R\x94(h\x15)}\x94h\x19h\x10sNt\x94bh?h5hAK\x10hCh6hEh9hGh:hIK\x01hKK\x01hMG?\x1a6\xe2\xeb\x1cC-hOh<ub\x8c\twildcards\x94h\x06\x8c\tWildcards\x94\x93\x94)\x81\x94}\x94(h\x0b}\x94h\r]\x94(h\x0fh\x10eh\x0fh\x13h\x15\x85\x94R\x94(h\x15)}\x94h\x19h\x0fsNt\x94bh\x10h\x13h\x15\x85\x94R\x94(h\x15)}\x94h\x19h\x10sNt\x94bub\x8c\x07threads\x94K\x01\x8c\tresources\x94h\x06\x8c\tResources\x94\x93\x94)\x81\x94(K\x01K\x01M\xa0\x0fM\xe7\x0eM\xe8\x03M\xba\x03\x8c\x04/tmp\x94K\x01Kx\x8cy/nfs/jbailey5/baileyweb/asimkin/miptools/Mikalayi_TES/whole_dataset_wrangled/variant_calling/run_settings/check_run_stats\x94e}\x94(h\x0b}\x94(\x8c\x06_cores\x94K\x00N\x86\x94\x8c\x06_nodes\x94K\x01N\x86\x94\x8c\x06mem_mb\x94K\x02N\x86\x94\x8c\x07mem_mib\x94K\x03N\x86\x94\x8c\x07disk_mb\x94K\x04N\x86\x94\x8c\x08disk_mib\x94K\x05N\x86\x94\x8c\x06tmpdir\x94K\x06N\x86\x94\x8c\x05nodes\x94K\x07N\x86\x94\x8c\x08time_min\x94K\x08N\x86\x94\x8c\x07log_dir\x94K\tN\x86\x94uh\r]\x94(h\x0fh\x10eh\x0fh\x13h\x15\x85\x94R\x94(h\x15)}\x94h\x19h\x0fsNt\x94bh\x10h\x13h\x15\x85\x94R\x94(h\x15)}\x94h\x19h\x10sNt\x94bhrK\x01htK\x01hvM\xa0\x0fhxM\xe7\x0ehzM\xe8\x03h|M\xba\x03h~hn\x8c\x05nodes\x94K\x01\x8c\x08time_min\x94Kx\x8c\x07log_dir\x94houb\x8c\x03log\x94h\x06\x8c\x03Log\x94\x93\x94)\x81\x94}\x94(h\x0b}\x94h\r]\x94(h\x0fh\x10eh\x0fh\x13h\x15\x85\x94R\x94(h\x15)}\x94h\x19h\x0fsNt\x94bh\x10h\x13h\x15\x85\x94R\x94(h\x15)}\x94h\x19h\x10sNt\x94bub\x8c\x06config\x94}\x94(\x8c\routput_folder\x94\x8c\\/nfs/jbailey5/baileyweb/asimkin/miptools/Mikalayi_TES/whole_dataset_wrangled/variant_calling\x94\x8c\x08sif_file\x94\x8cN/nfs/jbailey5/baileyweb/asimkin/miptools/miptools_tutorial/miptools_v0.4.0.sif\x94\x8c\x10processor_number\x94K\x10\x8c\tbwa_extra\x94]\x94(h7h8e\x8c\x07species\x94h9\x8c\x0fprobe_sets_used\x94]\x94h;a\x8c\rsample_groups\x94]\x94]\x94(\x8c\x03JJJ\x94\x8c\x15DR2,HAPDR,HEOME96,IBC\x94ea\x8c\rsample_sheets\x94]\x94\x8c*/opt/data/mikalayi_merged_sample_sheet.tsv\x94a\x8c\ninfo_files\x94]\x94\x8c6/opt/data/allInfo_shrunknames_filtered_samples.tab.txt\x94a\x8c\x16min_haplotype_barcodes\x94K\x01\x8c\x15min_haplotype_samples\x94K\x01\x8c\x1dmin_haplotype_sample_fraction\x94G?\x1a6\xe2\xeb\x1cC-u\x8c\x04rule\x94\x8c\x15modify_ozkan_settings\x94\x8c\x0fbench_iteration\x94N\x8c\tscriptdir\x94\x8ce/nfs/jbailey5/baileyweb/asimkin/github_pipelines/miptools_analysis_no_jupyter/check_run_stats/scripts\x94ub.'); from snakemake.logging import logger; logger.printshellcmds = True; __real_file__ = __file__; __file__ = '/nfs/jbailey5/baileyweb/asimkin/github_pipelines/miptools_analysis_no_jupyter/check_run_stats/scripts/modify_ozkan_settings.py';
######## snakemake preamble end #########
'''
The code this function depends on could probably be significantly streamlined by
reading and writing settings file dictionaries with yaml instead of Ozkan's
custom functions.
Also, not sure why mipSetKey needs an empty entry added on to the existing list.
'''
import sys
sys.path.append("/opt/src")
import subprocess
import mip_functions as mip

temp_settings_file = snakemake.params['template_settings']
processor_number=snakemake.params['processor_number']
bwa_extra=snakemake.params['bwa_extra']
species=snakemake.params['species']
probe_sets_used=snakemake.params['probe_sets_used']
wdir=snakemake.params['wdir']
min_haplotype_barcodes=snakemake.params['min_haplotype_barcodes']
min_haplotype_samples=snakemake.params['min_haplotype_samples']
min_haplotype_sample_fraction=snakemake.params['min_haplotype_sample_fraction']

# extract the settings template
settings = mip.get_analysis_settings(temp_settings_file)
settings["bwaOptions"]=[settings['bwaOptions']]+bwa_extra
settings['species']=species
settings['processorNumber']=processor_number
settings['mipSetKey'] = probe_sets_used + [''] #this feels weird, why are we adding an extra element?
settings['minHaplotypeBarcodes']=min_haplotype_barcodes
settings['minHaplotypeSamples']=min_haplotype_samples
settings['minHaplotypeSampleFraction']=min_haplotype_sample_fraction
mip.write_analysis_settings(settings, wdir+'/settings.txt')
