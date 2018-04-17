# -*- coding: utf-8 -*-
"""
Defines unit tests for :mod:`colour.models.rgb.transfer_functions.dicom_gsdf`
module.
"""

from __future__ import division, unicode_literals

import numpy as np
import unittest

from colour.models.rgb.transfer_functions import (oetf_DICOMGSDF,
                                                  eotf_DICOMGSDF)
from colour.utilities import ignore_numpy_errors

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013-2018 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = ['TestOetf_DICOMGSDF', 'TestEotf_DICOMGSDF']


class TestOetf_DICOMGSDF(unittest.TestCase):
    """
    Defines :func:`colour.models.rgb.transfer_functions.dicom_gsdf.\
oetf_DICOMGSDF` definition unit tests methods.
    """

    def test_oetf_DICOMGSDF(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.dicom_gsdf.\
oetf_DICOMGSDF` definition.
        """

        self.assertAlmostEqual(
            oetf_DICOMGSDF(0.05), 0.001007281350787, places=7)

        self.assertAlmostEqual(
            oetf_DICOMGSDF(130.0662), 0.500486263438448, places=7)

        self.assertAlmostEqual(
            oetf_DICOMGSDF(4000), 1.000160314715578, places=7)

        self.assertAlmostEqual(
            oetf_DICOMGSDF(130.0662, out_int=True), 512, places=7)

    def test_n_dimensional_oetf_DICOMGSDF(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.dicom_gsdf.\
oetf_DICOMGSDF` definition n-dimensional arrays support.
        """

        L = 130.0662
        J = 0.500486263438448
        np.testing.assert_almost_equal(oetf_DICOMGSDF(L), J, decimal=7)

        L = np.tile(L, 6)
        J = np.tile(J, 6)
        np.testing.assert_almost_equal(oetf_DICOMGSDF(L), J, decimal=7)

        L = np.reshape(L, (2, 3))
        J = np.reshape(J, (2, 3))
        np.testing.assert_almost_equal(oetf_DICOMGSDF(L), J, decimal=7)

        L = np.reshape(L, (2, 3, 1))
        J = np.reshape(J, (2, 3, 1))
        np.testing.assert_almost_equal(oetf_DICOMGSDF(L), J, decimal=7)

    @ignore_numpy_errors
    def test_nan_oetf_DICOMGSDF(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.dicom_gsdf.\
oetf_DICOMGSDF` definition nan support.
        """

        oetf_DICOMGSDF(np.array([-1.0, 0.0, 1.0, -np.inf, np.inf, np.nan]))


class TestEotf_DICOMGSDF(unittest.TestCase):
    """
    Defines :func:`colour.models.rgb.transfer_functions.dicom_gsdf.
eotf_DICOMGSDF` definition unit tests methods.
    """

    def test_eotf_DICOMGSDF(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.dicom_gsdf.\
eotf_DICOMGSDF` definition.
        """

        self.assertAlmostEqual(
            eotf_DICOMGSDF(0.001007281350787), 0.050143440671692, places=7)

        self.assertAlmostEqual(
            eotf_DICOMGSDF(0.500486263438448), 130.062864706476550, places=7)

        self.assertAlmostEqual(
            eotf_DICOMGSDF(1.000160314715578), 3997.586161113322300, places=7)

        self.assertAlmostEqual(
            eotf_DICOMGSDF(512, in_int=True), 130.065284012159790, places=7)

    def test_n_dimensional_eotf_DICOMGSDF(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.dicom_gsdf.\
eotf_DICOMGSDF` definition n-dimensional arrays support.
        """

        J = 0.500486263438448
        L = 130.062864706476550
        np.testing.assert_almost_equal(eotf_DICOMGSDF(J), L, decimal=7)

        J = np.tile(J, 6)
        L = np.tile(L, 6)
        np.testing.assert_almost_equal(eotf_DICOMGSDF(J), L, decimal=7)

        J = np.reshape(J, (2, 3))
        L = np.reshape(L, (2, 3))
        np.testing.assert_almost_equal(eotf_DICOMGSDF(J), L, decimal=7)

        J = np.reshape(J, (2, 3, 1))
        L = np.reshape(L, (2, 3, 1))
        np.testing.assert_almost_equal(eotf_DICOMGSDF(J), L, decimal=7)

    @ignore_numpy_errors
    def test_nan_eotf_DICOMGSDF(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.dicom_gsdf.\
eotf_DICOMGSDF` definition nan support.
        """

        eotf_DICOMGSDF(np.array([-1.0, 0.0, 1.0, -np.inf, np.inf, np.nan]))


if __name__ == '__main__':
    unittest.main()
