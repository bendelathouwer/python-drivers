
import scoop_wrapper
import matplotlib.pyplot as plt
import numpy as np
#plotting needs figuering out
#-1.400001e+00,-1.460001e+00,-1.440001e+00,-1.380001e+00,-1.380001e+00,-1.440001e+00,-1.420001e+00,-1.360001e+00,-1.400001e+00,-1.320001e+00,-1.340001e+00,-1.380001e+00,-1.380001e+00,-1.300001e+00,-1.300001e+00,-1.340001e+00,-1.340001e+00,-1.260001e+00,-1.320001e+00,-1.260001e+00,-1.300001e+00,-1.220001e+00,-1.220001e+00,-1.280001e+00,-1.260001e+00,-1.180001e+00,-1.240001e+00,-1.160001e+00,-1.220001e+00,-1.140001e+00,-1.200001e+00,-1.120001e+00,-1.160001e+00,-1.100001e+00,-1.140001e+00,-1.080001e+00,-1.120001e+00,-1.040001e+00,-1.100001e+00,-1.020001e+00,-1.060001e+00,-1.000001e+00,-1.040001e+00,-9.600015e-01,-1.020001e+00,-9.400015e-01,-9.600015e-01,-9.000015e-01,-9.600015e-01,-8.800015e-01,-9.000015e-01,-8.600016e-01,-8.800015e-01,-8.000016e-01,-8.000016e-01,-8.400016e-01,-8.200016e-01,-7.600017e-01,-8.000016e-01,-7.000017e-01,-7.600017e-01,-6.800017e-01,-7.200017e-01,-6.400018e-01,-6.800017e-01,-6.200018e-01,-6.600018e-01,-5.800018e-01,-6.200018e-01,-5.600019e-01,-5.800018e-01,-5.000019e-01,-5.600019e-01,-4.800019e-01,-5.200019e-01,-4.400019e-01,-5.000019e-01,-4.000019e-01,-4.400019e-01,-3.800018e-01,-4.200019e-01,-3.400018e-01,-3.800018e-01,-3.000018e-01,-3.200018e-01,-2.600018e-01,-3.000018e-01,-2.200018e-01,-2.600018e-01,-1.800018e-01,-2.200018e-01,-1.400018e-01,-1.800018e-01,-1.200018e-01,-1.400018e-01,-6.000182e-02,-1.000018e-01,-4.000182e-02,-6.000182e-02,-1.817942e-06,-4.000182e-02,3.999818e-02,-1.817942e-06,7.999818e-02,3.999818e-02,1.199982e-01,9.999818e-02,1.599982e-01,1.199982e-01,1.799982e-01,1.599982e-01,2.199982e-01,1.999982e-01,2.599981e-01,2.399981e-01,2.999982e-01,2.799982e-01,3.399982e-01,2.999982e-01,3.799982e-01,3.399982e-01,4.199982e-01,4.399982e-01,3.799982e-01,4.199982e-01,4.799983e-01,4.399982e-01,5.199983e-01,4.799983e-01,5.599982e-01,5.199983e-01,5.999982e-01,5.599982e-01,6.199982e-01,5.999982e-01,6.599981e-01,6.399981e-01,6.999981e-01,6.399981e-01,7.199981e-01,6.799981e-01,7.599980e-01,7.199981e-01,7.799980e-01,7.399980e-01,8.199980e-01,7.999980e-01,8.599979e-01,8.199980e-01,8.999979e-01,8.599979e-01,9.199979e-01,8.799979e-01,9.599978e-01,9.199979e-01,9.999978e-01,9.999978e-01,9.399979e-01,9.599978e-01,1.039998e+00,9.999978e-01,1.059998e+00,1.019998e+00,1.099998e+00,1.059998e+00,1.119998e+00,1.079998e+00,1.159998e+00,1.099998e+00,1.159998e+00,1.119998e+00,1.199998e+00,1.139998e+00,1.219998e+00,1.179998e+00,1.239998e+00,1.199998e+00,1.259998e+00,1.219998e+00,1.279998e+00,1.239998e+00,1.299998e+00,1.259998e+00,1.319998e+00,1.299998e+00,1.339998e+00,1.299998e+00,1.359998e+00,1.359998e+00,1.299998e+00,1.339998e+00,1.379997e+00,1.359998e+00,1.399997e+00,1.359998e+00,1.419997e+00,1.379997e+00,1.439997e+00,1.399997e+00,1.439997e+00,1.399997e+00,1.459997e+00,1.419997e+00,1.479997e+00,1.479997e+00,1.439997e+00,1.439997e+00,1.499997e+00,1.439997e+00,1.499997e+00,1.459997e+00,1.519997e+00,1.459997e+00,1.519997e+00,1.459997e+00,1.519997e+00,1.459997e+00,1.539997e+00,1.479997e+00,1.539997e+00,1.479997e+00,1.539997e+00,1.539997e+00,1.479997e+00,1.479997e+00,1.539997e+00,1.479997e+00,1.539997e+00,1.479997e+00,1.539997e+00,1.539997e+00,1.479997e+00,1.479997e+00,1.539997e+00,1.519997e+00,1.459997e+00,1.519997e+00,1.459997e+00,1.459997e+00,1.519997e+00,1.499997e+00,1.459997e+00,1.459997e+00,1.499997e+00,1.499997e+00,1.439997e+00,1.459997e+00,1.419997e+00,1.419997e+00,1.479997e+00,1.459997e+00,1.399997e+00,1.399997e+00,1.459997e+00,1.379997e+00,1.439997e+00,1.379997e+00,1.419997e+00,1.399997e+00,1.359998e+00,1.379997e+00,1.339998e+00,1.359998e+00,1.319998e+00,1.339998e+00,1.279998e+00,1.339998e+00,1.279998e+00,1.319998e+00,1.259998e+00,1.299998e+00,1.239998e+00,1.279998e+00,1.219998e+00,1.259998e+00,1.199998e+00,1.239998e+00,1.179998e+00,1.199998e+00,1.139998e+00,1.179998e+00,1.139998e+00,1.179998e+00,1.099998e+00,1.139998e+00,1.079998e+00,1.119998e+00,1.059998e+00,1.099998e+00,1.019998e+00,1.059998e+00,9.999978e-01,1.039998e+00,9.599978e-01,9.999978e-01,9.399979e-01,9.999978e-01,9.199979e-01,9.399979e-01,8.999979e-01,9.199979e-01,8.399979e-01,8.799979e-01,8.199980e-01,8.599979e-01,7.999980e-01,8.199980e-01,7.599980e-01,7.999980e-01,7.399980e-01,7.599980e-01,6.799981e-01,7.199981e-01,6.599981e-01,6.999981e-01,6.199982e-01,6.599981e-01,5.999982e-01,6.399981e-01,5.599982e-01,5.799982e-01,5.199983e-01,5.599982e-01,4.799983e-01,5.199983e-01,4.599983e-01,4.799983e-01,4.199982e-01,4.599983e-01,3.799982e-01,4.199982e-01,3.599982e-01,3.799982e-01,2.999982e-01,3.399982e-01,2.799982e-01,2.999982e-01,2.399981e-01,2.599981e-01,1.999982e-01,2.199982e-01,1.599982e-01,1.799982e-01,1.199982e-01,1.599982e-01,7.999818e-02,1.199982e-01,3.999818e-02,5.999818e-02,-1.817942e-06,1.999818e-02,-4.000182e-02,-2.000182e-02,-8.000182e-02,-2.000182e-02,-1.000018e-01,-8.000182e-02,-1.600018e-01,-1.200018e-01,-1.800018e-01,-1.400018e-01,-2.200018e-01,-1.800018e-01,-2.600018e-01,-2.200018e-01,-2.800018e-01,-2.600018e-01,-3.200018e-01,-3.000018e-01,-3.600018e-01,-3.400018e-01,-4.000019e-01,-3.800018e-01,-4.400019e-01,-4.000019e-01,-4.800019e-01,-4.400019e-01,-5.200019e-01,-4.800019e-01,-5.600019e-01,-5.200019e-01,-6.000018e-01,-5.400019e-01,-6.200018e-01,-5.800018e-01,-6.600018e-01,-6.200018e-01,-6.800017e-01,-6.600018e-01,-7.200017e-01,-7.000017e-01,-7.600017e-01,-7.000017e-01,-7.800016e-01,-7.400017e-01,-8.200016e-01,-7.600017e-01,-8.400016e-01,-8.000016e-01,-9.000015e-01,-8.400016e-01,-9.200015e-01,-8.800015e-01,-9.600015e-01,-9.200015e-01,-9.600015e-01,-9.200015e-01,-1.000001e+00,-9.600015e-01,-1.040001e+00,-1.000001e+00,-1.060001e+00,-1.020001e+00,-1.100001e+00,-1.040001e+00,-1.120001e+00,-1.080001e+00,-1.140001e+00,-1.100001e+00,-1.160001e+00,-1.120001e+00,-1.180001e+00,-1.140001e+00,-1.220001e+00,-1.180001e+00,-1.240001e+00,-1.180001e+00,-1.260001e+00,-1.200001e+00,-1.280001e+00,-1.220001e+00,-1.300001e+00,-1.260001e+00,-1.320001e+00,-1.260001e+00,-1.340001e+00,-1.280001e+00,-1.360001e+00,-1.300001e+00,-1.380001e+00,-1.320001e+00,-1.400001e+00,-1.400001e+00,-1.320001e+00,-1.360001e+00,-1.420001e+00,-1.360001e+00,-1.460001e+00,-1.380001e+00,-1.440001e+00,-1.400001e+00,-1.460001e+00,-1.420001e+00,-1.480001e+00,-1.420001e+00,-1.480001e+00,-1.440001e+00,-1.480001e+00,-1.440001e+00,-1.500001e+00,-1.440001e+00,-1.500001e+00,-1.440001e+00,-1.520001e+00,-1.460001e+00,-1.520001e+00,-1.460001e+00,-1.520001e+00,-1.460001e+00,-1.540001e+00,-1.460001e+00,-1.540001e+00,-1.480001e+00,-1.540001e+00,-1.460001e+00,-1.540001e+00,-1.480001e+00,-1.540001e+00,-1.480001e+00,-1.540001e+00,-1.520001e+00,-1.460001e+00,-1.520001e+00,-1.460001e+00,-1.520001e+00,-1.460001e+00,-1.460001e+00,-1.500001e+00,-1.460001e+00,-1.520001e+00,-1.440001e+00,-1.500001e+00,-1.440001e+00,-1.500001e+00,-1.440001e+00,-1.480001e+00,-1.460001e+00,-1.420001e+00,-1.420001e+00,-1.480001e+00,-1.440001e+00,-1.400001e+00,-1.460001e+00,-1.380001e+00,-1.440001e+00,-1.380001e+00,-1.420001e+00,-1.360001e+00,-1.340001e+00,-1.400001e+00,-1.400001e+00,-1.320001e+00,-1.360001e+00,-1.280001e+00,-1.360001e+00,-1.300001e+00,-1.340001e+00,-1.260001e+00,-1.320001e+00,-1.260001e+00,-1.300001e+00,-1.240001e+00,-1.280001e+00,-1.220001e+00,-1.240001e+00,-1.180001e+00,-1.240001e+00,-1.160001e+00,-1.200001e+00,-1.140001e+00,-1.200001e+00,-1.120001e+00,-1.160001e+00,-1.100001e+00,-1.140001e+00,-1.080001e+00,-1.100001e+00,-1.040001e+00,-1.080001e+00,-1.020001e+00,-1.060001e+00,-1.000001e+00,-1.040001e+00,-9.600015e-01,-1.000001e+00,-9.400015e-01,-9.200015e-01,-9.800014e-01,-9.400015e-01,-8.800015e-01,-9.200015e-01,-8.600016e-01,-9.000015e-01,-8.200016e-01,-8.400016e-01,-7.800016e-01,-8.200016e-01,-7.600017e-01,-7.800016e-01,-7.000017e-01,-7.400017e-01,-6.800017e-01,-7.200017e-01,-6.600018e-01,-6.800017e-01,-6.200018e-01,-6.600018e-01,-5.800018e-01,-6.200018e-01,-5.400019e-01,-5.800018e-01,-5.000019e-01,-5.600019e-01,-4.800019e-01,-5.200019e-01,-4.400019e-01,-4.800019e-01,-4.000019e-01,-4.400019e-01,-3.800018e-01,-4.000019e-01,-3.400018e-01,-3.600018e-01,-3.000018e-01,-3.400018e-01,-2.600018e-01,-2.800018e-01,-2.200018e-01,-2.600018e-01,-1.800018e-01,-2.000018e-01,-1.400018e-01,-1.800018e-01,-1.000018e-01,-1.400018e-01,-6.000182e-02,-1.000018e-01,-2.000182e-02,-8.000182e-02,-1.817942e-06,-4.000182e-02,3.999818e-02,-1.817942e-06,7.999818e-02,3.999818e-02,1.199982e-01,7.999818e-02,1.399982e-01,1.199982e-01,1.799982e-01,1.599982e-01,2.199982e-01,1.999982e-01,2.599981e-01,2.199982e-01,3.199982e-01,2.799982e-01,3.399982e-01,2.999982e-01,3.799982e-01,3.399982e-01,3.999982e-01,3.999982e-01,4.599983e-01,4.199982e-01,4.799983e-01,4.599983e-01,5.399982e-01,4.799983e-01,5.399982e-01,5.199983e-01,5.999982e-01,5.599982e-01,6.199982e-01,5.999982e-01,6.599981e-01,6.199982e-01,6.999981e-01,6.599981e-01,7.199981e-01,6.999981e-01,7.599980e-01,7.399980e-01,7.999980e-01,7.599980e-01,8.199980e-01,7.999980e-01,8.599979e-01,8.399979e-01,8.799979e-01,8.599979e-01,9.399979e-01,8.999979e-01,9.599978e-01,9.599978e-01,9.399979e-01,9.399979e-01,9.999978e-01,9.799978e-01,1.059998e+00,9.999978e-01,1.079998e+00,1.019998e+00,1.099998e+00,1.059998e+00,1.119998e+00,1.079998e+00,1.159998e+00,1.099998e+00,1.159998e+00,1.119998e+00,1.199998e+00,1.159998e+00,1.219998e+00,1.179998e+00,1.239998e+00,1.199998e+00,1.259998e+00,1.279998e+00,1.219998e+00,1.299998e+00,1.239998e+00,1.259998e+00,1.319998e+00,1.339998e+00,1.259998e+00,1.279998e+00,1.359998e+00,1.319998e+00,1.379997e+00,1.339998e+00,1.379997e+00,1.359998e+00,1.399997e+00,1.359998e+00,1.439997e+00,1.419997e+00,1.379997e+00,1.399997e+00,1.439997e+00,1.399997e+00,1.479997e+00,1.419997e+00,1.479997e+00,1.439997e+00,1.479997e+00,1.439997e+00,1.479997e+00,1.459997e+00,1.499997e+00,1.499997e+00,1.459997e+00,1.459997e+00,1.519997e+00,1.459997e+00,1.539997e+00,1.479997e+00,1.539997e+00,1.519997e+00,1.479997e+00,1.539997e+00,1.479997e+00,1.479997e+00,1.539997e+00,1.539997e+00,1.479997e+00,1.479997e+00,1.539997e+00,1.539997e+00,1.479997e+00,1.479997e+00,1.539997e+00,1.479997e+00,1.519997e+00,1.479997e+00,1.539997e+00,1.519997e+00,1.459997e+00,1.459997e+00,1.519997e+00,1.459997e+00,1.519997e+00,1.519997e+00,1.459997e+00,1.479997e+00,1.439997e+00,1.479997e+00,1.439997e+00,1.479997e+00,1.419997e+00,1.419997e+00,1.459997e+00,1.459997e+00,1.399997e+00,1.439997e+00,1.379997e+00,1.419997e+00,1.359998e+00,1.399997e+00,1.359998e+00,1.379997e+00,1.339998e+00,1.379997e+00,1.339998e+00,1.359998e+00,1.299998e+00,1.339998e+00,1.259998e+00,1.339998e+00,1.259998e+00,1.299998e+00,1.239998e+00,1.279998e+00,1.219998e+00,1.259998e+00,1.199998e+00,1.239998e+00,1.179998e+00,1.219998e+00,1.159998e+00,1.199998e+00,1.139998e+00,1.159998e+00,1.099998e+00,1.159998e+00,1.079998e+00,1.119998e+00,1.059998e+00,1.039998e+00,1.099998e+00,1.059998e+00,9.999978e-01,1.039998e+00,9.599978e-01,1.019998e+00,9.399979e-01,9.999978e-01,9.199979e-01,9.599978e-01,8.799979e-01,9.399979e-01,8.599979e-01,8.399979e-01,8.999979e-01,8.599979e-01,7.999980e-01,8.199980e-01,7.599980e-01,7.799980e-01,7.199981e-01,7.599980e-01,6.999981e-01,7.199981e-01,6.599981e-01,6.999981e-01,6.399981e-01,6.599981e-01,5.999982e-01,6.399981e-01,5.599982e-01,5.999982e-01,5.199983e-01,5.599982e-01,4.999983e-01,5.199983e-01,4.599983e-01,4.799983e-01,4.199982e-01,4.599983e-01,3.799982e-01,4.199982e-01,3.599982e-01,3.799982e-01,2.999982e-01,3.599982e-01,2.799982e-01,3.199982e-01,2.399981e-01,2.599981e-01,1.799982e-01,2.199982e-01,1.599982e-01,1.999982e-01,1.199982e-01,1.599982e-01,9.999818e-02,1.199982e-01,3.999818e-02,7.999818e-02,-1.817942e-06,3.999818e-02,-2.000182e-02,1.999818e-02,-6.000182e-02,-4.000182e-02,-1.000018e-01,-6.000182e-02,-1.400018e-01,-1.000018e-01,-1.800018e-01,-1.600018e-01,-2.200018e-01,-1.800018e-01,-2.400018e-01,-2.200018e-01,-3.000018e-01,-2.600018e-01,-3.400018e-01,-3.000018e-01,-3.800018e-01,-3.400018e-01,-4.200019e-01,-3.600018e-01,-4.400019e-01,-4.000019e-01,-4.800019e-01,-4.400019e-01,-5.200019e-01,-4.600019e-01,-5.400019e-01,-5.200019e-01,-5.800018e-01,-5.400019e-01,-6.200018e-01,-6.000018e-01,-6.600018e-01,-6.000018e-01,-6.800017e-01,-6.400018e-01,-7.200017e-01,-6.600018e-01,-7.400017e-01,-7.000017e-01,-7.800016e-01,-7.400017e-01,-8.200016e-01,-7.800016e-01,-8.400016e-01,-8.200016e-01,-8.600016e-01,-8.400016e-01,-9.200015e-01,-8.800015e-01,-9.400015e-01,-9.000015e-01,-9.600015e-01,-9.200015e-01,-1.020001e+00,-9.600015e-01,-1.040001e+00,-9.800014e-01,-1.060001e+00,-1.080001e+00,-1.020001e+00,-1.040001e+00,-1.100001e+00,-1.060001e+00,-1.140001e+00,-1.100001e+00,-1.160001e+00,-1.120001e+00,-1.200001e+00,-1.140001e+00,-1.200001e+00,-1.160001e+00,-1.240001e+00,-1.180001e+00,-1.260001e+00,-1.200001e+00,-1.260001e+00,-1.220001e+00,-1.280001e+00,-1.260001e+00,-1.300001e+00,-1.260001e+00,-1.340001e+00,-1.280001e+00,-1.340001e+00,-1.320001e+00,-1.360001e+00,-1.320001e+00,-1.380001e+00,-1.340001e+00,-1.400001e+00,-1.360001e+00,-1.420001e+00,-1.360001e+00,-1.420001e+00,-1.380001e+00,-1.440001e+00,-1.400001e+00,-1.460001e+00,-1.460001e+00,-1.400001e+00,-1.420001e+00,-1.480001e+00,-1.420001e+00,-1.500001e+00,-1.440001e+00,-1.500001e+00,-1.440001e+00,-1.500001e+00,-1.460001e+00,-1.520001e+00,-1.460001e+00,-1.520001e+00,-1.460001e+00,-1.540001e+00,-1.460001e+00,-1.540001e+00,-1.520001e+00,-1.460001e+00,-1.460001e+00,-1.540001e+00,-1.540001e+00,-1.460001e+00,-1.460001e+00,-1.540001e+00,-1.460001e+00,-1.540001e+00,-1.480001e+00,-1.520001e+00,-1.460001e+00,-1.520001e+00,-1.520001e+00,-1.460001e+00,-1.460001e+00,-1.520001e+00,-1.520001e+00,-1.440001e+00,-1.440001e+00,-1.500001e+00,-1.440001e+00,-1.500001e+00,-1.440001e+00,-1.500001e+00,-1.480001e+00,-1.420001e+00,-1.460001e+00,-1.400001e+00,-1.400001e+00,-1.440001e+00,-1.440001e+00,-1.380001e+00,-1.380001e+00,-1.420001e+00,-1.340001e+00,-1.420001e+00,-1.400001e+00,-1.320001e+00,-1.380001e+00,-1.320001e+00,-1.360001e+00,-1.300001e+00,-1.300001e+00,-1.340001e+00,-1.340001e+00,-1.280001e+00,-1.320001e+00,-1.220001e+00,-1.300001e+00,-1.220001e+00,-1.220001e+00,-1.260001e+00,-1.260001e+00,-1.180001e+00,-1.240001e+00,-1.160001e+00,-1.200001e+00,-1.140001e+00,-1.180001e+00,-1.120001e+00,-1.160001e+00,-1.080001e+00,-1.080001e+00,-1.140001e+00,-1.100001e+00,-1.040001e+00,-1.080001e+00,-1.020001e+00,-1.000001e+00,-1.060001e+00,-1.020001e+00,-9.600015e-01,-9.400015e-01,-1.000001e+00,-9.200015e-01,-9.800014e-01,-9.400015e-01,-8.800015e-01,-9.000015e-01,-8.400016e-01,-8.800015e-01,-8.200016e-01,-8.000016e-01,-8.400016e-01,-8.200016e-01,-7.400017e-01,-7.800016e-01,-7.200017e-01,-7.600017e-01,-6.800017e-01,-7.200017e-01,-6.400018e-01,-6.800017e-01,-6.200018e-01,-6.600018e-01,-5.800018e-01,-6.200018e-01,-5.400019e-01,-5.800018e-01,-5.000019e-01,-5.400019e-01,-4.800019e-01,-5.200019e-01,-4.400019e-01,-4.800019e-01,-4.000019e-01,-4.400019e-01,-3.800018e-01,-4.000019e-01,-3.400018e-01,-3.600018e-01,-3.000018e-01,-3.200018e-01,-2.800018e-01,-2.800018e-01,-2.200018e-01,-2.400018e-01,-1.800018e-01,-2.200018e-01,-1.400018e-01,-1.800018e-01,-1.200018e-01,-1.400018e-01,-8.000182e-02,-1.000018e-01,-2.000182e-02,-6.000182e-02,1.999818e-02,-4.000182e-02,3.999818e-02,-1.817942e-06,7.999818e-02,3.999818e-02,1.199982e-01,9.999818e-02,1.599982e-01,1.199982e-01,1.799982e-01,1.599982e-01,2.199982e-01,1.999982e-01,2.599981e-01,2.399981e-01,2.999982e-01,2.799982e-01,3.199982e-01,3.199982e-01,3.799982e-01,3.599982e-01,4.199982e-01,3.799982e-01,4.399982e-01,4.199982e-01,4.799983e-01,4.599983e-01,5.199983e-01,5.399982e-01,4.799983e-01,5.199983e-01,5.999982e-01,5.599982e-01,6.399981e-01,5.999982e-01,6.599981e-01,6.799981e-01,6.199982e-01,6.599981e-01,7.199981e-01,6.999981e-01,7.599980e-01,7.199981e-01,7.999980e-01,7.799980e-01,8.399979e-01,7.999980e-01,8.599979e-01,8.399979e-01,8.799979e-01,8.599979e-01,9.399979e-01,8.799979e-01,9.599978e-01,9.199979e-01,9.799978e-01,9.599978e-01,1.019998e+00,9.599978e-01,1.039998e+00,9.999978e-01,1.079998e+00,1.039998e+00,1.099998e+00,1.059998e+00,1.119998e+00,1.079998e+00,1.159998e+00,1.099998e+00,1.159998e+00,1.139998e+00,1.199998e+00,1.159998e+00,1.219998e+00,1.179998e+00,1.239998e+00,1.199998e+00,1.259998e+00,1.219998e+00,1.279998e+00,1.239998e+00,1.299998e+00,1.319998e+00,1.239998e+00,1.299998e+00,1.339998e+00,1.299998e+00,1.359998e+00,1.319998e+00,1.379997e+00,1.339998e+00,1.379997e+00,1.359998e+00,1.419997e+00,1.419997e+00,1.359998e+00,1.439997e+00,1.379997e+00,1.399997e+00,1.439997e+00

scoop=scoop_wrapper.scoop("TCPIP0::169.254.226.8::INSTR")
data = scoop.takemeasurement("CHAN1","NORMal","ASCii")
print(data)
print(type(data))
print(len(data))
t = np.arange(0, len(data))
fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.plot([data], [len(data)])  # Plot some data on the Axes.
plt.show()

