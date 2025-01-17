#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
********************************************
Created on Mon Apr  2 10:14:27 2018
by
Chamara Rajapakshe
(cpn.here@umbc.edu)
********************************************
tools for spot_MODIS_3Deffects.py
"""
import numpy as np
import matplotlib.pyplot as plt
import os,string
import scipy.signal as signal
from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable
import pickle
#import mpl_toolkits.basemap as bm

class pkl_classes(object):
    def __init__(self,):
        self.class_names=[]

def find_CDF(data,bins=None):
    '''
    To find cumulative distribution function (CDF)
    data: 1D data array
    bins: bins for the histogram
    '''
    weights=np.ones_like(data)/len(data)
    if bins is None:
        val, base = np.histogram(data, weights=weights)
    else:
        val, base = np.histogram(data, bins=bins,weights=weights)
    return base[1:], np.cumsum(val)

def save_obj(obj, name ):
    '''
    To temporally save object/dictonary
    File names will be OVERWRITTEN!!
    '''
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
    print(name + '.pkl SAVED!')

def load_obj(name ):
    '''
    To load temporally saved object/dictionary
    '''
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f,encoding='latin1')
        
def add_cb(fig,ctf,ax,ticks=None,orientation='horizontal',label='label',pad=0.2):
    divider = make_axes_locatable(ax)
    if orientation=='horizontal':
        cax = divider.append_axes("bottom", size="5%", pad=pad)
    elif orientation=='vertical':
        cax = divider.append_axes("right", size="5%", pad=pad)
    if ticks is None:    
        fig.colorbar(ctf, cax=cax,orientation=orientation,label=label)
    else:
        fig.colorbar(ctf, cax=cax,ticks=ticks,orientation=orientation,label=label)
def savefig(fig,fig_ttl,path=None):
    '''
    fig: Figure object matplotlib.figure.Figure
    fig_ttl: figure title string (some specila characterls will be removed from the file name)
    '''
    rp=False
    for ch in [' ','[',']']:
        if ch in fig_ttl:
            fig_ttl=fig_ttl.replace(ch,'_')
    fig_ttl=fig_ttl.replace('.','p')
    if path==None:
        filename=fig_ttl
    else:
        filename=path+fig_ttl
    if os.path.isfile(filename+'.png'):
        usr=raw_input('Replace existing file?: ')
        if usr=='y':
            rp=True
    else:
        rp=True
    if rp:
        fig.savefig(filename+'.png', format='png', dpi=200)
        print(filename+'.png SAVED.')

def mapProject(ax,lat={'mn':-90,'mx':90},lon={'mn':-180,'mx':180},line_step={'lon':45.0,'lat':30.0}):
    lat_int=line_step['lat']
    lon_int=line_step['lon']

    mapproj = bm.Basemap(ax=ax,projection='cyl',llcrnrlat= lat['mn'], llcrnrlon= lon['mn'],urcrnrlat= lat['mx'], urcrnrlon= lon['mx'])
    
    latlines = np.arange(lat['mn'],lat['mx'],lat_int)
    lonlines = np.arange(lon['mn'],lon['mx'],lon_int)
    
    mapproj.drawcoastlines()
    mapproj.drawparallels(latlines, labels=[1,0,0,0])
    mapproj.drawmeridians(lonlines, labels=[0,0,0,1])
    
    return mapproj
