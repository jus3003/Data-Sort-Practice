# 2022Fall_assignment1
Hi, this is TA testing

## Problem sets
Please refer to the Google doc: [LINK][link1]

[link1]: https://docs.google.com/document/d/1TEtpCfENPWmX8ZjUBchjg9efbcljBJ78GsxSulRpuN8/edit

09/13 update:
You should not use any packages except those imported at the top of the file and those used in the Wordcloud problem. In fact, you won't need random. It just got left in the supplied code. [2022 09 13]


## Files
- `assignment1.py` : This is an empty framework of the code template.

  1. Do not change the name of the functions given
  2. You will need to complete the 4 functions as specified inside

- `test_assignment1.py` : A test script written with pytest. It is not necessary to run these tests to earn full credit on this assignment, but it is for your benefit as they are similar to how you will be graded.
  - The way to specify file path depends on OS: L12, 13 provides the format for linux/MacOS, and Windows (just leave the right path format for your python running OS)

    ```python

    path  = os.getcwd() + '/' + 'assignment1.py' #linux, mac user
    # path  = os.getcwd() + '\\' + 'assignment1.py' #windows user

    ```

- `integers.txt` : This is the testing input file for Q1

- `scifibookfavorites.txt` : This is the raw input file for Q2

- `example*.txt` : The file name starts with example is  used for the reference of the expected output for pytest testing


## Reminders
- For Q1, Q2, the answer will be examined by your stdout (i.e. `print`). Hence, **you must print the proper format** as the problem requires to pass the grading scripts.

- For Q3 (Word cloud), please remember to upload your final pictures to your repo. The testing script does not examine this problem.

- For Q4 (Calculator), **must implement an exit function** by entering `q`, otherwirse, the function doesn't have an endding point, which might affect the testing and the grading script.

- For the testing script, a `pytest` package can be installed by
  - Conda user:
  ```shell
  conda install -c anaconda pytest
  ```

  - PIP user:
  ```shell
  pip install pytest
  ```

- Execpt Q3 (Word cloud), you can NOT use the external packages (e.g. `pandas`, `numpy`) to do data processing for all the other problems (Q1, Q2, Q4).
