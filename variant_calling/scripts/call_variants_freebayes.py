import sys
sys.path.append("/opt/src")
import mip_functions as mip
import subprocess

wdir=snakemake.params['wdir']
settings_file=snakemake.params['settings_file']
options=snakemake.params['freebayes_settings']
processor_number=snakemake.params.processor_number
settings = mip.get_analysis_settings(wdir+'/'+settings_file)

settings['processorNumber']=processor_number
verbose=True
fastq_dir="/opt/analysis/padded_fastqs"
bam_dir="/opt/analysis/padded_bams"
vcf_file="/opt/analysis/variants.vcf.gz"
targets_file="/opt/project_resources/targets.tsv"
errors_file="/opt/analysis/freebayes_errors.txt"
warnings_file="/opt/analysis/freebayes_warnings.txt"

#what is the purpose of the variable 'r'? I don't think it ever gets used again.
subprocess.call('ulimit -n 10000', shell=True)
r = mip.freebayes_call(settings=settings, options=options, align=True,
verbose=True, fastq_dir=fastq_dir, bam_dir=bam_dir, vcf_file=vcf_file,
targets_file=targets_file, bam_files=None, errors_file=errors_file,
warnings_file=warnings_file, fastq_padding=20)
