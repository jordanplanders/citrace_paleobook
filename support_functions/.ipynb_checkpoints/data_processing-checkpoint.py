import numpy as np


def between(ds, var, lims):
    ds.coords[var] = ds.coords[var].load()
    _ds = ds.where((ds.coords[var]<max(lims)) & (ds.coords[var]>min(lims)), drop=True)
    return _ds


def lon_180_to_360(x):
    return x % 360


def convert_z_to_meters(ds):
    cm_to_m = 1/100
    z_t = ds.z_t.data
    ds['z_t_m'] = ("z_t", z_t*cm_to_m)
    ds = ds.swap_dims({'z_t':'z_t_m'})
    return ds


def epsNd(Nd):
    (Nd143, Nd144) = Nd
    Nd_CHUR = 0.512638
    scaler = 1000
    return (np.divide(Nd143,Nd144)*1/Nd_CHUR-1)*10**4