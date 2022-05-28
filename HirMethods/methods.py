def num_sep(a):
    import locale
    locale.setlocale(locale.LC_ALL, '')  # Use '' for auto, or force e.g. to 'en_US.UTF-8'
    value = a
    value = f'{value:n}'  # For Python ≥3.6
    return value