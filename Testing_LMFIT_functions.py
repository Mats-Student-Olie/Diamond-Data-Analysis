import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from lmfit.models import PseudoVoigtModel, PolynomialModel, ConstantModel, LinearModel, VoigtModel


def interactive_plot_results(x, y, init, out):
    comps = out.eval_components(x=x)

    fig, axes = plt.subplots(1, 2, figsize=(9, 3))
    axes[0].plot(x, y)
    axes[0].plot(x, init, '--', label='initial fit')
    axes[0].plot(x[~np.isnan(y)], out.best_fit, '-', label='best fit')
    for model in out.model.components:
        if "constant" in model.name:
            continue
        else:
            axes[0].plot(x, comps[model.prefix], '--', label=model.prefix)

#     axes[1].plot(x, y)
#     for model in out.model.components:
#         if "constant" in model.name:
#             continue
#         else:
#             axes[1].plot(x, comps[model.prefix], '--', label=model.prefix)

    axes[1].plot(x, y, '+', color="tab:blue", label="data")
    axes[1].plot(x, init, '--', color="tab:orange", label='initial fit')
    axes[1].plot(x[~np.isnan(y)], out.best_fit, '-', color="tab:green", label='best fit')
    for model in out.model.components:
        if "bg_spline" in model.name:
            axes[1].plot(x, comps[model.prefix], '--', color="tab:red", label=model.prefix)
        else:
            continue    

#     axes[0].legend(loc=1)
#     axes[1].legend()
#     axes[2].legend()
    axes[0].set_yscale("log")
    axes[1].set_yscale("log")
#     axes[2].set_yscale("log")
#     axes[0].set_xlim(2.5, 3.5)
#     axes[0].set_ylim(10**2,)
#     axes[1].set_xlim(2.70, 3)
#     axes[1].set_ylim(10**3, 10**5.5)
#     axes[2].set_xlim(2.60, 3)
#     axes[2].set_ylim(10**4, 10**5.5)

    plt.show()
    
def plot_results(x, y, init, out):
    comps = out.eval_components(x=x)

    fig, axes = plt.subplots(2, 2, figsize=(14, 6))
    axes[0,0].plot(x, y)
    axes[0,0].plot(x, init, '--', label='initial fit')
    axes[0,0].plot(x[~np.isnan(y)], out.best_fit, '-', label='best fit')
    for model in out.model.components:
        if "constant" in model.name:
            continue
        else:
            axes[0,0].plot(x, comps[model.prefix], '--', label=model.prefix)

    axes[0,1].plot(x, y)
    for model in out.model.components:
        if "constant" in model.name:
            continue
        else:
            axes[0,1].plot(x, comps[model.prefix], '--', label=model.prefix)
    axes[0,1].plot(x, y, '+', color="tab:blue", label="data")
    axes[0,1].plot(x, init, '--', color="tab:orange", label='initial fit')
    axes[0,1].plot(x[~np.isnan(y)], out.best_fit, '-', color="tab:green", label='best fit')
    for model in out.model.components:
        if "bg_spline" in model.name:
            axes[0,1].plot(x, comps[model.prefix], '--', color="tab:red", label=model.prefix)
        else:
            continue   
            
    axes[1,0].plot(x, y)
    for model in out.model.components:
        if "constant" in model.name:
            continue
        else:
            axes[1,0].plot(x, comps[model.prefix], '--', label=model.prefix)
    axes[1,0].plot(x, y, '+', color="tab:blue", label="data")
    axes[1,0].plot(x, init, '--', color="tab:orange", label='initial fit')
    axes[1,0].plot(x[~np.isnan(y)], out.best_fit, '-', color="tab:green", label='best fit')
    for model in out.model.components:
        if "bg_spline" in model.name:
            axes[1,0].plot(x, comps[model.prefix], '--', color="tab:red", label=model.prefix)
        else:
            continue 
            
    axes[1,1].plot(x, y)
    for model in out.model.components:
        if "constant" in model.name:
            continue
        else:
            axes[1,1].plot(x, comps[model.prefix], '--', label=model.prefix)
    axes[1,1].plot(x, y, '+', color="tab:blue", label="data")
    axes[1,1].plot(x, init, '--', color="tab:orange", label='initial fit')
    axes[1,1].plot(x[~np.isnan(y)], out.best_fit, '-', color="tab:green", label='best fit')
    for model in out.model.components:
        if "bg_spline" in model.name:
            axes[1,1].plot(x, comps[model.prefix], '--', color="tab:red", label=model.prefix)
        else:
            continue 

#     axes[0].legend(loc=1)
#     axes[1].legend()
#     axes[2].legend()
    axes[0,0].set_yscale("log")
    axes[0,1].set_yscale("log")
    axes[1,0].set_yscale("log")
    axes[1,1].set_yscale("log")
#     axes[2].set_yscale("log")
#     axes[0].set_xlim(2.5, 3.5)
#     axes[0].set_ylim(10**2,)
    axes[0,1].set_xlim(2.80, 3)
    axes[0,1].set_ylim(10, 10000)
    axes[1,0].set_xlim(4.6, 5.0)
    axes[1,0].set_ylim(10, 5000)
    axes[1,1].set_xlim(5.35, 5.65)
    axes[1,1].set_ylim(10, 3500)

    plt.show()
    
def auto_peak_selector(data_x, data_y, threshold):

    maxima = []

    for i, val in enumerate(data_y):
        if data_y[i] > threshold:
            maxima.append((i,val))
 
    consecutive_list = []

    for i in range(len(maxima)):

        try:

            #check consecutiveness
#             print(maxima[i+1][0])
            if maxima[i+1][0] - maxima[i][0] == 1:

                #check if it's already in list
                if (data_x[maxima[i][0]], maxima[i][1]) not in consecutive_list:
                    consecutive_list.append((data_x[maxima[i][0]], maxima[i][1]))

                #add last one too
                consecutive_list.append((data_x[maxima[i+1][0]], maxima[i + 1][1]))

            else:

                #yield here and empty list
                yield consecutive_list
                consecutive_list = []
        except Exception:
            pass
    yield consecutive_list
    
def auto_minimum_selector(data_x, data_y, threshold):
    minima = []
    for i, val in enumerate(data_y):
        if data_y[i] < threshold:
            minima.append((i, val))
    
    consecutive_list = []

    for i in range(len(minima)):

        try:

            #check consecutiveness
            if minima[i+1][0] - minima[i][0] == 1:

                #check if it's already in list
                if (data_x[minima[i][0]], minima[i][1]) not in consecutive_list:
                    consecutive_list.append((data_x[minima[i][0]], minima[i][1]))

                #add last one too
                consecutive_list.append((data_x[minima[i+1][0]], minima[i + 1][1]))

            else:

                #yield here and empty list
                yield consecutive_list
                consecutive_list = []
        except Exception:
            pass
    yield consecutive_list

    
def update_params(out):
    for param in out.params.valuesdict().keys():
        if "center" in param:
            ### calc movement of peak centre ###
            increment = out.params[param].value - old_params[param].value
            centre_value = out.params[param].value
            centre_min = out.params[param].min
            centre_max = out.params[param].max
            print(param, "Increment = ", f"{increment:.2e}", "Min = ", f"{centre_min:.2e}", "Max = ", f"{centre_max:.2e}")
            ### update the new parameter min & max by increment ###
            out.params[param].set(value= centre_value + increment, min= centre_min + increment, max= centre_max + increment)
    return out.params


def merge_cakes(frames, cake_list):
    '''
    frames: list(pathlib.Path(experiment_dir) containing list of the stacked frames
    cake_list: list of cakes to merge where #cake = #column i.e. cake1 = column1
    returns data as transposed numpy array as [[twothetas],[F1-intensity],[F2-intensity],...]
    '''
    ### setup pd.df to add data to ###
    twothetas = np.loadtxt(frames[0])[:,0]
    df = pd.DataFrame(data={"twotheta": twothetas})

    ### perform merge ###
    for fname in frames: # for each stacked frames "merge" cakes
        data = np.loadtxt(fname)
        merge = np.nansum(data[:,cake_list], axis=1)         # merge cakes for each bin range
        frame_num = fname.stem.split("_")[-1]                # get frame number for col header
        merge_df = pd.DataFrame(data={frame_num: merge})     # put new data into df
        df = df.join(merge_df)                               # join the two dataframes
    return df.to_numpy().T, sorted(list(df)[1:])
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            