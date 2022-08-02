import argparse
import numpy as np
import pandas as pd
import sys
import NaiveDE
import SpatialDE

parser=argparse.ArgumentParser()
parser.add_argument('-cd',"--counts_df",required=True)
parser.add_argument("-ld","--location_df",required=True)
args =  parser.parse_args()


#定义函数
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

#读入文件
counts = pd.read_csv(args.counts_df)
sample_info = pd.read_csv(args.location_df)
counts = counts.loc[sample_info.index]
SVG = Spatial_DE(counts,sample_info)
results1 = SVG["ms_results"].sort_values('qval')[['g', 'FSV', 'qval']]
results1.to_csv("svg_ms.csv",index=False)