import numpy as np
import sys
import os

sys.path.append(os.path.abspath("../py"))
from deterministic import acc_cross_validated


def var_noise(forecast_arr):
    """
    Compute the variance of noise

    Parameters:
        forecast_arr (numpy.ndarray): Ensemble values with shape (year, ensemble_member, lat, lon)

    Returns:
        numpy.ndarray: variance of noise values with shape (lat, lon).
    """
    forecast_arr = np.asarray(forecast_arr)

    T = forecast_arr.shape[0]
    M = forecast_arr.shape[1]

    ensemble_mean = np.nanmean(forecast_arr, axis=1)
    ensemble_mean = np.reshape(
        ensemble_mean, (T, 1, forecast_arr.shape[-2], forecast_arr.shape[-1])
    )

    difference_quad = (forecast_arr - ensemble_mean) ** 2

    result = np.nanmean(np.nanmean(difference_quad, axis=1), axis=0) * (M / (M - 1))

    return result


def var_signal(forecast_arr):
    """
    Compute the variance of signal

    Parameters:
        forecast_arr (numpy.ndarray): Ensemble values with shape (year, ensemble_member, lat, lon)

    Returns:
        numpy.ndarray: variance of signal values with shape (lat, lon).
    """
    forecast_arr = np.asarray(forecast_arr)

    result = np.nanstd(np.nanmean(forecast_arr, axis=1), axis=0) ** 2

    return result


def total_var(forecast_arr):
    """
    Compute the variance of signal

    Parameters:
        forecast_arr (numpy.ndarray): Ensemble values with shape (year, ensemble_member, lat, lon)

    Returns:
        numpy.ndarray: total variance values with shape (lat, lon).
    """
    forecast_arr = np.asarray(forecast_arr)

    result = var_signal(forecast_arr) + var_noise(forecast_arr)

    return result


def potential_predictability(forecast_arr):
    """
    Compute potential predictability

    Parameters:
        forecast_arr (numpy.ndarray): Ensemble values with shape (year, ensemble_member, lat, lon)

    Returns:
        numpy.ndarray: potential predictability values with shape (lat, lon).
    """
    forecast_arr = np.asarray(forecast_arr)

    result = (var_signal(forecast_arr)) / total_var(forecast_arr)

    return result


def perfect_skill(forecast_arr):
    """
    Compute the perfect-model skill

    Parameters:
        forecast_arr (numpy.ndarray): Ensemble values with shape (year, ensemble_member, lat, lon)

    Returns:
        numpy.ndarray: perfect-model skill values with shape (lat, lon).
    """
    forecast_arr = np.asarray(forecast_arr)

    M = forecast_arr.shape[1]

    result_partial = np.full(
        (M, forecast_arr.shape[-2], forecast_arr.shape[-1]), np.nan
    )

    for m in range(M):
        member = forecast_arr[:, m, :]
        mean_over_members = np.nanmean(np.delete(forecast_arr, obj=m, axis=1), axis=1)

        result_partial[m] = acc_cross_validated(member, mean_over_members)

    result = np.nanmean(result_partial, axis=0)
    return result
