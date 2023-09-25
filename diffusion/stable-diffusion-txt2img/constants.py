import numpy as np

alphas_cumprod = np.array([
    0.9991, 0.9983, 0.9974, 0.9966, 0.9957, 0.9948, 0.9940, 0.9931, 0.9922,
    0.9913, 0.9904, 0.9895, 0.9886, 0.9877, 0.9868, 0.9859, 0.9850, 0.9841,
    0.9832, 0.9822, 0.9813, 0.9804, 0.9794, 0.9785, 0.9776, 0.9766, 0.9757,
    0.9747, 0.9737, 0.9728, 0.9718, 0.9708, 0.9698, 0.9689, 0.9679, 0.9669,
    0.9659, 0.9649, 0.9639, 0.9629, 0.9619, 0.9609, 0.9599, 0.9588, 0.9578,
    0.9568, 0.9557, 0.9547, 0.9537, 0.9526, 0.9516, 0.9505, 0.9495, 0.9484,
    0.9473, 0.9463, 0.9452, 0.9441, 0.9430, 0.9420, 0.9409, 0.9398, 0.9387,
    0.9376, 0.9365, 0.9354, 0.9343, 0.9332, 0.9320, 0.9309, 0.9298, 0.9287,
    0.9275, 0.9264, 0.9252, 0.9241, 0.9229, 0.9218, 0.9206, 0.9195, 0.9183,
    0.9171, 0.9160, 0.9148, 0.9136, 0.9124, 0.9112, 0.9100, 0.9089, 0.9077,
    0.9065, 0.9052, 0.9040, 0.9028, 0.9016, 0.9004, 0.8992, 0.8979, 0.8967,
    0.8955, 0.8942, 0.8930, 0.8917, 0.8905, 0.8892, 0.8880, 0.8867, 0.8854,
    0.8842, 0.8829, 0.8816, 0.8804, 0.8791, 0.8778, 0.8765, 0.8752, 0.8739,
    0.8726, 0.8713, 0.8700, 0.8687, 0.8674, 0.8661, 0.8647, 0.8634, 0.8621,
    0.8607, 0.8594, 0.8581, 0.8567, 0.8554, 0.8540, 0.8527, 0.8513, 0.8500,
    0.8486, 0.8473, 0.8459, 0.8445, 0.8431, 0.8418, 0.8404, 0.8390, 0.8376,
    0.8362, 0.8348, 0.8334, 0.8320, 0.8306, 0.8292, 0.8278, 0.8264, 0.8250,
    0.8236, 0.8221, 0.8207, 0.8193, 0.8179, 0.8164, 0.8150, 0.8136, 0.8121,
    0.8107, 0.8092, 0.8078, 0.8063, 0.8049, 0.8034, 0.8019, 0.8005, 0.7990,
    0.7975, 0.7960, 0.7946, 0.7931, 0.7916, 0.7901, 0.7886, 0.7871, 0.7856,
    0.7842, 0.7827, 0.7812, 0.7796, 0.7781, 0.7766, 0.7751, 0.7736, 0.7721,
    0.7706, 0.7690, 0.7675, 0.7660, 0.7645, 0.7629, 0.7614, 0.7599, 0.7583,
    0.7568, 0.7552, 0.7537, 0.7521, 0.7506, 0.7490, 0.7475, 0.7459, 0.7444,
    0.7428, 0.7412, 0.7397, 0.7381, 0.7365, 0.7350, 0.7334, 0.7318, 0.7302,
    0.7286, 0.7271, 0.7255, 0.7239, 0.7223, 0.7207, 0.7191, 0.7175, 0.7159,
    0.7143, 0.7127, 0.7111, 0.7095, 0.7079, 0.7063, 0.7047, 0.7031, 0.7015,
    0.6999, 0.6982, 0.6966, 0.6950, 0.6934, 0.6918, 0.6901, 0.6885, 0.6869,
    0.6852, 0.6836, 0.6820, 0.6803, 0.6787, 0.6771, 0.6754, 0.6738, 0.6722,
    0.6705, 0.6689, 0.6672, 0.6656, 0.6639, 0.6623, 0.6606, 0.6590, 0.6573,
    0.6557, 0.6540, 0.6524, 0.6507, 0.6490, 0.6474, 0.6457, 0.6441, 0.6424,
    0.6407, 0.6391, 0.6374, 0.6357, 0.6341, 0.6324, 0.6307, 0.6291, 0.6274,
    0.6257, 0.6241, 0.6224, 0.6207, 0.6190, 0.6174, 0.6157, 0.6140, 0.6123,
    0.6107, 0.6090, 0.6073, 0.6056, 0.6039, 0.6023, 0.6006, 0.5989, 0.5972,
    0.5955, 0.5939, 0.5922, 0.5905, 0.5888, 0.5871, 0.5855, 0.5838, 0.5821,
    0.5804, 0.5787, 0.5770, 0.5754, 0.5737, 0.5720, 0.5703, 0.5686, 0.5669,
    0.5652, 0.5636, 0.5619, 0.5602, 0.5585, 0.5568, 0.5551, 0.5535, 0.5518,
    0.5501, 0.5484, 0.5467, 0.5450, 0.5434, 0.5417, 0.5400, 0.5383, 0.5366,
    0.5350, 0.5333, 0.5316, 0.5299, 0.5282, 0.5266, 0.5249, 0.5232, 0.5215,
    0.5199, 0.5182, 0.5165, 0.5148, 0.5132, 0.5115, 0.5098, 0.5082, 0.5065,
    0.5048, 0.5032, 0.5015, 0.4998, 0.4982, 0.4965, 0.4948, 0.4932, 0.4915,
    0.4898, 0.4882, 0.4865, 0.4849, 0.4832, 0.4816, 0.4799, 0.4782, 0.4766,
    0.4749, 0.4733, 0.4716, 0.4700, 0.4684, 0.4667, 0.4651, 0.4634, 0.4618,
    0.4601, 0.4585, 0.4569, 0.4552, 0.4536, 0.4520, 0.4503, 0.4487, 0.4471,
    0.4455, 0.4438, 0.4422, 0.4406, 0.4390, 0.4374, 0.4357, 0.4341, 0.4325,
    0.4309, 0.4293, 0.4277, 0.4261, 0.4245, 0.4229, 0.4213, 0.4197, 0.4181,
    0.4165, 0.4149, 0.4133, 0.4117, 0.4101, 0.4086, 0.4070, 0.4054, 0.4038,
    0.4022, 0.4007, 0.3991, 0.3975, 0.3960, 0.3944, 0.3928, 0.3913, 0.3897,
    0.3882, 0.3866, 0.3850, 0.3835, 0.3819, 0.3804, 0.3789, 0.3773, 0.3758,
    0.3742, 0.3727, 0.3712, 0.3697, 0.3681, 0.3666, 0.3651, 0.3636, 0.3621,
    0.3605, 0.3590, 0.3575, 0.3560, 0.3545, 0.3530, 0.3515, 0.3500, 0.3485,
    0.3470, 0.3456, 0.3441, 0.3426, 0.3411, 0.3396, 0.3382, 0.3367, 0.3352,
    0.3338, 0.3323, 0.3308, 0.3294, 0.3279, 0.3265, 0.3250, 0.3236, 0.3222,
    0.3207, 0.3193, 0.3178, 0.3164, 0.3150, 0.3136, 0.3122, 0.3107, 0.3093,
    0.3079, 0.3065, 0.3051, 0.3037, 0.3023, 0.3009, 0.2995, 0.2981, 0.2967,
    0.2954, 0.2940, 0.2926, 0.2912, 0.2899, 0.2885, 0.2871, 0.2858, 0.2844,
    0.2831, 0.2817, 0.2804, 0.2790, 0.2777, 0.2763, 0.2750, 0.2737, 0.2723,
    0.2710, 0.2697, 0.2684, 0.2671, 0.2658, 0.2645, 0.2631, 0.2618, 0.2606,
    0.2593, 0.2580, 0.2567, 0.2554, 0.2541, 0.2528, 0.2516, 0.2503, 0.2490,
    0.2478, 0.2465, 0.2453, 0.2440, 0.2428, 0.2415, 0.2403, 0.2391, 0.2378,
    0.2366, 0.2354, 0.2341, 0.2329, 0.2317, 0.2305, 0.2293, 0.2281, 0.2269,
    0.2257, 0.2245, 0.2233, 0.2221, 0.2209, 0.2198, 0.2186, 0.2174, 0.2163,
    0.2151, 0.2139, 0.2128, 0.2116, 0.2105, 0.2093, 0.2082, 0.2071, 0.2059,
    0.2048, 0.2037, 0.2026, 0.2014, 0.2003, 0.1992, 0.1981, 0.1970, 0.1959,
    0.1948, 0.1937, 0.1926, 0.1915, 0.1905, 0.1894, 0.1883, 0.1872, 0.1862,
    0.1851, 0.1841, 0.1830, 0.1820, 0.1809, 0.1799, 0.1788, 0.1778, 0.1768,
    0.1757, 0.1747, 0.1737, 0.1727, 0.1717, 0.1707, 0.1696, 0.1686, 0.1677,
    0.1667, 0.1657, 0.1647, 0.1637, 0.1627, 0.1618, 0.1608, 0.1598, 0.1589,
    0.1579, 0.1569, 0.1560, 0.1550, 0.1541, 0.1532, 0.1522, 0.1513, 0.1504,
    0.1494, 0.1485, 0.1476, 0.1467, 0.1458, 0.1449, 0.1440, 0.1431, 0.1422,
    0.1413, 0.1404, 0.1395, 0.1386, 0.1378, 0.1369, 0.1360, 0.1352, 0.1343,
    0.1334, 0.1326, 0.1317, 0.1309, 0.1301, 0.1292, 0.1284, 0.1276, 0.1267,
    0.1259, 0.1251, 0.1243, 0.1235, 0.1227, 0.1219, 0.1211, 0.1203, 0.1195,
    0.1187, 0.1179, 0.1171, 0.1163, 0.1155, 0.1148, 0.1140, 0.1132, 0.1125,
    0.1117, 0.1110, 0.1102, 0.1095, 0.1087, 0.1080, 0.1073, 0.1065, 0.1058,
    0.1051, 0.1044, 0.1036, 0.1029, 0.1022, 0.1015, 0.1008, 0.1001, 0.0994,
    0.0987, 0.0980, 0.0973, 0.0967, 0.0960, 0.0953, 0.0946, 0.0940, 0.0933,
    0.0926, 0.0920, 0.0913, 0.0907, 0.0900, 0.0894, 0.0887, 0.0881, 0.0875,
    0.0868, 0.0862, 0.0856, 0.0850, 0.0844, 0.0837, 0.0831, 0.0825, 0.0819,
    0.0813, 0.0807, 0.0801, 0.0795, 0.0789, 0.0784, 0.0778, 0.0772, 0.0766,
    0.0761, 0.0755, 0.0749, 0.0744, 0.0738, 0.0732, 0.0727, 0.0721, 0.0716,
    0.0711, 0.0705, 0.0700, 0.0694, 0.0689, 0.0684, 0.0679, 0.0673, 0.0668,
    0.0663, 0.0658, 0.0653, 0.0648, 0.0643, 0.0638, 0.0633, 0.0628, 0.0623,
    0.0618, 0.0613, 0.0608, 0.0604, 0.0599, 0.0594, 0.0589, 0.0585, 0.0580,
    0.0575, 0.0571, 0.0566, 0.0562, 0.0557, 0.0553, 0.0548, 0.0544, 0.0539,
    0.0535, 0.0531, 0.0526, 0.0522, 0.0518, 0.0514, 0.0509, 0.0505, 0.0501,
    0.0497, 0.0493, 0.0489, 0.0485, 0.0481, 0.0477, 0.0473, 0.0469, 0.0465,
    0.0461, 0.0457, 0.0453, 0.0450, 0.0446, 0.0442, 0.0438, 0.0435, 0.0431,
    0.0427, 0.0424, 0.0420, 0.0416, 0.0413, 0.0409, 0.0406, 0.0402, 0.0399,
    0.0395, 0.0392, 0.0389, 0.0385, 0.0382, 0.0379, 0.0375, 0.0372, 0.0369,
    0.0365, 0.0362, 0.0359, 0.0356, 0.0353, 0.0350, 0.0347, 0.0343, 0.0340,
    0.0337, 0.0334, 0.0331, 0.0328, 0.0325, 0.0323, 0.0320, 0.0317, 0.0314,
    0.0311, 0.0308, 0.0305, 0.0303, 0.0300, 0.0297, 0.0295, 0.0292, 0.0289,
    0.0286, 0.0284, 0.0281, 0.0279, 0.0276, 0.0274, 0.0271, 0.0268, 0.0266,
    0.0264, 0.0261, 0.0259, 0.0256, 0.0254, 0.0251, 0.0249, 0.0247, 0.0244,
    0.0242, 0.0240, 0.0237, 0.0235, 0.0233, 0.0231, 0.0229, 0.0226, 0.0224,
    0.0222, 0.0220, 0.0218, 0.0216, 0.0214, 0.0212, 0.0210, 0.0207, 0.0205,
    0.0203, 0.0201, 0.0200, 0.0198, 0.0196, 0.0194, 0.0192, 0.0190, 0.0188,
    0.0186, 0.0184, 0.0182, 0.0181, 0.0179, 0.0177, 0.0175, 0.0174, 0.0172,
    0.0170, 0.0168, 0.0167, 0.0165, 0.0163, 0.0162, 0.0160, 0.0158, 0.0157,
    0.0155, 0.0154, 0.0152, 0.0151, 0.0149, 0.0147, 0.0146, 0.0144, 0.0143,
    0.0142, 0.0140, 0.0139, 0.0137, 0.0136, 0.0134, 0.0133, 0.0132, 0.0130,
    0.0129, 0.0127, 0.0126, 0.0125, 0.0123, 0.0122, 0.0121, 0.0120, 0.0118,
    0.0117, 0.0116, 0.0115, 0.0113, 0.0112, 0.0111, 0.0110, 0.0109, 0.0107,
    0.0106, 0.0105, 0.0104, 0.0103, 0.0102, 0.0101, 0.0100, 0.0098, 0.0097,
    0.0096, 0.0095, 0.0094, 0.0093, 0.0092, 0.0091, 0.0090, 0.0089, 0.0088,
    0.0087, 0.0086, 0.0085, 0.0084, 0.0083, 0.0082, 0.0082, 0.0081, 0.0080,
    0.0079, 0.0078, 0.0077, 0.0076, 0.0075, 0.0074, 0.0074, 0.0073, 0.0072,
    0.0071, 0.0070, 0.0070, 0.0069, 0.0068, 0.0067, 0.0066, 0.0066, 0.0065,
    0.0064, 0.0063, 0.0063, 0.0062, 0.0061, 0.0061, 0.0060, 0.0059, 0.0058,
    0.0058, 0.0057, 0.0056, 0.0056, 0.0055, 0.0054, 0.0054, 0.0053, 0.0053,
    0.0052, 0.0051, 0.0051, 0.0050, 0.0049, 0.0049, 0.0048, 0.0048, 0.0047,
    0.0047
])

log_sigmas = np.array([
    -3.465247869e+00, -3.262352705e+00, -3.006420135e+00, -2.837683201e+00,
    -2.711531878e+00, -2.610528946e+00, -2.566935062e+00, -2.489443779e+00,
    -2.422124147e+00, -2.362802029e+00, -2.309390783e+00, -2.284866810e+00,
    -2.238821030e+00, -2.196660280e+00, -2.157779932e+00, -2.121440172e+00,
    -2.087811947e+00, -2.056070566e+00, -2.040925026e+00, -2.011517525e+00,
    -1.984147549e+00, -1.958198309e+00, -1.933165073e+00, -1.909325600e+00,
    -1.886571169e+00, -1.864807487e+00, -1.843951702e+00, -1.823931098e+00,
    -1.804399610e+00, -1.785873890e+00, -1.767748117e+00, -1.750256658e+00,
    -1.733356476e+00, -1.717008829e+00, -1.701178789e+00, -1.685834646e+00,
    -1.670516253e+00, -1.656071663e+00, -1.642032743e+00, -1.627981305e+00,
    -1.614699244e+00, -1.601385355e+00, -1.588416934e+00, -1.576133013e+00,
    -1.563795447e+00, -1.545673847e+00, -1.534057021e+00, -1.522703886e+00,
    -1.511602998e+00, -1.500743032e+00, -1.490114093e+00, -1.479412079e+00,
    -1.469222426e+00, -1.453897834e+00, -1.444210291e+00, -1.434437990e+00,
    -1.424853086e+00, -1.415448427e+00, -1.401916742e+00, -1.392930031e+00,
    -1.383858919e+00, -1.375188112e+00, -1.362457633e+00, -1.354147196e+00,
    -1.345972657e+00, -1.337486506e+00, -1.325669765e+00, -1.317518473e+00,
    -1.309916973e+00, -1.302429318e+00, -1.291000366e+00, -1.283390999e+00,
    -1.276287556e+00, -1.265434384e+00, -1.258201718e+00, -1.251072049e+00,
    -1.240747213e+00, -1.234220743e+00, -1.223881721e+00, -1.217221856e+00,
    -1.210649729e+00, -1.201119065e+00, -1.194753885e+00, -1.185192108e+00,
    -1.179025173e+00, -1.172933459e+00, -1.163776278e+00, -1.157866359e+00,
    -1.148978591e+00, -1.142939925e+00, -1.134311318e+00, -1.128737688e+00,
    -1.120061994e+00, -1.114644170e+00, -1.106207609e+00, -1.100661159e+00,
    -1.092726707e+00, -1.087327003e+00, -1.079335332e+00, -1.074077725e+00,
    -1.066293478e+00, -1.061170459e+00, -1.053583026e+00, -1.048588037e+00,
    -1.041187763e+00, -1.036314487e+00, -1.028614521e+00, -1.021502018e+00,
    -1.016816020e+00, -1.009868264e+00, -1.004833817e+00, -9.980494976e-01,
    -9.909129143e-01, -9.865037203e-01, -9.795289040e-01, -9.730771780e-01,
    -9.683983326e-01, -9.620876908e-01, -9.554430842e-01, -9.509256482e-01,
    -9.444267154e-01, -9.380112886e-01, -9.340429306e-01, -9.277585149e-01,
    -9.215520620e-01, -9.173294306e-01, -9.112502933e-01, -9.048712254e-01,
    -8.989408016e-01, -8.949041367e-01, -8.890901208e-01, -8.833428621e-01,
    -8.773080707e-01, -8.734416366e-01, -8.675243855e-01, -8.620184660e-01,
    -8.562340736e-01, -8.505159020e-01, -8.468504548e-01, -8.412380219e-01,
    -8.356878161e-01, -8.301985860e-01, -8.247689605e-01, -8.193976879e-01,
    -8.159526587e-01, -8.106746674e-01, -8.054519296e-01, -7.999807000e-01,
    -7.948679328e-01, -7.895107269e-01, -7.845033407e-01, -7.792554498e-01,
    -7.760753036e-01, -7.709147334e-01, -7.658068538e-01, -7.610301971e-01,
    -7.560217977e-01, -7.510631084e-01, -7.461530566e-01, -7.412908077e-01,
    -7.364753485e-01, -7.314421535e-01, -7.267202139e-01, -7.220424414e-01,
    -7.174080014e-01, -7.125622630e-01, -7.080144882e-01, -7.032585144e-01,
    -6.985473037e-01, -6.941246986e-01, -6.892561316e-01, -6.849145889e-01,
    -6.806104183e-01, -6.758710146e-01, -6.716436744e-01, -6.669880748e-01,
    -6.623755097e-01, -6.582603455e-01, -6.537271738e-01, -6.492347121e-01,
    -6.452258825e-01, -6.408088803e-01, -6.364305019e-01, -6.320902705e-01,
    -6.277872920e-01, -6.235210299e-01, -6.180288196e-01, -6.138446331e-01,
    -6.096953154e-01, -6.055800319e-01, -6.014983058e-01, -5.974497199e-01,
    -5.934336782e-01, -5.890529156e-01, -5.839246511e-01, -5.796260834e-01,
    -5.757501125e-01, -5.715209246e-01, -5.677070618e-01, -5.635449886e-01,
    -5.597913265e-01, -5.545829535e-01, -5.505282879e-01, -5.468706489e-01,
    -5.428779125e-01, -5.389168262e-01, -5.339202881e-01, -5.300292373e-01,
    -5.261682272e-01, -5.223367810e-01, -5.185344815e-01, -5.133956671e-01,
    -5.096604824e-01, -5.059530735e-01, -5.022729635e-01, -4.986196458e-01,
    -4.936805069e-01, -4.897640347e-01, -4.862006307e-01, -4.823421836e-01,
    -4.775604010e-01, -4.740827084e-01, -4.703162014e-01, -4.656476974e-01,
    -4.619439840e-01, -4.582674205e-01, -4.546177685e-01, -4.500928521e-01,
    -4.465022087e-01, -4.429371059e-01, -4.393972456e-01, -4.347161353e-01,
    -4.312338531e-01, -4.274884760e-01, -4.229170978e-01, -4.195156395e-01,
    -4.161373079e-01, -4.113899767e-01, -4.080658257e-01, -4.044894874e-01,
    -3.998509943e-01, -3.966024816e-01, -3.931068480e-01, -3.885723352e-01,
    -3.851322234e-01, -3.817156851e-01, -3.772828281e-01, -3.739192784e-01,
    -3.705782294e-01, -3.659886718e-01, -3.627000451e-01, -3.594328463e-01,
    -3.549440205e-01, -3.517270088e-01, -3.473065495e-01, -3.441381454e-01,
    -3.407483101e-01, -3.364233971e-01, -3.330852687e-01, -3.297693431e-01,
    -3.255379796e-01, -3.222715557e-01, -3.181028962e-01, -3.148844838e-01,
    -3.112315238e-01, -3.071535528e-01, -3.040046096e-01, -2.995403111e-01,
    -2.964388728e-01, -2.933565378e-01, -2.889858782e-01, -2.859489918e-01,
    -2.816422880e-01, -2.786495686e-01, -2.752511203e-01, -2.710352242e-01,
    -2.681051195e-01, -2.639487684e-01, -2.606484890e-01, -2.565534413e-01,
    -2.533013821e-01, -2.500703335e-01, -2.460606843e-01, -2.428760231e-01,
    -2.389234453e-01, -2.357836515e-01, -2.314984798e-01, -2.284048796e-01,
    -2.253303677e-01, -2.211334556e-01, -2.181031257e-01, -2.139662057e-01,
    -2.109789103e-01, -2.069002539e-01, -2.039547861e-01, -2.010264993e-01,
    -1.966660023e-01, -1.937800050e-01, -1.898387074e-01, -1.866369992e-01,
    -1.827514023e-01, -1.795946062e-01, -1.757632047e-01, -1.726501137e-01,
    -1.695562005e-01, -1.654606164e-01, -1.624107808e-01, -1.587083191e-01,
    -1.556993127e-01, -1.513846368e-01, -1.484191865e-01, -1.444924921e-01,
    -1.415675730e-01, -1.386596113e-01, -1.344889253e-01, -1.316217780e-01,
    -1.275091320e-01, -1.246816069e-01, -1.206254438e-01, -1.178364679e-01,
    -1.138351783e-01, -1.107789502e-01, -1.068335325e-01, -1.038196906e-01,
    -1.008238718e-01, -9.695594013e-02, -9.400088340e-02, -9.018516541e-02,
    -8.726972342e-02, -8.321639895e-02, -8.034119755e-02, -7.634346187e-02,
    -7.350736111e-02, -7.040617615e-02, -6.648673862e-02, -6.342861801e-02,
    -5.956332758e-02, -5.682060495e-02, -5.273452029e-02, -4.975913092e-02,
    -4.680131376e-02, -4.306199402e-02, -4.014343768e-02, -3.619085997e-02,
    -3.331203759e-02, -2.941283397e-02, -2.631529793e-02, -2.349255234e-02,
    -1.941506192e-02, -1.663096994e-02, -1.260882989e-02, -9.862258099e-03,
    -5.893995985e-03, -2.938291524e-03, 4.880429187e-04, 3.891040571e-03,
    6.789590232e-03, 1.015012432e-02, 1.348834764e-02, 1.727615669e-02,
    2.056724206e-02, 2.337099425e-02, 2.708495967e-02, 3.031228669e-02,
    3.351897001e-02, 3.715863824e-02, 3.987107426e-02, 4.346502200e-02,
    4.703324661e-02, 5.057620630e-02, 5.321704969e-02, 5.671669170e-02,
    6.019189581e-02, 6.364320964e-02, 6.664356589e-02, 7.005082816e-02,
    7.343488932e-02, 7.637733966e-02, 8.013517410e-02, 8.303847164e-02,
    8.633618802e-02, 9.002013505e-02, 9.286689758e-02, 9.610046446e-02,
    9.971351177e-02, 1.029033288e-01, 1.060729176e-01, 1.096148193e-01,
    1.127422601e-01, 1.158502996e-01, 1.193238348e-01, 1.227734312e-01,
    1.258199066e-01, 1.292252094e-01, 1.326073557e-01, 1.355947107e-01,
    1.393039525e-01, 1.426188648e-01, 1.455471218e-01, 1.491834521e-01,
    1.517133564e-01, 1.556630880e-01, 1.585161239e-01, 1.617065072e-01,
    1.655784398e-01, 1.687241495e-01, 1.718502641e-01, 1.753009111e-01,
    1.787279397e-01, 1.817922741e-01, 1.855123043e-01, 1.878652275e-01,
    1.918732822e-01, 1.948584020e-01, 1.978257447e-01, 2.017550766e-01,
    2.043575346e-01, 2.079139501e-01, 2.111252248e-01, 2.143161148e-01,
    2.178026587e-01, 2.206373066e-01, 2.243919969e-01, 2.274994999e-01,
    2.305878103e-01, 2.342688888e-01, 2.370119691e-01, 2.409478128e-01,
    2.439543903e-01, 2.472408861e-01, 2.502100766e-01, 2.537499368e-01,
    2.572648525e-01, 2.598848939e-01, 2.636454701e-01, 2.668054402e-01,
    2.699456513e-01, 2.730662227e-01, 2.767292559e-01, 2.803656161e-01,
    2.831449807e-01, 2.864598632e-01, 2.894793451e-01, 2.932961881e-01,
    2.965447009e-01, 2.997722626e-01, 3.029791415e-01, 3.061655164e-01,
    3.093318045e-01, 3.124780357e-01, 3.163833320e-01, 3.192279041e-01,
    3.230809867e-01, 3.258878291e-01, 3.294376135e-01, 3.324602842e-01,
    3.359637558e-01, 3.389473557e-01, 3.426519632e-01, 3.455960453e-01,
    3.490090370e-01, 3.519160450e-01, 3.557659090e-01, 3.586339653e-01,
    3.624326885e-01, 3.652628660e-01, 3.690117300e-01, 3.718050122e-01,
    3.750442863e-01, 3.782626987e-01, 3.819156587e-01, 3.850902319e-01,
    3.886938989e-01, 3.918258846e-01, 3.944949508e-01, 3.984719813e-01,
    4.015435576e-01, 4.050308466e-01, 4.084940851e-01, 4.115048945e-01,
    4.149236679e-01, 4.183192849e-01, 4.216919839e-01, 4.246245623e-01,
    4.283699095e-01, 4.316756427e-01, 4.345504045e-01, 4.382224381e-01,
    4.418676496e-01, 4.446845651e-01, 4.478845596e-01, 4.510641694e-01,
    4.546173215e-01, 4.581453800e-01, 4.616487026e-01, 4.647423029e-01,
    4.678168297e-01, 4.716337025e-01, 4.742882252e-01, 4.784313738e-01,
    4.814231098e-01, 4.847676456e-01, 4.880898893e-01, 4.910246134e-01,
    4.946689010e-01, 4.979262948e-01, 5.015208125e-01, 5.047339797e-01,
    5.079265833e-01, 5.114502311e-01, 5.146003962e-01, 5.180774927e-01,
    5.215305686e-01, 5.249599218e-01, 5.283658504e-01, 5.317488313e-01,
    5.351091027e-01, 5.384469032e-01, 5.414320230e-01, 5.453845263e-01,
    5.489805341e-01, 5.519035459e-01, 5.551314354e-01, 5.583386421e-01,
    5.621603131e-01, 5.653228760e-01, 5.687787533e-01, 5.718998313e-01,
    5.756196976e-01, 5.790053010e-01, 5.823682547e-01, 5.860112309e-01,
    5.890269279e-01, 5.923233032e-01, 5.958947539e-01, 5.994408131e-01,
    6.029620171e-01, 6.061680913e-01, 6.093537211e-01, 6.128059626e-01,
    6.165192723e-01, 6.196398139e-01, 6.235834956e-01, 6.266604662e-01,
    6.302725673e-01, 6.335838437e-01, 6.368733048e-01, 6.404126883e-01,
    6.436576843e-01, 6.474171281e-01, 6.506170630e-01, 6.540608406e-01,
    6.572187543e-01, 6.611382365e-01, 6.642519236e-01, 6.678602099e-01,
    6.714426279e-01, 6.747462749e-01, 6.780282855e-01, 6.820383668e-01,
    6.852729917e-01, 6.889794469e-01, 6.921696663e-01, 6.955826283e-01,
    6.989725232e-01, 7.023394704e-01, 7.061598897e-01, 7.094790936e-01,
    7.127763629e-01, 7.165181637e-01, 7.202321291e-01, 7.234594822e-01,
    7.271225452e-01, 7.303057909e-01, 7.339191437e-01, 7.375066280e-01,
    7.410684824e-01, 7.446053028e-01, 7.481171489e-01, 7.511699200e-01,
    7.550677061e-01, 7.589353323e-01, 7.623484135e-01, 7.657381892e-01,
    7.691051960e-01, 7.724497318e-01, 7.761856318e-01, 7.798939943e-01,
    7.831673026e-01, 7.868244052e-01, 7.904549837e-01, 7.936601043e-01,
    7.972414494e-01, 8.015841246e-01, 8.051094413e-01, 8.086099625e-01,
    8.120862246e-01, 8.155385256e-01, 8.189671040e-01, 8.227493763e-01,
    8.265030384e-01, 8.298575878e-01, 8.335585594e-01, 8.372323513e-01,
    8.401519656e-01, 8.441389799e-01, 8.477361202e-01, 8.513075709e-01,
    8.548536897e-01, 8.587256074e-01, 8.622196913e-01, 8.656894565e-01,
    8.694787025e-01, 8.728986979e-01, 8.769719601e-01, 8.803412914e-01,
    8.843547106e-01, 8.876746893e-01, 8.916299343e-01, 8.949022293e-01,
    8.984771967e-01, 9.026693702e-01, 9.058703780e-01, 9.096847773e-01,
    9.131559730e-01, 9.169154167e-01, 9.209563732e-01, 9.246578217e-01,
    9.280269146e-01, 9.319795370e-01, 9.356005192e-01, 9.391955137e-01,
    9.427648187e-01, 9.466030598e-01, 9.504120350e-01, 9.536125660e-01,
    9.573687315e-01, 9.613824487e-01, 9.650808573e-01, 9.690334797e-01,
    9.723967314e-01, 9.765691757e-01, 9.798822403e-01, 9.837200046e-01,
    9.875285625e-01, 9.913083315e-01, 9.950596690e-01, 9.987830520e-01,
    1.002741814e+00, 1.006408691e+00, 1.010048985e+00, 1.013919830e+00,
    1.017506003e+00, 1.021319866e+00, 1.025104880e+00, 1.029110909e+00,
    1.032837629e+00, 1.036536813e+00, 1.040696383e+00, 1.044096112e+00,
    1.047953367e+00, 1.051781178e+00, 1.056052685e+00, 1.059349895e+00,
    1.063557506e+00, 1.066805720e+00, 1.070951462e+00, 1.074607730e+00,
    1.078689337e+00, 1.082737923e+00, 1.086309433e+00, 1.090296984e+00,
    1.094253063e+00, 1.098178029e+00, 1.101641297e+00, 1.105936885e+00,
    1.109771490e+00, 1.113577008e+00, 1.117353916e+00, 1.121102333e+00,
    1.125234485e+00, 1.128924608e+00, 1.132992983e+00, 1.137028456e+00,
    1.140632868e+00, 1.145003200e+00, 1.148943305e+00, 1.152463078e+00,
    1.156731606e+00, 1.160580754e+00, 1.164400458e+00, 1.168568730e+00,
    1.172702551e+00, 1.176431179e+00, 1.180132151e+00, 1.184537411e+00,
    1.188541770e+00, 1.192154527e+00, 1.196098685e+00, 1.200366020e+00,
    1.204246163e+00, 1.208444953e+00, 1.212608695e+00, 1.216738224e+00,
    1.220153451e+00, 1.224221230e+00, 1.228591084e+00, 1.232591033e+00,
    1.236559391e+00, 1.240496397e+00, 1.244726777e+00, 1.248600245e+00,
    1.252444029e+00, 1.256258368e+00, 1.260985732e+00, 1.265047073e+00,
    1.269075632e+00, 1.273072004e+00, 1.277036548e+00, 1.281271338e+00,
    1.285171747e+00, 1.289634705e+00, 1.293470740e+00, 1.297569036e+00,
    1.301923275e+00, 1.305953145e+00, 1.309950948e+00, 1.314198971e+00,
    1.318131566e+00, 1.322588444e+00, 1.326455951e+00, 1.330566645e+00,
    1.334914446e+00, 1.338956594e+00, 1.342966199e+00, 1.347208023e+00,
    1.351414084e+00, 1.355844736e+00, 1.359979033e+00, 1.364079595e+00,
    1.368399739e+00, 1.372432113e+00, 1.376681089e+00, 1.380894184e+00,
    1.385316849e+00, 1.389215469e+00, 1.393565536e+00, 1.397877932e+00,
    1.402153373e+00, 1.406861663e+00, 1.410596490e+00, 1.415226102e+00,
    1.419356465e+00, 1.423452973e+00, 1.427965641e+00, 1.431992531e+00,
    1.436429024e+00, 1.440826654e+00, 1.445185781e+00, 1.449507356e+00,
    1.453791976e+00, 1.458039999e+00, 1.462671757e+00, 1.466429591e+00,
    1.470984340e+00, 1.475089550e+00, 1.479971528e+00, 1.484003901e+00,
    1.488402128e+00, 1.493156433e+00, 1.497084260e+00, 1.501757145e+00,
    1.506002665e+00, 1.510212541e+00, 1.514764786e+00, 1.519276142e+00,
    1.523376107e+00, 1.528178453e+00, 1.532570839e+00, 1.537286162e+00,
    1.541241646e+00, 1.545876145e+00, 1.550116539e+00, 1.554669976e+00,
    1.559182286e+00, 1.563654304e+00, 1.568426013e+00, 1.572480083e+00,
    1.577168584e+00, 1.581483364e+00, 1.586088657e+00, 1.590327263e+00,
    1.594852209e+00, 1.599655271e+00, 1.604097009e+00, 1.608812451e+00,
    1.613484025e+00, 1.617805004e+00, 1.622089028e+00, 1.626940489e+00,
    1.631446362e+00, 1.635615587e+00, 1.640631795e+00, 1.644725442e+00,
    1.649651527e+00, 1.654243946e+00, 1.658794641e+00, 1.663304210e+00,
    1.668051600e+00, 1.672478914e+00, 1.677140236e+00, 1.682029009e+00,
    1.686602473e+00, 1.691400051e+00, 1.695626140e+00, 1.700598717e+00,
    1.705006361e+00, 1.709886909e+00, 1.714467049e+00, 1.719256639e+00,
    1.724249244e+00, 1.728700161e+00, 1.733355999e+00, 1.738210440e+00,
    1.743018150e+00, 1.747780085e+00, 1.752497077e+00, 1.757169962e+00,
    1.761799693e+00, 1.766843319e+00, 1.771384597e+00, 1.776332974e+00,
    1.780789375e+00, 1.785645962e+00, 1.790455699e+00, 1.795219660e+00,
    1.799938679e+00, 1.804613590e+00, 1.809664249e+00, 1.814249516e+00,
    1.819204092e+00, 1.824110031e+00, 1.828565359e+00, 1.833780050e+00,
    1.838545799e+00, 1.843657851e+00, 1.848330855e+00, 1.853344321e+00,
    1.858308077e+00, 1.862846732e+00, 1.867717505e+00, 1.872910380e+00,
    1.877684593e+00, 1.882413626e+00, 1.887815237e+00, 1.892804503e+00,
    1.897393346e+00, 1.902288437e+00, 1.907136202e+00, 1.912278533e+00,
    1.917368412e+00, 1.922072768e+00, 1.927064538e+00, 1.932334661e+00,
    1.937225461e+00, 1.942390203e+00, 1.947184086e+00, 1.952247381e+00,
    1.957260013e+00, 1.962222815e+00, 1.967442393e+00, 1.972002983e+00,
    1.977720737e+00, 1.982485652e+00, 1.987498879e+00, 1.992752910e+00,
    1.997664809e+00, 2.002813578e+00, 2.007909775e+00, 2.012954712e+00,
    2.017673016e+00, 2.023440838e+00, 2.028332233e+00, 2.033443928e+00,
    2.038503885e+00, 2.043513060e+00, 2.048991919e+00, 2.054154634e+00,
    2.059264421e+00, 2.064322710e+00, 2.069579363e+00, 2.074781179e+00,
    2.080417156e+00, 2.085266829e+00, 2.090547800e+00, 2.095773458e+00,
    2.100944996e+00, 2.106063843e+00, 2.111130714e+00, 2.116600275e+00,
    2.122010469e+00, 2.126919031e+00, 2.132219553e+00, 2.137464285e+00,
    2.143084764e+00, 2.148217440e+00, 2.153718948e+00, 2.158744097e+00,
    2.164131641e+00, 2.169869423e+00, 2.174735546e+00, 2.180353642e+00,
    2.185514450e+00, 2.191013336e+00, 2.196452379e+00, 2.201833010e+00,
    2.207156181e+00, 2.212423325e+00, 2.217635632e+00, 2.223160505e+00,
    2.228987217e+00, 2.234030485e+00, 2.239732504e+00, 2.245019913e+00,
    2.250598907e+00, 2.256116152e+00, 2.261233807e+00, 2.266635656e+00,
    2.272311926e+00, 2.277924299e+00, 2.283474445e+00, 2.288642406e+00,
    2.294393301e+00, 2.299764633e+00, 2.305389643e+00, 2.310644627e+00,
    2.316149473e+00, 2.321894884e+00, 2.327574968e+00, 2.332897425e+00,
    2.338745356e+00, 2.344238520e+00, 2.349956036e+00, 2.355327845e+00,
    2.360920668e+00, 2.366726637e+00, 2.372466087e+00, 2.377871513e+00,
    2.383750677e+00, 2.389298916e+00, 2.394786596e+00, 2.400471210e+00,
    2.406092167e+00, 2.411901951e+00, 2.417644739e+00, 2.423076868e+00,
    2.428936243e+00, 2.434247732e+00, 2.440453053e+00, 2.446113586e+00,
    2.451710701e+00, 2.457704306e+00, 2.463173866e+00, 2.469032288e+00,
    2.475265741e+00, 2.480985165e+00, 2.486207008e+00, 2.492231369e+00,
    2.497760773e+00, 2.503648281e+00, 2.509880066e+00, 2.515627384e+00,
    2.521309137e+00, 2.527326107e+00, 2.532877445e+00, 2.538757324e+00,
    2.544569254e+00, 2.550694942e+00, 2.556746244e+00, 2.562353849e+00,
    2.568266869e+00, 2.574110508e+00, 2.580245495e+00, 2.585951805e+00,
    2.592294216e+00, 2.598211527e+00, 2.604059696e+00, 2.609839916e+00,
    2.615554333e+00, 2.621864557e+00, 2.627770185e+00, 2.633606911e+00,
    2.639694691e+00, 2.645709276e+00, 2.651963234e+00, 2.657833099e+00,
    2.663634539e+00, 2.669969559e+00, 2.675929070e+00, 2.681818485e+00
])
