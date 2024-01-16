def round_(number, ndigits: int = None):
    # Due to this special case, we have some partial code duplication
    if ndigits is None:
        fraction = number % 1
        return int(number) if fraction < 0.5 else int(number + 1)
    scale = 10 ** ndigits
    scaled_number = number * scale
    fraction = scaled_number % 1
    return int(scaled_number) / scale if fraction < 0.5 else int(scaled_number + 1) / scale


# Alternative solution without scaling (due to floating point arithmetic, some
# inputs will yield different results than the solution above)
def round_2(number, ndigits: int = None):
    if ndigits is None:
        fraction = number % 1
        return int(number) if fraction < 0.5 else int(number + 1)
    mod = 10 ** -ndigits
    # Converting to float is done because the task description states that float
    # values should be returned. The implementation would still work without it,
    # just that the type of the returned value would then depend on the type of
    # "number" and on the value of "ndigits", e.g., round(123, -2) would return
    # the integer 100 rather than the float 100.0
    fraction = float(number % mod)
    comparison = 0.5 * mod
    return number - fraction if fraction < comparison else number - fraction + mod
