# Class to define common group structures

class Groups:

####################################################################

	def __init__(self):

		self.GroupStructures = {}

####################################################################

	def CASMO(self):

		print("Using the CASMO group structures")

		two_group = [0.0, 0.625, 2e7]

		three_group = [0.0, 0.625, 8.21e5, 2e7]

		four_group = [0.0, 0.625, 5.53e3, 8.21e5, 2e7]

		seven_group = [0.0, 5.8e-2, 0.14, 0.625, 4.0, 5.53e3, 8.21e5, 2e7]

		eight_group = [0.0, 5.8e-2, 0.14, 0.28, 0.625, 4.0, 5.53e3, 8.21e5, 2e7]

		nine_group = [0.0, 5.8e-2, 0.14, 0.625, 0.972, 1.15, 4.0, 5.53e3, 8.21e5, 2e7]

		twelve_group = [0.0, 3.e-2, 5.8e-2, 0.14, 0.28, 0.35, 0.625, 4.0, 4.8052e1, 5.53e3, 8.21e5, 2.231e6, 2e7]

		fourteen_group = [0.0, 3.e-2, 5.8e-2, 0.14, 0.28, 0.35, 0.625, 0.972, 1.15, 4.0, 4.8052e1, 5.53e3, 8.21e5, 2.231e6, 2e7]

		sixteen_group = [0.0, 3.e-2, 5.8e-2, 0.14, 0.28, 0.35, 0.625, 0.972, 1.02, 1.097, 1.15, 1.3, 4.0, 5.53e3, 8.21e5, 2.231e6, 2e7]

		eighteen_group = [0.0, 5.8e-2, 0.14, 0.28, 0.625, 0.972, 1.15, 1.855, 4.0, 9.877, 5.53e3, 9.118e3, 1.11e5, 5.e5, 8.21e5, 2.231e6, 2e7]

		twentythree_group = [0.0, 3.e-2, 5.8e-2, 0.14, 0.28, 0.35, 0.625, 1.02, 1.097, 1.855, 4.0, 9.877, 1.5968e1, 1.48728e2, 5.53e3, 9.118e3, 1.11e5, 5.e5, 8.21e5, 1.353e6, 2.231e6, 3.679e6, 6.0655e6, 2e7]

		twentyfive_group = [0.0, 3.e-2, 5.8e-2, 0.14, 0.28, 0.35, 0.625, 0.972, 1.02, 1.097, 1.15, 1.855, 4.0, 9.877, 1.5968e1, 1.48728e2, 5.53e3, 9.118e3, 1.11e5, 5.e5, 8.21e5, 1.353e6, 2.231e6, 3.679e6, 6.0655e6, 2e7]

		forty_group = [0.0, 1.5e-5, 3e-2, 4.2e-2, 5.8e-2, 8e-2, 
		1e-1, 1.4e-1, 1.8e-1, 2.2e-1, 2.8e-1, 3.5e-1, 0.625, 8.5e-1, 9.5e-1, 9.72e-1, \
		1.02, 1.097, 1.15, 1.3, 1.5, 1.855, 2.1, 2.6, 3.3, 4., 9.877, \
		1.5968e1, 2.77e1, 4.8052e1, 1.48728e2, 5.53e3, 9.118e3, 1.11e5, 5.e5, 8.21e5, \
		1.353e6, 2.231e6, 3.679e6, 6.0655e6, 2e7]

		seventy_group = [0.0, 1.5e-5, 5e-3, 1e-2, 1.5e-2, 2e-2, 2.5e-2, 3e-2, 3.5e-2, 4.2e-2, 5e-2, 5.8e-2, 6.7e-2, 8e-2, \
		1e-1, 1.4e-1, 1.8e-1, 2.2e-1, 2.5e-1, 2.8e-1, 3e-1, 3.2e-1, 3.5e-1, 4e-1, 5e-1, 0.625, 7.8e-1, 8.5e-1, 9.1e-1, 9.5e-1, 9.72e-1, 9.96e-1, \
		1.02, 1.045, 1.071, 1.097, 1.123, 1.15, 1.3, 1.5, 1.855, 2.1, 2.6, 3.3, 4, 9.877, \
		1.5968e1, 2.77e1, 4.8052e1, 7.55014e1, 1.48728e2, 3.67262e2, 9.06898e2, 2.23945e3, 3.5191e3, 5.53e3, 9.118e3, 1.503e4, 2.478e4, 4.085e4, 6.743e4, 1.11e5, 1.83e5, 3.025e5, 5e5, 8.21e5, \
		1.353e6, 2.231e6, 3.679e6, 6.0655e6, 2e7]

		self.GroupStructures = {
		2: two_group,
		3: three_group,
		4: four_group,
		7: seven_group,
		8: eight_group,
		9: nine_group,
		12: twelve_group,
		14: fourteen_group,
		16: sixteen_group,
		18: eighteen_group,
		23: twentythree_group,
		25: twentyfive_group,
		40: forty_group,
		70: seventy_group
		}

####################################################################

	def LANL(self):

		print("Using LANL group structures")

		LANL30 = [0.0, 1.52e-1, 4.14e-1, 1.13, 3.06, 8.32, 2.26e1, 6.14e1,
		1.67e2, 4.54e2, 1.235e3, 3.35e3, 9.12e3, 2.48e4, 6.76e4, 1.84e5, 3.03e5, 5.e5, 8.23e5,
		1.353e6, 1.738e6, 2.232e6, 2.865e6, 3.68e6, 6.07e6, 7.79e6, 1.e7, 1.2e7, 1.35e7, 1.5e7, 2.e7]

		LANL70 = [0.0, 1.0677e1, 6.14e1, 1.01301e2, 1.30073e2, 1.67e2, 2.14454e2, 
		2.75365e2, 3.53575e2, 4.54e2, 5.82947e2, 7.48518e2, 9.61117e2,
		1.08909e3, 1.235e3, 1.58461e3, 1.7956e3, 2.03468e3, 2.3056e3, 2.61259e3, 2.96045e3, 
		3.35e3, 3.80129e3, 4.30743e3, 4.88095e3, 5.53084e3, 6.26727e3, 7.10174e3, 8.04733e3, 9.12e3,
		1.03333e4, 1.17088e4, 1.32678e4, 1.50344e4, 1.70362e4, 1.93045e4, 2.18749e4, 
		2.48e4, 2.80879e4, 3.18278e4, 4.08677e4, 5.24752e4, 6.76e4, 8.6517e4, 
		1.1109e5, 1.42642e5, 1.84e5, 2.35178e5, 3.03e5, 3.87742e5, 4.39369e5, 
		4.8255e5, 5.64161e5, 6.39279e5, 7.24398e5, 8.23e5, 9.30145e5,
		1.05399e6, 1.19433e6, 1.353e6, 1.738e6, 2.232e6, 
		2.865e6, 3.68e6, 4.72367e6, 6.07e6, 7.79e6, 
		1.e7, 1.2875e7, 1.65e7, 2.e7]

		LANL80 = [0.0, 1.52e-1, 4.14e-1, 1.13, 3.06, 8.32, 1.0677e1, 2.26e1, 6.14e1, 
		1.01301e2, 1.30073e2, 1.67e2, 2.14454e2, 
		2.75365e2, 3.53575e2, 4.54e2, 5.82947e2, 7.48518e2, 9.61117e2,
		1.08909e3, 1.235e3, 1.58461e3, 1.7956e3, 2.03468e3, 2.3056e3, 2.61259e3, 2.96045e3, 
		3.35e3, 3.80129e3, 4.30743e3, 4.88095e3, 5.53084e3, 6.26727e3, 7.10174e3, 8.04733e3, 9.12e3,
		1.03333e4, 1.17088e4, 1.32678e4, 1.50344e4, 1.70362e4, 1.93045e4, 2.18749e4, 
		2.48e4, 2.80879e4, 3.18278e4, 4.08677e4, 5.24752e4, 6.76e4, 8.6517e4, 
		1.1109e5, 1.42642e5, 1.84e5, 2.35178e5, 3.03e5, 3.87742e5, 4.39369e5, 
		4.8255e5, 5.e5, 5.64161e5, 6.39279e5, 7.24398e5, 8.23e5, 9.30145e5,
		1.05399e6, 1.19433e6, 1.353e6, 1.738e6, 2.232e6, 
		2.865e6, 3.68e6, 4.72367e6, 6.07e6, 7.79e6, 
		1.e7, 1.2e7, 1.2875e7, 1.35e7, 1.5e7, 1.65e7, 2.e7]


		self.GroupStructures = {
		30: LANL30,
		70: LANL70,
		80: LANL80
		}

####################################################################

	def XMAS(self):

		print("Using XMAS group structure and constituent WIMS-69 (for thermal systems) and APOLLO-99 (for fast systems)")

		WIMS_69 = [0.0, 5.e-3,
		1.e-2, 1.5e-2, 2.e-2, 2.5e-2, 3.e-2, 3.5e-2, 4.2e-2, 5.e-2, 5.8e-2, 6.7e-2, 8.e-2,
		1.00001e-1, 1.4e-1, 1.8e-1, 2.2e-1, 2.48e-1, 2.8e-1, 3.e-1, 
		3.2e-1, 3.5e-1, 4.e-1, 5.e-1, 6.25e-1, 7.8e-1, 8.5e-1,
		9.1e-1, 9.5e-1, 9.72e-1, 9.96e-1, 
		1.02, 1.045, 1.071, 1.097, 1.12535, 1.15, 1.3, 
		1.5, 2.1, 2.6, 3.3, 4.0, 9.90555,
		1.59283e1, 2.76077e1, 4.82516e1, 7.56736e1,
		1.48625e2, 3.71703e2, 9.14242e2,
		1.43382e3, 2.24867e3, 3.52662e3, 5.53084e3, 9.11882e3,
		1.50344e4, 2.47875e4, 4.08677e4, 6.73795e4,
		1.1109e5, 1.83156e5, 3.01974e5, 4.97871e5, 8.2085e5,
		1.35335e6, 2.2313e6, 3.67879e6, 6.06531e6, 2.e7]

		APOLLO_104 = [0.0, 3.e-3, 6.9e-3, 
		7.7e-2, 9.5e-2,
		1.15e-1, 1.34e-1, 1.6e-1, 1.89e-1, 3.145e-1, 
		3.91e-1, 4.33e-1, 4.85e-1, 5.4e-1, 7.05e-1, 7.9e-1,
		8.6e-1, 9.3e-1, 9.86e-1,
		1.035, 1.11, 1.17, 1.235, 1.3375, 1.37, 1.44498, 1.475, 
		1.59, 1.67, 1.755, 1.84, 1.93, 2.02, 2.13, 2.36, 2.55, 2.72, 2.76792, 3.38075,
		4.12925, 5.04348, 5.34643, 6.16012, 7.52398, 8.315298, 9.18981,
		1.12245e1, 1.37096e1, 1.94548e1, 2.26033e1, 2.49805e1, 3.05113e1, 
		3.37201e1, 3.72665e1, 4.0169e1, 4.55174e1, 5.1578e1, 5.55951e1, 6.79041e1, 9.16609e1,
		1.36742e2, 2.03995e2, 3.04325e2, 4.53999e2, 6.77287e2, 7.48518e2,
		1.01039e3, 1.2341e3, 1.50733e3, 2.03468e3, 3.35463e3, 5.00451e3, 7.46586e3,
		1.11378e4, 1.66156e4, 2.73944e4, 2.9283e4, 3.69786e4, 5.51656e4, 8.22975e4,
		1.22773e5, 2.47235e5, 2.73237e5, 4.07622e5, 4.50492e5, 5.50232e5, 6.08101e5, 9.0718e5,
		1.00259e6, 1.10803e6, 1.22456e6, 1.65299e6, 2.01897e6, 2.46597e6, 
		3.01194e6, 4.49329e6, 5.48812e6, 6.7032e6, 8.18731e6, 
		1.e7, 1.16183e7, 1.38403e7, 1.49182e7, 1.73325e7, 2.e7]

		XMAS_172 = [0.0, 3.e-3, 5.e-3, 6.9e-3, 
		1.e-2, 1.5e-2, 2.e-2, 2.5e-2, 3.e-2, 3.5e-2, 4.2e-2, 5.e-2, 5.8e-2, 6.7e-2, 7.7e-2, 8.e-2, 9.5e-2,
		1.00001e-1, 1.15e-1, 1.34e-1, 1.4e-1, 1.6e-1, 1.8e-1, 1.89e-1, 2.2e-1, 2.48e-1, 2.8e-1, 3.e-1, 3.145e-1, 
		3.2e-1, 3.5e-1, 3.91e-1, 4.e-1, 4.33e-1, 4.85e-1, 5.e-1, 5.4e-1, 6.25e-1, 7.05e-1, 7.8e-1, 7.9e-1, 8.5e-1,
		8.6e-1, 9.1e-1, 9.3e-1, 9.5e-1, 9.72e-1, 9.86e-1, 9.96e-1, 
		1.02, 1.035, 1.045, 1.071, 1.097, 1.11, 1.12535, 1.15, 1.17, 1.235, 1.3, 1.3375, 1.37, 1.44498, 1.475, 
		1.5, 1.59, 1.67, 1.755, 1.84, 1.93, 2.02, 2.1, 2.13, 2.36, 2.55, 2.6, 2.72, 2.76792, 3.3, 3.38075, 4.0,
		4.12925, 5.04348, 5.34643, 6.16012, 7.52398, 8.315298, 9.18981, 9.90555,
		1.12245e1, 1.37096e1, 1.59283e1, 1.94548e1, 2.26033e1, 2.49805e1, 2.76077e1, 3.05113e1, 
		3.37201e1, 3.72665e1, 4.0169e1, 4.55174e1, 4.82516e1, 5.1578e1, 5.55951e1, 6.79041e1, 7.56736e1, 9.16609e1,
		1.36742e2, 1.48625e2, 2.03995e2, 3.04325e2, 3.71703e2, 4.53999e2, 6.77287e2, 7.48518e2, 9.14242e2,
		1.01039e3, 1.2341e3, 1.43382e3, 1.50733e3, 2.03468e3, 2.24867e3, 3.35463e3, 3.52662e3, 5.00451e3, 5.53084e3, 7.46586e3, 9.11882e3,
		1.11378e4, 1.50344e4, 1.66156e4, 2.47875e4, 2.73944e4, 2.9283e4, 3.69786e4, 4.08677e4, 5.51656e4, 6.73795e4, 8.22975e4,
		1.1109e5, 1.22773e5, 1.83156e5, 2.47235e5, 2.73237e5, 3.01974e5, 4.07622e5, 4.50492e5, 4.97871e5, 5.50232e5, 6.08101e5, 8.2085e5, 9.0718e5,
		1.00259e6, 1.10803e6, 1.22456e6, 1.35335e6, 1.65299e6, 2.01897e6, 2.2313e6, 2.46597e6, 
		3.01194e6, 3.67879e6, 4.49329e6, 5.48812e6, 6.06531e6, 6.7032e6, 8.18731e6, 
		1.e7, 1.16183e7, 1.38403e7, 1.49182e7, 1.73325e7, 2.e7]

		self.GroupStructures = {
		69: WIMS_69,
		104: APOLLO_104,
		172: XMAS_172
		}

####################################################################

	def ANL(self):

		print("Using ANL group structures")

		# NOTE: The energy group structures must all share group edges with the largest group
		# i.e. the smaller group structures must be sub-sets of the largest structure

		four_group = [0.0, 2.2603e1, 1.5846e3, 1.1109e5, 1.4191e7] #Modifed to be subset of 70 groups

		nine_group = [0.0, 5.0435, 4.54e2, 2.0347e3, 9.1188e3, 4.0868e4,
		1.8316e5, 8.2085e5, 2.2313e6, 1.4191e7]

		thirtythree_group = [0.0, 4.1746e-1, 5.3158e-1,
		3.9279, 8.3153,
		1.371e1, 2.2603e1, 3.7267e1, 6.1442e1,
		1.013e2, 1.6702e2, 2.7536e2, 4.54e2, 7.4852e2,
		1.2341e3, 2.0347e3, 3.3546e3, 5.5308e3, 9.1188e3,
		1.5034e4, 2.4787e4, 4.0868e4, 6.7379e4,
		1.1109e5, 1.8316e5,  3.0197e5, 4.9787e5, 8.2085e5,
		1.3534e6, 2.2313e6, 3.6788e6, 6.0653e6,
		1.e7, 1.4191e7]

		seventy_group = [0.0, 4.1746e-1, 5.3158e-1, 6.8256e-1, 8.7642e-1, 
		1.1254, 1.445, 1.8554, 2.3824, 3.059, 3.9279, 5.0435, 6.4759, 8.3153,
		1.0677e1, 1.371e1, 1.7603e1, 2.2603e1, 2.9023e1, 3.7267e1, 4.7851e1, 6.1442e1, 7.8893e1,
		1.013e2, 1.3007e2, 1.6702e2, 2.1445e2, 2.7536e2, 3.5357e2, 4.54e2, 5.8295e2, 7.4852e2, 9.6112e2,
		1.2341e3, 1.5846e3, 2.0347e3, 2.6126e3, 3.3546e3, 4.3074e3, 5.5308e3, 7.1017e3, 9.1188e3,
		1.1709e4, 1.5034e4, 1.9305e4, 2.4787e4, 3.1828e4, 4.0868e4, 5.2475e4, 6.7379e4, 8.6517e4,
		1.1109e5, 1.4264e5, 1.8316e5, 2.3518e5, 3.0197e5, 3.8774e5, 4.9787e5, 6.3928e5, 8.2085e5,
		1.054e6, 1.3534e6, 1.7377e6, 2.2313e6, 2.865e6, 3.6788e6, 4.7237e6, 6.0653e6, 7.788e6,
		1.e7, 1.4191e7]

		self.GroupStructures = {
		4: four_group,
		9: nine_group,
		33: thirtythree_group,
		70: seventy_group
		}

####################################################################

	def CUSTOM(self):

		print("Using custom group structures")

		# NOTE: The energy group structures must all share group edges with the largest group
		# i.e. the smaller group structures must be sub-sets of the largest structure

		two_group = [0.0, 0.625, 2e7]

		three_group = [0.0, 0.625, 8.21e5, 2e7]

		four_group = [0.0, 0.625, 5.53e3, 8.21e5, 2e7]

		self.GroupStructures = {
		2: two_group,
		3: three_group,
		4: four_group
		}

####################################################################
# end class