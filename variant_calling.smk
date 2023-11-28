configfile: 'miptools_analysis_no_jupyter.yaml'
#singularity: config['sif_file']
output_folder=config['output_directory']
log_folder=config['output_directory']+'/run_settings/variant_calling'
import subprocess
subprocess.call(f'mkdir {log_folder}', shell=True)

rule all:
	input:
		snakefile=log_folder+'/variant_calling.smk',
		cov_table=output_folder+'/coverage_table.csv'
#		targets_vcf=output_folder+'/targets.vcf.gz'

rule copy_params:
	'''
	copies snakemake file, config file, profile, and python scripts to output
	folder
	'''
	input:
		snakefile='variant_calling.smk',
		configfile='miptools_analysis_no_jupyter.yaml',
		profile='singularity_profile',
		scripts='scripts'
	output:
		snakefile=log_folder+'/variant_calling.smk',
		configfile=log_folder+'/miptools_analysis_no_jupyter.yaml',
		profile=directory(log_folder+'/singularity_profile'),
		scripts=directory(log_folder+'/scripts')
	resources:
		log_dir=log_folder
	shell:
		'''
		cp {input.snakefile} {output.snakefile}
		cp {input.configfile} {output.configfile}
		cp -r {input.profile} {output.profile}
		cp -r {input.scripts} {output.scripts}
		'''

rule call_variants_freebayes:
	'''
	calls variants with freebayes and produces a VCF output file
	'''
	input:
		output_folder+'/aligned_haplotypes.csv',
	output:
		contig_vcfs=directory(output_folder+'/contig_vcfs'),
		padded_bams=directory(output_folder+'/padded_bams'),
		padded_fastqs=directory(output_folder+'/padded_fastqs'),
		variants_index=output_folder+'/variants.vcf.gz.csi',
		variants=output_folder+'/variants.vcf.gz',
		unfixed_variants=output_folder+'/unfixed.vcf.gz',
		new_header=output_folder+'/new_vcf_header.txt',
		warnings=output_folder+'/freebayes_warnings.txt',
		errors=output_folder+'/freebayes_errors.txt',
		targets_index=output_folder+'/targets.vcf.gz.tbi',
		targets_vcf=output_folder+'/targets.vcf.gz'
	params:
		targets_file=config['target_aa_annotation'],
		freebayes_settings=config['freebayes_settings'],
		wdir='/opt/analysis',
		settings_file='settings.txt'
	#resources below are currently not utilized - haven't figured out a way to
	#get singularity profile, slurm profile, and high ulimits all at once.
	resources:
		mem_mb=200000,
		nodes=16,
		time_min=5760,
		log_dir=log_folder
	singularity: config['sif_file']
	script:
		'scripts/call_variants_freebayes.py'

rule generate_tables:
	input:
		variants=output_folder+'/variants.vcf.gz'
	output:
		ref_table=output_folder+'/reference_table.csv',
		cov_table=output_folder+'/coverage_table.csv',
		alt_table=output_folder+'/alternate_table.csv'
	params:
		wdir='/opt/analysis',
		settings_file='settings.txt',
		geneid_to_genename=config['geneid_to_genename'],
		target_aa_annotation=config['target_aa_annotation'],
		aggregate_nucleotides=config['aggregate_nucleotides'],
		aggregate_aminoacids=config['aggregate_aminoacids'],
		target_nt_annotation=config['target_nt_annotation'],
		annotate=config['annotate'],
		decompose_options=config['decompose_options'],
		annotated_vcf=config['annotated_vcf'],
		aggregate_none=config['aggregate_none'],
		output_prefix=config['output_prefix']
	singularity: config['sif_file']
	script:
		'scripts/generate_tables.py'
