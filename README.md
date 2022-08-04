# Compute SRT svg
This is a process of concatenating spatialDE
## Work Flow
This process uses the method of finding SVG in spatialDE. 
For the specific reason and process, see [spatialDE](https://www.nature.com/articles/nmeth.4636)
## Requirements
This script runs based on python, and the required python packages are as follows：
* argparse
* numpy
* pandas
* sys
* NaiveDE
* SpatialDE
* matplotlib
## Use the script
To use this script you can calculate an SVG of your own data, you need to provide 
a spatial expression matrix with ** row names for cell names, columns for gene names ** 
and a file with spatial location information 
1. Example of a spatial representation matrix: [Rep11_MOB_0.csv](https://github.com/gouxiaojuan/pipeline_spatialDE/blob/main/example/Rep11_MOB_0.csv)<br>
2. Example of a file with spatial location information: [MOB_sample_info.csv](https://github.com/gouxiaojuan/pipeline_spatialDE/blob/main/example/MOB_sample_info.csv)<br>

If you have these two files ready, you can get the SVG using the following command：<br>
`$ python spatialDE.py --counts_df=Rep11_MOB_0.csv --location_df=MOB_sample_info.csv`

With this script you can get a [svg_spatialDE.csv](https://github.com/gouxiaojuan/pipeline_spatialDE/blob/main/example/svg_spatialDE.csv)
where column g represents the found SVG and column FSV represents the spatial variance score


# SVG visualization
This script can draw the spatial expression mos of the SVG you are interested in
## Requirements
This script runs based on python, and the required python packages are as follows:
* argparse
* numpy
* pandas
* sys
* NaiveDE
* SpatialDE
* matplotlib
## Use the script
To use this script you can calculate an SVG of your own data, you need to provide 
a spatial expression matrix with ** row names for cell names, columns for gene names ** 
and a file with spatial location information 
1. Example of a spatial representation matrix: [Rep11_MOB_0.csv](https://github.com/gouxiaojuan/pipeline_spatialDE/blob/main/example/Rep11_MOB_0.csv)<br>
2. Example of a file with spatial location information: [MOB_sample_info.csv](https://github.com/gouxiaojuan/pipeline_spatialDE/blob/main/example/MOB_sample_info.csv)<br>
3. Sample files for the SVG you are interested in: [gene.csv](https://github.com/gouxiaojuan/pipeline_spatialDE/blob/main/example/gene.csv)

If you have these two files ready, you can get the SVG using the following command：<br>
`$ python spatialDE_plot.py --counts_df=Rep11_MOB_0.csv --location_df=MOB_sample_info.csv --gene=gene.csv`

With this script you can get the expression pattern of your gene of interest, e.g.:[Kcnh3](https://github.com/gouxiaojuan/pipeline_spatialDE/blob/main/image/scatter0.pdf),[Pcp4](https://github.com/gouxiaojuan/pipeline_spatialDE/blob/main/image/scatter1.pdf),[Igfbp2](https://github.com/gouxiaojuan/pipeline_spatialDE/blob/main/image/scatter2.pdf)