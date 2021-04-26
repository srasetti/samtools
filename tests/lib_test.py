# -*- coding: UTF-8 -*-

# Import from standard library
import os
import samtools
import pandas as pd
# Import from our lib
from samtools.lib import clean_data, is_palyndrome
import pytest


def test_clean_data():
    datapath = os.path.dirname(os.path.abspath(samtools.__file__)) + '/data'
    df = pd.read_csv('{}/data.csv.gz'.format(datapath))
    first_cols = ['id', 'civility', 'birthdate', 'city', 'postal_code', 'vote_1']
    assert list(df.columns)[:6] == first_cols
    assert df.shape == (999, 142)
    out = clean_data(df)
    assert out.shape == (985, 119)

def test_is_palyndrome():
    assert is_palyndrome("Bob") == True
    assert is_palyndrome("12345") == False
