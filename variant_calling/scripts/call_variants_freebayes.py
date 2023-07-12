import sys
sys.path.append("/opt/src")
import mip_functions as mip
import subprocess
import resource

wdir=snakemake.params['wdir']
settings_file=snakemake.params['settings_file']
options=snakemake.params['freebayes_settings']
processor_number=snakemake.params.processor_number
freebayes_threads=snakemake.params.freebayes_threads
settings = mip.get_analysis_settings(wdir+'/'+settings_file)


settings['freebayes_threads']=freebayes_threads
settings['processorNumber']=processor_number
verbose=True
fastq_dir="/opt/analysis/padded_fastqs"
bam_dir="/opt/analysis/padded_bams"
vcf_file="/opt/analysis/variants.vcf.gz"
targets_file="/opt/project_resources/targets.tsv"
errors_file="/opt/analysis/freebayes_errors.txt"
warnings_file="/opt/analysis/freebayes_warnings.txt"

#what is the purpose of the variable 'r'? I don't think it ever gets used again.
hard_limit=int(subprocess.check_output('ulimit -Hn', shell=True).decode().strip())
soft_limit=int(hard_limit*0.9)
resource.setrlimit(resource.RLIMIT_NOFILE, (soft_limit, hard_limit))

subprocess.call('ulimit -Sn $(ulimit -Hn)', shell=True)
r = mip.freebayes_call(settings=settings, options=options, align=True,
verbose=True, fastq_dir=fastq_dir, bam_dir=bam_dir, vcf_file=vcf_file,
targets_file=targets_file, bam_files=None, errors_file=errors_file,
warnings_file=warnings_file, fastq_padding=20)
