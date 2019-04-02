import os
import re

from utils import sys_url
import platform

class MedEx:

    def __init__(self, medex_home):
        """
        Helper class for running MedEx.
        :param medex_home: The url to the home directory of MedEx e.g. "~/Medex_UIMA_1.3.7"
        """
        self.medex_home = sys_url(medex_home)
        self.libs = "lib/*"
        self.app = "bin"
        self.main_class = "org.apache.medex.Main"

    def parse(self, input_dir, output_dir, params="-b y -f y -d n -p n -t n"):
        """
        Runs MedEx with the input director provided and outputs to the output directory provided.
        :param input_dir: The url to the input directory.
        :param output_dir: The url to the output directory.
        :return: The exit code of the MedEx execution.
        """
        input_dir = sys_url(input_dir)
        output_dir = sys_url(output_dir)
        print("Running medex with input", input_dir, "and output", output_dir)
        # ensure input exists before running MedEx
        if not os.path.exists(input_dir):
            raise Exception(f"Input directory '{input_dir}' does not exist.")

        # create output directory
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)

        # the working directory needs to be within MEDEX_HOME for MedEx to work properly.
        current_dir = os.getcwd()
        os.chdir(self.medex_home)

        class_path_separator = ';' if platform.system().lower().startswith("windows") else ":"
        command = f"java -Xmx1024m -cp {self.libs}{class_path_separator}{self.app} {self.main_class} -i \"{input_dir}\" -o \"{output_dir}\" {params}"
        exitcode = os.system(command)
        os.chdir(current_dir)

        return exitcode


    def build_medex_obj(self, input_file, remove_indices=True):
        """
            This function parses a MedEx output file into an object slightly more friendly to work with. The output is a
            list where each index is mapped to a line from the file. Each line is split into a list of all of the data.

            Each MedEx line is in the foll:
                0  - Sentence index (start from 1)

                1  - Sentence text

                2  - Drug name      (e.g. 'simvastatin[0, 11]')

                3  - Brand name     (e.g. 'zocor[12, 17]')

                4  - Drug form      (e.g. 'tablet[19, 25]')

                5  - Strength       (e.g. '10mg[20, 24]')

                6  - Dose amount    (e.g. '2 tablets[2, 11]')

                7  - Route          (e.g. 'by mouth[10, 18]')

                8  - Frequency      (normalized frequency) (e.g. 'b.i.d.(R1P12H)[10, 16]', 'R1P12H' is the TIMEX3 format
                                    of 'b.i.d.')

                9  - Duration       (e.g. 'for 10 days[10, 21]')

                10 - Neccessity     (e.g. 'prn[10, 13]')

                11 - UMLS CUI

                12 - RXNORM RxCUI

                13 - RXNORM RxCUI for generic name

                14 - Generic name   (associated with RXCUI code) e.g. 'calcium[3897,3904]' -> 'calcium'
            :param input_file: The url to the input file.
            :param remove_indices: True if the indices for a piece of data should be removed.
            :return: A list of each line parsed into a list.
        """
        output = []
        input_file = sys_url(input_file)

        if not os.path.exists(input_file) or not os.path.isfile(input_file):
            raise Exception(f"Input file '{input_file}' does not exist.")

        with open(input_file, 'r') as fhandle:
            lines = fhandle.read().split("\n")
            for line in lines:
                if line:
                    # first capture group is the sentence index, second capture group is the data separated by the '|'
                    # character.
                    matcher = re.search("^(\d+)[\t|](.+)$", line)

                    if matcher:
                        line_output = []

                        # append index
                        line_output.append(matcher.group(1))

                        data = matcher.group(2).split('|')

                        # append sentence
                        line_output.append(data.pop(0))

                        # remove the index
                        for d in data:
                            matcher = re.search("\[\d+,\d+\]", d)
                            if remove_indices and matcher:
                                line_output.append(d[:matcher.start()])
                            else:
                                line_output.append(d)

                        output.append(line_output)
        return output
