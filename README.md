# WindForecastEval
This repository contains the scripts and data used in a study on the predictability and skill assessment of seasonal 10-meter wind speed forecasts over Argentina.

## Data
- **Variable:** 3-monthly mean 10-meter wind speed.
- **Region:** Argentina.
- **Study period:** Focus on December-January-February (DJF) during the period 1994-2017.
- **Data availability:**
    - CFSv2 and SEAS5 data are publicly available through the [Copernicus Climate Data Store](https://cds.climate.copernicus.eu/). MERRA2 reanalysis products are accessible via the [NASA POWER Project](https://power.larc.nasa.gov/) and [NASA GES DISC](https://disc.gsfc.nasa.gov/)
    - Processed data are stored in the `data/` subdirectory.

## Methods

### Interpolation
Processed data has a common grid of 1.0°x1.0°, corresponding to the retrieved SEAS5 horizontal resolution, which is the coarser resolution of the raw datasets. CFSv2 and MERRA2 data were interpolated using the `scipy.interpolate` function `RectBivariateSpline`.

### Predictability assessment
The functions used for predictability analysis are located in `py/predictability.py`, while their execution and visualization are performed in `ipynb/predictability/`.

### Deterministic skill assessment
The functions used for the deterministic skill assessment are located in `py/deterministic.py`, while their execution and visualization are performed in `ipynb/deterministic_forecasts/`.

### Region-specific analysis and probabilistic assessment
This analysis is performed for three selected regions. The selection of the data corresponding to the regions of analysis was done in `ipynb/time_series_extract/`. The `py/probabilistic.py` script contains the functions used for constructing probabilistic forecasts using a three-year-out cross-validation for median- and tercile-based categories. Performance analysis and metrics are presented in `ipynb/probabilistic_forecasts/`.


## Repository Structure

```bash
WindForecastEval/
├── data/                  
│   ├── cfsv2_djf.npz  
│   ├── cfsv2_jja.npz  
│   ├── elev.0.5-deg.nc  
│   ├── eolicos.json  
│   ├── merra2_djf.npz  
│   ├── merra2_jja.npz  
│   ├── seas5_djf.npz  
│   └── seas5_jja.npz  
├── ipynb/                 # Jupyter notebooks for analysis and visualization  
│   ├── deterministic_forecasts/  
│   │   ├── bootstrap_test_bias.ipynb  
│   │   └── deterministic_forecasts.ipynb  
│   ├── predictability/  
│   │   └── predictability.ipynb  
│   ├── probabilistic_forecasts/  
│   │   ├── bs/  
│   │   │   ├── bs_and_decomposition_median.ipynb  
│   │   │   ├── bs_and_decomposition_terciles.ipynb  
│   │   │   ├── npz_to_rds_prob.ipynb  
│   │   │   └── rds/  
│   │   │       ├── median_prob_and_reference_cfsv2_djf_r1.rds  
│   │   │       ├── median_prob_and_reference_cfsv2_djf_r2.rds  
│   │   │       ├── median_prob_and_reference_cfsv2_djf_r3.rds  
│   │   │       ├── median_prob_and_reference_seas5_djf_r1.rds  
│   │   │       ├── median_prob_and_reference_seas5_djf_r2.rds  
│   │   │       ├── median_prob_and_reference_seas5_djf_r3.rds  
│   │   │       ├── terciles_prob_and_reference_cfsv2_djf_r1.rds  
│   │   │       ├── terciles_prob_and_reference_cfsv2_djf_r2.rds  
│   │   │       ├── terciles_prob_and_reference_cfsv2_djf_r3.rds  
│   │   │       ├── terciles_prob_and_reference_seas5_djf_r1.rds  
│   │   │       ├── terciles_prob_and_reference_seas5_djf_r2.rds  
│   │   │       └── terciles_prob_and_reference_seas5_djf_r3.rds  
│   │   ├── probability_median.ipynb  
│   │   ├── probability_terciles.ipynb  
│   │   ├── reliability_diagrams/  
│   │   │   ├── reliability_diagrams_median.ipynb  
│   │   │   └── reliability_diagrams_terciles.ipynb  
│   │   └── roc/  
│   │       ├── roc_curves_median.ipynb  
│   │       └── roc_curves_terciles.ipynb  
│   └── time_series_extract/  
│       ├── plot_ws_anomalies_timeseries.ipynb  
│       └── time_series_extract.ipynb  
├── outputs/             
│   ├── bias_test/  
│   │   ├── bootstrap_bias_cfsv2_djf.npz  
│   │   └── bootstrap_bias_seas5_djf.npz  
│   ├── probabilistic_forecasts/  
│   │   ├── median_prob_and_reference_djf_r1.npz  
│   │   ├── median_prob_and_reference_djf_r2.npz  
│   │   ├── median_prob_and_reference_djf_r3.npz  
│   │   ├── terciles_prob_and_reference_djf_r1.npz  
│   │   ├── terciles_prob_and_reference_djf_r2.npz  
│   │   └── terciles_prob_and_reference_djf_r3.npz  
│   └── timeseries/  
│       ├── timeseries_djf_r1.npz  
│       ├── timeseries_djf_r2.npz  
│       └── timeseries_djf_r3.npz  
├── py/                    # Python scripts with functions used in the study
│   ├── deterministic.py  
│   ├── predictability.py  
│   └── probabilistic.py  
├── README.md              
├── requirements.txt      
