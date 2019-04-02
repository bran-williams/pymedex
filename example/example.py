from medex.medex import MedEx, build_medex_obj
import os


input_folder = os.path.join(os.getcwd(), "input")
output_folder = os.path.join(os.getcwd(), "output")


def test_parsing(medex_url):
    m = MedEx(medex_url)
    m.parse(input_folder, output_folder)


def test_building():
    parsed = build_medex_obj(os.path.join(output_folder, "test.txt"))

    for line in parsed:
        print(line)