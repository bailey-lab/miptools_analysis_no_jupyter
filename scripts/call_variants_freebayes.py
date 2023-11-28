import sys
sys.path.append("/opt/src")
import mip_functions as mip

wdir=snakemake.params['wdir']
settings_file=snakemake.params['settings_file']
options=snakemake.params['freebayes_settings']
settings = mip.get_analysis_settings(wdir+'/'+settings_file)
targets_file=snakemake.params.targets_file

verbose=True
fastq_dir="/opt/analysis/padded_fastqs"
bam_dir="/opt/analysis/padded_bams"
vcf_file="/opt/analysis/variants.vcf.gz"
errors_file="/opt/analysis/freebayes_errors.txt"
warnings_file="/opt/analysis/freebayes_warnings.txt"

#what is the purpose of the variable 'r'? I don't think it ever gets used again.
r = mip.freebayes_call(settings=settings, options=options, align=True,
verbose=True, fastq_dir=fastq_dir, bam_dir=bam_dir, vcf_file=vcf_file,
targets_file=targets_file, bam_files=None, errors_file=errors_file,
warnings_file=warnings_file, fastq_padding=20)

contig_dict_list, results, errors=r
for contig_dict in contig_dict_list:
	print(contig_dict)
