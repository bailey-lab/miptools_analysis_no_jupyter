snakemake -s setup_run.smk --cores 4
snakemake -s check_run_stats.smk --profile singularity_profile
snakemake -s variant_calling.smk --profile singularity_profile
