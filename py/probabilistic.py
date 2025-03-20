import numpy as np


def terciles(sample):
    """
    Compute the terciles (q0.33 and q0.66) for the sample

    Parameters:
        sample (numpy.array): Sample values

    Returns:
        numpy.array: terciles
    """
    return np.nanquantile(sample, q=[1 / 3, 2 / 3])


def median(sample):
    """
    Compute the terciles (q0.33 and q0.66) for the sample

    Parameters:
        sample (numpy.array): Sample values

    Returns:
        numpy.array: terciles
    """
    return np.nanquantile(sample, q=[1 / 2])


def cross_validation(forecast_arr, func_statistic, n_statistic, window_width=1):
    """
    Compute a given statistic using a cross-validation-approch

    Parameters:
        forecast_arr: (numpy.ndarray): Ensemble values with shape (year, gridpoint, ensemble_member)
        func_statistic (function): Function to compute the statistic (e.g., terciles or median)
        n_statistic (int): Number of statistics computed per gridpoint (e.g., for terciles, n_statistic = 2, and for median, n_statistic = 1)
        window_width (int): Width of windwo cross-validation. Default value of 1 (three-leave-out cross-validation)

    Returns:
        numpy.ndarray: Array of shape (year, gridpoint, statistic) with computed statistics
    """
    n_year = forecast_arr[0]
    n_point = forecast_arr[1]
    result = np.full((n_year, n_point, n_statistic), np.nan)

    for year in range(n_year):
        window_idx = np.arange(year - window_width, year + window_width + 1)
        if year == 0:
            window_idx = np.arange(0, window_idx * 2 + 1)
        if year == (n_year - 1):
            window_idx = np.arange(year - window_idx * 2, n_year)
        data_partial = np.delete(forecast_arr, window_idx, axis=0)

        for point in n_point:
            result[year, point, :] = func_statistic(data_partial[:, point])
    return result
