# -*- coding: utf-8 -*-

"""
@author: Nicolás Nieto - nnieto

Power Spectral Density
"""
# In[] Imports modules

import mne
import numpy as np


from mne.time_frequency import psd_welch
from Data_extractions   import Extract_block_data_from_subject, Extract_data_from_subject
from Data_processing    import Filter_by_condition, Filter_by_class
from Utilitys           import Ensure_dir, unify_names


# In[]: Processing Variables

# Root where the data are stored
root_dir = "/media/nnieto/50e793fa-4717-4997-b590-b4167be63ee7/home/nnieto/Escritorio/Nico/Doctorado/Tesis/LIAA - sinc(i)/Toma de datos/Dataset InnerSpeech/"
save_dir = "/media/nnieto/50e793fa-4717-4997-b590-b4167be63ee7/home/nnieto/Escritorio/Nico/Doctorado/Tesis/LIAA - sinc(i)/Toma de datos/Analisis/PSD/Dataset final/PSD_Calculated/"

# Save options
save_bool = False
overwrite = True

# Subjets list
N_S_list=[1]

# Data filtering
datatype="EEG"
Conditions_list = ["Pron"]      # All - Pron - Inner - Vis
Classes_list = [ "Left"]        # All - Up - Down - Right - Left

#Fix all random states
random_state = 23
np.random.seed(random_state)

# Time window
tmin = 0.5
tmax = 3

# PSD Parameters
fmin = 0.5
fmax = 100
n_overlap = 0
n_fft = 256
picks = "all"
average = "mean"


# In[]: Main Loop

# Load a single subject to use the Epoched Object structure
N_B=1
N_S=1
X_S, Y = Extract_block_data_from_subject(root_dir,N_S,datatype,N_B=N_B)

# Set Montage
Adquisition_eq="biosemi128"
montage=mne.channels.make_standard_montage(Adquisition_eq)
X_S.set_montage(montage)

for Classes in Classes_list:   
    for Cond in Conditions_list:
        count=1
        for N_S in N_S_list :
            
            # Load full subject's data
            X_s, Y = Extract_data_from_subject(root_dir,N_S,datatype)
        
            # Filter by condition
            X_cond , Y_cond = Filter_by_condition(X_s, Y, Condition = Cond)
        
            # Filter by class
            X_cond , Y_cond =  Filter_by_class(X_cond, Y_cond, Class = Classes)
            
            # Stack trial for every subject
            if count == 1:    
                #Inicialiced
                X_data = X_cond
                count  = 2
            else:
                #Stack trials
                X_data = np.vstack((X_data, X_cond))
        
        # In[]
        # Calculated TFR for a particular clase in a particular condition for the selected subjects
        print("Calculated PSD for Class: " + Classes +" in Condition: " + Cond )
        print("with the information of Subjects: " + str(N_S_list ))
        
        # Create a subject with all trials
        X_S._data = X_data

        psds , freqs = psd_welch(X_S, fmin = fmin , fmax = fmax, tmin = tmin ,tmax = tmax, n_fft = n_fft,
                                 average = average, n_overlap = n_overlap, picks = picks)
        if save_bool:
            Ensure_dir(save_dir)
            Cond, Classes = unify_names(Cond, Class = Classes)
            file_name = save_dir + "PSD_" + Cond + "_" + Classes + "_PSD-tfr.h5"
            psds.save(fname = file_name, overwrite = overwrite)
            
