# pymedex

Python wrapper for this [MedEx](https://sbmi.uth.edu/ccb/resources/medex.htm) implementation by the University of Texas.

## Example Usage

To run MedEx with an input directory and an output directory,

the input/output directories *must* be absolute URLs since MedEx will run within its working directory ("~/Medex_UIMA_1.3.7" in this example).

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

