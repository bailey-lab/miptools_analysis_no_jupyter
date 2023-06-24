'''
The code this function depends on could probably be significantly streamlined by
reading and writing settings file dictionaries with yaml instead of Ozkan's
custom functions.
Also, not sure why mipSetKey needs an empty entry added on to the existing list.
'''
import mip_functions as mip

temp_settings_file = snakemake.input['template_settings']
processor_number=snakemake.params['processor_number'],
bwa_extra=snakemake.params['bwa_extra'],
species=snakemake.params['species'],
probe_sets_used=snakemake.params['probe_sets_used']
subprocess.call(['cp', temp_settings_file, '/opt/analysis/template_settings.txt'])
# extract the settings template
temp_settings = mip.get_analysis_settings("/opt/analysis/template_settings.txt")
temp_settings["bwaOptions"].extend(bwa_extra)
temp_settings['species']=species
temp_settings['processorNumber']=processor_number
temp_settings['mipSetKey'] = probe_sets_used + ['']
mip.write_analysis_settings(temp_settings, '/opt/analysis/settings.txt')
settings = mip.get_analysis_settings(wdir + settings_file)
