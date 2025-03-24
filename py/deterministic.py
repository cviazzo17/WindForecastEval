import numpy as np


def bias(reference_arr, forecast_arr):
    """
    Compute bias or mean error

    Parameters:
        reference_arr (numpy.ndarray): Reference or verification values with shape (year, lat, lon)
        forecast_arr (numpy.ndarray): Deterministic forecast values with shape (year, lat, lon)

    Returns:
        numpy.ndarray: bias values with shape (lat, lon).
    """
    reference_arr = np.asarray(reference_arr)
    forecast_arr = np.asarray(forecast_arr)

    if reference_arr.shape != forecast_arr.shape:
        raise ValueError(
            "Shapes of reference_arr and forecast_arr must match (year, lat, lon)."
        )

    bias = np.nanmean(forecast_arr - reference_arr, axis=0)
    return bias


def mae(reference_arr, forecast_arr):
    """
    Compute Mean Absolute Error (MAE)

    Parameters:
        reference_arr (numpy.ndarray): Reference or verification values with shape (year, lat, lon)
        forecast_arr (numpy.ndarray): Deterministic forecast values with shape (year, lat, lon)

    Returns:
        numpy.ndarray: MAE values with shape (lat, lon).
    """

    mae = np.nanmean(np.abs(forecast_arr - reference_arr), axis=0)
    return mae


def nrmsess_cross_validated(reference_arr, forecast_arr):
    """
    Compute Normalized Root Mean Squared Error Skill Score (NRMSESS)
    Uses the one-year-out cross-validation approach

    Parameters:
        reference_arr (numpy.ndarray): Reference or verification values with shape (year, lat, lon)
        forecast_arr (numpy.ndarray): Deterministic forecast values with shape (year, lat, lon)

    Returns:
        numpy.ndarray: NRMSESS values with shape (lat, lon).
    """
    reference_arr = np.asarray(reference_arr)
    forecast_arr = np.asarray(forecast_arr)

    if reference_arr.shape != forecast_arr.shape:
        raise ValueError(
            "Shapes of reference_arr and forecast_arr must match (year, lat, lon)."
        )

    T = forecast_arr.shape[0]

    reference_arr_mean = np.full(forecast_arr.shape, np.nan)
    forecast_arr_mean = np.full(forecast_arr.shape, np.nan)

    for t in range(T):
        reference_arr_mean[t] = np.nanmean(
            np.delete(reference_arr, obj=t, axis=0), axis=0
        )
        forecast_arr_mean[t] = np.nanmean(
            np.delete(forecast_arr, obj=t, axis=0), axis=0
        )

    num = np.sqrt(
        np.nanmean(
            (forecast_arr - forecast_arr_mean + reference_arr_mean - reference_arr)
            ** 2,
            axis=0,
        )
    )

    denom = np.sqrt(np.nanmean((reference_arr - reference_arr_mean) ** 2, axis=0))

    nrmsess = 1 - num / denom
    return nrmsess


def acc_cross_validated(reference_arr, forecast_arr):
    """
    Compute Anomalt Correlation Coeffitient (ACC)
    Uses the one-year-out cross-validation approach

    Parameters:
        reference_arr (numpy.ndarray): Reference or verification values with shape (year, lat, lon)
        forecast_arr (numpy.ndarray): Deterministic forecast values with shape (year, lat, lon)

    Returns:
        numpy.ndarray: ACC values with shape (lat, lon).
    """

    reference_arr = np.asarray(reference_arr)
    forecast_arr = np.asarray(forecast_arr)

    if reference_arr.shape != forecast_arr.shape:
        raise ValueError(
            "Shapes of reference_arr and forecast_arr must match (year, lat, lon)."
        )

    T = forecast_arr.shape[0]

    reference_arr_mean = np.full(forecast_arr.shape, np.nan)
    forecast_arr_mean = np.full(forecast_arr.shape, np.nan)

    for t in range(T):
        reference_arr_mean[t] = np.nanmean(
            np.delete(reference_arr, obj=t, axis=0), axis=0
        )
        forecast_arr_mean[t] = np.nanmean(
            np.delete(forecast_arr, obj=t, axis=0), axis=0
        )

    covariance = np.sum(
        ((forecast_arr - forecast_arr_mean) * (reference_arr - reference_arr_mean)),
        axis=0,
    )
    std_reference = np.sqrt(np.sum(((reference_arr - reference_arr_mean) ** 2), axis=0))
    std_forecast = np.sqrt(np.sum(((forecast_arr - forecast_arr_mean) ** 2), axis=0))

    acc = covariance / (std_forecast * std_reference)
    return acc
