'''
There is a problem here: If the miptools singularity image is run with
--use-singularity, then folder bindings can only be passed at the command line
with --singularity-args (not from a config file) and are therefore not logged.
If singularity image is run without --use-singularity, then there's no easy way
to pass snakemake variables to the python scripts (user is then using 'shell' to
call singularity exec, which probably doesn't pass snakemake variables to python
scripts inside a singularity environment the way 'script' might).
'''

configfile: 'check_run_stats.yaml'
singularity: config['sif_file']

rule all:
	snakefile='run_settings/check_run_stats.smk',
	other_settings='run_settings/ozkan_settings/settings.txt'

rule copy_params:
	'''
	copies snakemake file, config file, profile, and python scripts to output
	folder
	'''
	input:
		snakefile='check_run_stats.smk',
		configfile='check_run_stats.yaml',
		profile='singularity_profile',
		scripts='scripts'
	output:
		snakefile='run_settings/check_run_stats.smk',
		configfile='run_settings/check_run_stats.yaml',
		profile='run_settings/check_run_stats.yaml',
		scripts=directory('run_settings/scripts')
	shell:
		'''
		cp input.snakefile output.snakefile
		cp input.configfile output.configfile
		cp input.profile output.profile
		cp input.scripts output.scripts
		'''

rule modify_ozkan_settings:
	'''
	copies Ozkan's default settings, plus any user updated settings, to an
	output folder alongside the data for later reference.
	'''
	input:
		template_settings='/opt/resources/templates/analysis_settings_templates/settings.txt',
	params:
		processor_number=config['processor_number'],
		bwa_options=config['bwa_options'],
		species=config['species'],
		probe_sets_used=config['probe_sets_used']
	output:
		default_settings='/opt/analysis/template_settings.txt',
		user_settings='/opt/analysis/settings.txt'
	script:
		'scripts/modify_ozkan_settings.py'
