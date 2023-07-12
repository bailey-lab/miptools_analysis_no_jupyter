
######## snakemake preamble start (automatically inserted, do not edit) ########
import sys; sys.path.extend(['/mnt/snakemake', '/users/asimkin/.cache/snakemake/snakemake/source-cache/runtime-cache/tmp1x7qm0xt/file/nfs/jbailey5/baileyweb/asimkin/github_pipelines/miptools_analysis_no_jupyter/check_run_stats/scripts', '/nfs/jbailey5/baileyweb/asimkin/github_pipelines/miptools_analysis_no_jupyter/check_run_stats/scripts']); import pickle; snakemake = pickle.loads(b'\x80\x04\x95z\x08\x00\x00\x00\x00\x00\x00\x8c\x10snakemake.script\x94\x8c\tSnakemake\x94\x93\x94)\x81\x94}\x94(\x8c\x05input\x94\x8c\x0csnakemake.io\x94\x8c\nInputFiles\x94\x93\x94)\x81\x94\x8co/nfs/jbailey5/baileyweb/asimkin/miptools/Mikalayi_TES/whole_dataset_wrangled/variant_calling/barcode_counts.csv\x94a}\x94(\x8c\x06_names\x94}\x94\x8c\x0ebarcode_counts\x94K\x00N\x86\x94s\x8c\x12_allowed_overrides\x94]\x94(\x8c\x05index\x94\x8c\x04sort\x94eh\x12\x8c\tfunctools\x94\x8c\x07partial\x94\x93\x94h\x06\x8c\x19Namedlist._used_attribute\x94\x93\x94\x85\x94R\x94(h\x18)}\x94\x8c\x05_name\x94h\x12sNt\x94bh\x13h\x16h\x18\x85\x94R\x94(h\x18)}\x94h\x1ch\x13sNt\x94bh\x0eh\nub\x8c\x06output\x94h\x06\x8c\x0bOutputFiles\x94\x93\x94)\x81\x94\x8cm/nfs/jbailey5/baileyweb/asimkin/miptools/Mikalayi_TES/whole_dataset_wrangled/variant_calling/umi_heatmap.html\x94a}\x94(h\x0c}\x94\x8c\x0coutput_graph\x94K\x00N\x86\x94sh\x10]\x94(h\x12h\x13eh\x12h\x16h\x18\x85\x94R\x94(h\x18)}\x94h\x1ch\x12sNt\x94bh\x13h\x16h\x18\x85\x94R\x94(h\x18)}\x94h\x1ch\x13sNt\x94bh)h&ub\x8c\x06params\x94h\x06\x8c\x06Params\x94\x93\x94)\x81\x94\x8c\r/opt/analysis\x94a}\x94(h\x0c}\x94\x8c\x04wdir\x94K\x00N\x86\x94sh\x10]\x94(h\x12h\x13eh\x12h\x16h\x18\x85\x94R\x94(h\x18)}\x94h\x1ch\x12sNt\x94bh\x13h\x16h\x18\x85\x94R\x94(h\x18)}\x94h\x1ch\x13sNt\x94bh;h8ub\x8c\twildcards\x94h\x06\x8c\tWildcards\x94\x93\x94)\x81\x94}\x94(h\x0c}\x94h\x10]\x94(h\x12h\x13eh\x12h\x16h\x18\x85\x94R\x94(h\x18)}\x94h\x1ch\x12sNt\x94bh\x13h\x16h\x18\x85\x94R\x94(h\x18)}\x94h\x1ch\x13sNt\x94bub\x8c\x07threads\x94K\x01\x8c\tresources\x94h\x06\x8c\tResources\x94\x93\x94)\x81\x94(K\x01K\x01M\xa0\x0fM\xe7\x0eM\xe8\x03M\xba\x03\x8c\x04/tmp\x94K\x01Kx\x8cy/nfs/jbailey5/baileyweb/asimkin/miptools/Mikalayi_TES/whole_dataset_wrangled/variant_calling/run_settings/check_run_stats\x94e}\x94(h\x0c}\x94(\x8c\x06_cores\x94K\x00N\x86\x94\x8c\x06_nodes\x94K\x01N\x86\x94\x8c\x06mem_mb\x94K\x02N\x86\x94\x8c\x07mem_mib\x94K\x03N\x86\x94\x8c\x07disk_mb\x94K\x04N\x86\x94\x8c\x08disk_mib\x94K\x05N\x86\x94\x8c\x06tmpdir\x94K\x06N\x86\x94\x8c\x05nodes\x94K\x07N\x86\x94\x8c\x08time_min\x94K\x08N\x86\x94\x8c\x07log_dir\x94K\tN\x86\x94uh\x10]\x94(h\x12h\x13eh\x12h\x16h\x18\x85\x94R\x94(h\x18)}\x94h\x1ch\x12sNt\x94bh\x13h\x16h\x18\x85\x94R\x94(h\x18)}\x94h\x1ch\x13sNt\x94bh^K\x01h`K\x01hbM\xa0\x0fhdM\xe7\x0ehfM\xe8\x03hhM\xba\x03hjhZ\x8c\x05nodes\x94K\x01\x8c\x08time_min\x94Kx\x8c\x07log_dir\x94h[ub\x8c\x03log\x94h\x06\x8c\x03Log\x94\x93\x94)\x81\x94}\x94(h\x0c}\x94h\x10]\x94(h\x12h\x13eh\x12h\x16h\x18\x85\x94R\x94(h\x18)}\x94h\x1ch\x12sNt\x94bh\x13h\x16h\x18\x85\x94R\x94(h\x18)}\x94h\x1ch\x13sNt\x94bub\x8c\x06config\x94}\x94(\x8c\routput_folder\x94\x8c\\/nfs/jbailey5/baileyweb/asimkin/miptools/Mikalayi_TES/whole_dataset_wrangled/variant_calling\x94\x8c\x08sif_file\x94\x8cN/nfs/jbailey5/baileyweb/asimkin/miptools/miptools_tutorial/miptools_v0.4.0.sif\x94\x8c\x10processor_number\x94K\x10\x8c\tbwa_extra\x94]\x94(\x8c\x02-t\x94\x8c\x0216\x94e\x8c\x07species\x94\x8c\x02pf\x94\x8c\x0fprobe_sets_used\x94]\x94\x8c\x03IBC\x94a\x8c\rsample_groups\x94]\x94]\x94(\x8c\x03JJJ\x94\x8c\x15DR2,HAPDR,HEOME96,IBC\x94ea\x8c\rsample_sheets\x94]\x94\x8c*/opt/data/mikalayi_merged_sample_sheet.tsv\x94a\x8c\ninfo_files\x94]\x94\x8c6/opt/data/allInfo_shrunknames_filtered_samples.tab.txt\x94a\x8c\x16min_haplotype_barcodes\x94K\x01\x8c\x15min_haplotype_samples\x94K\x01\x8c\x1dmin_haplotype_sample_fraction\x94G?\x1a6\xe2\xeb\x1cC-u\x8c\x04rule\x94\x8c\x0egraph_barcodes\x94\x8c\x0fbench_iteration\x94N\x8c\tscriptdir\x94\x8ce/nfs/jbailey5/baileyweb/asimkin/github_pipelines/miptools_analysis_no_jupyter/check_run_stats/scripts\x94ub.'); from snakemake.logging import logger; logger.printshellcmds = True; __real_file__ = __file__; __file__ = '/nfs/jbailey5/baileyweb/asimkin/github_pipelines/miptools_analysis_no_jupyter/check_run_stats/scripts/graph_barcodes.py';
######## snakemake preamble end #########
import sys
sys.path.append("/opt/src")
import mip_functions as mip
import pandas as pd
import matplotlib.pyplot as plt
import os

wdir=snakemake.params['wdir']

def make_graphing_list(barcode_file):
	import math
	graphing_list, rows=[],[]
	for line_number, line in enumerate(open(barcode_file)):
		line=line.strip().split(',')
		if line_number==0:
			columns=line[1:]
		if line_number>2:
			rows.append(line[0])
			int_line=list(map(int, list(map(float, line[1:]))))
			log_line=[math.log(number+1, 2) for number in int_line]
			graphing_list.append(log_line)
	return graphing_list, columns, rows

def plot_heatmap(graphing_list, x_values, y_values, x_title, y_title, count_title, output_path, width=2000, height=4000):
	import plotly.express as px
#	print(graphing_list)
	fig = px.imshow(graphing_list, aspect='auto', labels=dict(x=x_title, y=y_title,
	color=count_title), x=x_values, y=y_values)
	fig.update_xaxes(side="top")
	fig.update_layout(width=width, height=height, autosize=False)
	fig.write_html(output_path)

graphing_list, x_values, y_values=make_graphing_list(wdir+'/barcode_counts.csv')
plot_heatmap(graphing_list, x_values, y_values, 'mips', 'samples', 'log2 of umi_counts+1', '/opt/analysis/umi_heatmap.html')
