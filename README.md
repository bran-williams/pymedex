# pymedex

Python wrapper for the [MedEx](https://sbmi.uth.edu/ccb/resources/medex.htm) implementation 
by the University of Texas. This wrapper was written for a project at the University of Iowa,
but since no other python wrappers seem to be available, I have decided to upload this here. 

This program essentially runs MedEx as any regular Java application.

## Example Usage

Running MedEx on some input directory with some output directory.

These input/output directorys *must* be absolute URLs since MedEx requires the working directory to be the same as the URL provided to the MedEx constructor.

If they are not absolute URLs, the program will find the input/output directories within its working directory.
```python
from medex.medex import MedEx
from medex.utils import sys_url


# Create a medex object with a path to the location of the MedEx installation.
m = MedEx(sys_url("~/Medex_UIMA_1.3.7"))

# Run the application with an absolute URL to the input directory and output directory.
# Note that 'sys_url' is not necessary, it simply expands the user symbols and formats
# the URL to the system preferred.
m.parse(sys_url("url/to/input_dir"), sys_url("url/to/output_dir"))
```

Extracting MedEx output for analysis.
```python
from medex.medex import build_medex_obj
from medex.utils import sys_url


parsed = build_medex_obj(sys_url("output/test.txt"))

for line in parsed:
    print(line)
```

## Authors

* **Brandon Williams**

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details

