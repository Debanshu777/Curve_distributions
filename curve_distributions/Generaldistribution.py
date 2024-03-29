
class Distribution:

    def __init__(self, mu:int=0, sigma:int=1) -> None:
        """ Generic distribution class for calculating and
        visualizing a probability distribution.

        Attributes:
            mean (float) representing the mean value of the distribution
            stdev (float) representing the standard deviation of the distribution
            data_list (list of floats) a list of floats extracted from the data file
            """

        self.mean:int = mu
        self.stdev:int = sigma
        self.data:list = []

    def read_data_file(self, file_name:str) -> None:
        """Function to read in data from a txt file. The txt file should have
        one number (float) per line. The numbers are stored in the data attribute.

        Args:
            file_name (string): name of a file to read from

        Returns:
            None

        """

        with open(file_name) as file:
            data_list:list = []
            line = file.readline()
            while line:
                data_list.append(int(line))
                line = file.readline()
        file.close()

        self.data:list = data_list
