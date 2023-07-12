
######## snakemake preamble start (automatically inserted, do not edit) ########
import sys; sys.path.extend(['/mnt/snakemake', '/users/asimkin/.cache/snakemake/snakemake/source-cache/runtime-cache/tmpk_r54bvn/file/nfs/jbailey5/baileyweb/asimkin/github_pipelines/miptools_analysis_no_jupyter/variant_calling/scripts', '/nfs/jbailey5/baileyweb/asimkin/github_pipelines/miptools_analysis_no_jupyter/variant_calling/scripts']); import pickle; snakemake = pickle.loads(b"\x80\x04\x95\x97\r\x00\x00\x00\x00\x00\x00\x8c\x10snakemake.script\x94\x8c\tSnakemake\x94\x93\x94)\x81\x94}\x94(\x8c\x05input\x94\x8c\x0csnakemake.io\x94\x8c\nInputFiles\x94\x93\x94)\x81\x94\x8cs/nfs/jbailey5/baileyweb/asimkin/miptools/Mikalayi_TES/whole_dataset_wrangled/variant_calling/aligned_haplotypes.csv\x94a}\x94(\x8c\x06_names\x94}\x94\x8c\x12_allowed_overrides\x94]\x94(\x8c\x05index\x94\x8c\x04sort\x94eh\x10\x8c\tfunctools\x94\x8c\x07partial\x94\x93\x94h\x06\x8c\x19Namedlist._used_attribute\x94\x93\x94\x85\x94R\x94(h\x16)}\x94\x8c\x05_name\x94h\x10sNt\x94bh\x11h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x11sNt\x94bub\x8c\x06output\x94h\x06\x8c\x0bOutputFiles\x94\x93\x94)\x81\x94(\x8ch/nfs/jbailey5/baileyweb/asimkin/miptools/Mikalayi_TES/whole_dataset_wrangled/variant_calling/contig_vcfs\x94\x8ch/nfs/jbailey5/baileyweb/asimkin/miptools/Mikalayi_TES/whole_dataset_wrangled/variant_calling/padded_bams\x94\x8cj/nfs/jbailey5/baileyweb/asimkin/miptools/Mikalayi_TES/whole_dataset_wrangled/variant_calling/padded_fastqs\x94\x8cp/nfs/jbailey5/baileyweb/asimkin/miptools/Mikalayi_TES/whole_dataset_wrangled/variant_calling/variants.vcf.gz.csi\x94\x8cl/nfs/jbailey5/baileyweb/asimkin/miptools/Mikalayi_TES/whole_dataset_wrangled/variant_calling/variants.vcf.gz\x94\x8ck/nfs/jbailey5/baileyweb/asimkin/miptools/Mikalayi_TES/whole_dataset_wrangled/variant_calling/unfixed.vcf.gz\x94\x8co/nfs/jbailey5/baileyweb/asimkin/miptools/Mikalayi_TES/whole_dataset_wrangled/variant_calling/new_vcf_header.txt\x94\x8cs/nfs/jbailey5/baileyweb/asimkin/miptools/Mikalayi_TES/whole_dataset_wrangled/variant_calling/freebayes_warnings.txt\x94\x8cq/nfs/jbailey5/baileyweb/asimkin/miptools/Mikalayi_TES/whole_dataset_wrangled/variant_calling/freebayes_errors.txt\x94\x8co/nfs/jbailey5/baileyweb/asimkin/miptools/Mikalayi_TES/whole_dataset_wrangled/variant_calling/targets.vcf.gz.tbi\x94\x8ck/nfs/jbailey5/baileyweb/asimkin/miptools/Mikalayi_TES/whole_dataset_wrangled/variant_calling/targets.vcf.gz\x94e}\x94(h\x0c}\x94(\x8c\x0bcontig_vcfs\x94K\x00N\x86\x94\x8c\x0bpadded_bams\x94K\x01N\x86\x94\x8c\rpadded_fastqs\x94K\x02N\x86\x94\x8c\x0evariants_index\x94K\x03N\x86\x94\x8c\x08variants\x94K\x04N\x86\x94\x8c\x10unfixed_variants\x94K\x05N\x86\x94\x8c\nnew_header\x94K\x06N\x86\x94\x8c\x08warnings\x94K\x07N\x86\x94\x8c\x06errors\x94K\x08N\x86\x94\x8c\rtargets_index\x94K\tN\x86\x94\x8c\x0btargets_vcf\x94K\nN\x86\x94uh\x0e]\x94(h\x10h\x11eh\x10h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x10sNt\x94bh\x11h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x11sNt\x94bh1h$h3h%h5h&h7h'h9h(h;h)h=h*h?h+hAh,hCh-hEh.ub\x8c\x06params\x94h\x06\x8c\x06Params\x94\x93\x94)\x81\x94(]\x94(\x8c\x13--pooled-continuous\x94\x8c\x18--min-alternate-fraction\x94\x8c\x040.01\x94\x8c\x15--min-alternate-count\x94\x8c\x012\x94\x8c\x12--haplotype-length\x94\x8c\x013\x94\x8c\x15--min-alternate-total\x94\x8c\x0210\x94\x8c\x14--use-best-n-alleles\x94\x8c\x0270\x94\x8c\x14--genotype-qualities\x94\x8c\x06--gvcf\x94\x8c\x15--gvcf-dont-use-chunk\x94\x8c\x04true\x94e\x8c\r/opt/analysis\x94\x8c\x0csettings.txt\x94e}\x94(h\x0c}\x94(\x8c\x12freebayes_settings\x94K\x00N\x86\x94\x8c\x04wdir\x94K\x01N\x86\x94\x8c\rsettings_file\x94K\x02N\x86\x94uh\x0e]\x94(h\x10h\x11eh\x10h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x10sNt\x94bh\x11h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x11sNt\x94bhhhThjhdhlheub\x8c\twildcards\x94h\x06\x8c\tWildcards\x94\x93\x94)\x81\x94}\x94(h\x0c}\x94h\x0e]\x94(h\x10h\x11eh\x10h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x10sNt\x94bh\x11h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x11sNt\x94bub\x8c\x07threads\x94K\x01\x8c\tresources\x94h\x06\x8c\tResources\x94\x93\x94)\x81\x94(K\x01K\x01J@\r\x03\x00J\x0f\xe9\x02\x00M\xe8\x03M\xba\x03\x8c\x04/tmp\x94K\x10M\x80\x16\x8ci/nfs/jbailey5/baileyweb/asimkin/miptools/Mikalayi_TES/whole_dataset_wrangled/variant_calling/run_settings\x94e}\x94(h\x0c}\x94(\x8c\x06_cores\x94K\x00N\x86\x94\x8c\x06_nodes\x94K\x01N\x86\x94\x8c\x06mem_mb\x94K\x02N\x86\x94\x8c\x07mem_mib\x94K\x03N\x86\x94\x8c\x07disk_mb\x94K\x04N\x86\x94\x8c\x08disk_mib\x94K\x05N\x86\x94\x8c\x06tmpdir\x94K\x06N\x86\x94\x8c\x05nodes\x94K\x07N\x86\x94\x8c\x08time_min\x94K\x08N\x86\x94\x8c\x07log_dir\x94K\tN\x86\x94uh\x0e]\x94(h\x10h\x11eh\x10h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x10sNt\x94bh\x11h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x11sNt\x94bh\x8fK\x01h\x91K\x01h\x93J@\r\x03\x00h\x95J\x0f\xe9\x02\x00h\x97M\xe8\x03h\x99M\xba\x03h\x9bh\x8b\x8c\x05nodes\x94K\x10\x8c\x08time_min\x94M\x80\x16h\xa1h\x8cub\x8c\x03log\x94h\x06\x8c\x03Log\x94\x93\x94)\x81\x94}\x94(h\x0c}\x94h\x0e]\x94(h\x10h\x11eh\x10h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x10sNt\x94bh\x11h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x11sNt\x94bub\x8c\x06config\x94}\x94(\x8c\routput_folder\x94\x8c\\/nfs/jbailey5/baileyweb/asimkin/miptools/Mikalayi_TES/whole_dataset_wrangled/variant_calling\x94\x8c\x08sif_file\x94\x8cN/nfs/jbailey5/baileyweb/asimkin/miptools/miptools_tutorial/miptools_v0.4.0.sif\x94\x8c\x12freebayes_settings\x94]\x94(hUhVhWhXhYhZh[h\\h]h^h_h`hahbhceu\x8c\x04rule\x94\x8c\x17call_variants_freebayes\x94\x8c\x0fbench_iteration\x94N\x8c\tscriptdir\x94\x8ce/nfs/jbailey5/baileyweb/asimkin/github_pipelines/miptools_analysis_no_jupyter/variant_calling/scripts\x94ub."); from snakemake.logging import logger; logger.printshellcmds = True; __real_file__ = __file__; __file__ = '/nfs/jbailey5/baileyweb/asimkin/github_pipelines/miptools_analysis_no_jupyter/variant_calling/scripts/call_variants_freebayes.py';
######## snakemake preamble end #########
import sys
sys.path.append("/opt/src")
import mip_functions as mip

wdir=snakemake.params['wdir']
settings_file=snakemake.params['settings_file']
options=snakemake.params['freebayes_settings']
settings = mip.get_analysis_settings(wdir+'/'+settings_file)

verbose=True
fastq_dir="/opt/analysis/padded_fastqs"
bam_dir="/opt/analysis/padded_bams"
vcf_file="/opt/analysis/variants.vcf.gz"
targets_file="/opt/project_resources/targets.tsv"
errors_file="/opt/analysis/freebayes_errors.txt"
warnings_file="/opt/analysis/freebayes_warnings.txt"

#what is the purpose of the variable 'r'? I don't think it ever gets used again.
r = mip.freebayes_call(settings=settings, options=options, align=True,
verbose=True, fastq_dir=fastq_dir, bam_dir=bam_dir, vcf_file=vcf_file,
targets_file=targets_file, bam_files=None, errors_file=errors_file,
warnings_file=warnings_file, fastq_padding=20)
