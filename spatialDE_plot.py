import argparse
import numpy as np
import pandas as pd
import sys
import NaiveDE
import SpatialDE
import matplotlib.pyplot as plt

parser=argparse.ArgumentParser()
parser.add_argument('-cd',"--counts_df",required=True)
parser.add_argument("-ld","--location_df",required=True)
parser.add_argument("-g","--gene",required=True)
args =  parser.parse_args()

def Spatial_DE(filterd_exprs, coordinates):
    if(filterd_exprs.shape[0] != coordinates.shape[0]):
        sys.exit("The number of cells in expression file and location file don't match\n")
    else:
        ## results and ms_results
        coordinates_cp = coordinates.copy()
        coordinates_cp['total_counts'] = filterd_exprs.sum(1)
        
        dfm = NaiveDE.stabilize(filterd_exprs.T).T
        res = NaiveDE.regress_out(coordinates_cp, dfm.T, 'np.log(total_counts)').T
        res['log_total_count'] = np.log(coordinates_cp['total_counts'])
        
        results = SpatialDE.run(coordinates, res)

        de_results = results[(results.qval < 0.05)].copy()
        if(de_results.shape[0] > 0):
            ms_results = SpatialDE.model_search(coordinates, res, de_results)
            result_dic = ms_results.sort_values('qval')[['g', 'FSV', 'pval','qval']]
        
        else:
            print("No spatially variable genes found! \n")
            result_dic = results
        
        return result_dic

def Spatial_norm(filterd_exprs, coordinates):
    if(filterd_exprs.shape[0] != coordinates.shape[0]):
        sys.exit("The number of cells in expression file and location file don't match\n")
    else:
        ## results and ms_results
        coordinates_cp = coordinates.copy()
        coordinates_cp['total_counts'] = filterd_exprs.sum(1)
        
        dfm = NaiveDE.stabilize(filterd_exprs.T).T
    return dfm


counts = pd.read_csv(args.counts_df,index_col = 0)
sample_info = pd.read_csv(args.location_df,index_col = 0)
counts = counts.loc[sample_info.index]
gene = pd.read_csv(args.gene)
gene1=gene['gene']


norm_expr=Spatial_norm(counts,sample_info)
gene1=gene['gene']
for i in range(len(gene1)):
    plt.scatter(sample_info['x'], sample_info['y'], c=norm_expr[gene1[i]])
    plt.title(gene1[i])
    plt.axis('equal')
    plt.colorbar(ticks=[])
    plt.savefig("./scatter{}.pdf".format(i))  #输入地址，并利用format函数修改图片名称
    plt.clf()