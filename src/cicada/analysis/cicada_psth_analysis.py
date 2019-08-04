from cicada.analysis.cicada_analysis import CicadaAnalysis


class CicadaPsthAnalysis(CicadaAnalysis):
    def __init__(self):
        """
        A list of
        :param data_to_analyse: list of data_structure
        :param family_id: family_id indicated to which family of analysis this class belongs. If None, then
        the analysis is a family in its own.
        :param data_format: indicate the type of data structure. for NWB, NIX
        """
        super().__init__(name="PSTH",
                         short_description="Build PSTH")

    def check_data(self):
        """
        Check the data given one initiating the class and return True if the data given allows the analysis
        implemented, False otherwise.
        :return: a boolean
        """
        if self._data_format != "nwb":

            # non NWB format compatibility not yet implemented
            return False

        for data in self._data_to_analyse:
            # check is there is at least one processing module
            if len(data.processing) == 0:
                return False

            # in our case, we will use 'ophys' module
            if "ophys" not in data.processing:
                return False
        return True

    def set_arguments_for_gui(self):
        """

        Returns:

        """
        range_arg = {"arg_name": "psth_range", "value_type": "int", "min_value": 50, "max_value": 2000,
                     "default_value": 500, "description": "range of the PSTH"}
        self.add_argument_for_gui(**range_arg)

    def update_original_data(self):
        """
        To be called if the data to analyse should be updated after the analysis has been run.
        :return: boolean: return True if the data has been modified
        """
        pass

    def run_analysis(self, **kwargs):
        """
        test
        :param kwargs:
        :return:
        """

        for data in self._data_to_analyse:
            print(f"PSTH ----- {data.identifier} on range {kwargs['psth_range']}")
