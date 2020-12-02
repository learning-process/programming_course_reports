![Build application](https://github.com/learning-process/programming_course_reports/workflows/Build%20application/badge.svg?branch=master)

# Programming Course Reports

The following reporting technologies are considered in practice:
  * `LaTeX`

## Rules for submissions
1. You are not supposed to trigger CI jobs by frequent updates of your pull request. First you should test you work locally with all the scripts (code style)
    * Respect others time and don't slow down the job queue
2. Carefully check if the program can hang

## 1. Set up your environment
### Fetch submodules before building the project
```
git submodule update --init --recursive
```

### Reporting technologies
### `LaTeX`
  * **Windows**:

  Run powershell script `scripts/appveyor_install_miktex-latest-minimal.ps1` for install LaTeX and build project.

  * **Linux**:
  ```
  sudo apt install texlive*
  ```
  * **MacOS (apple clang)**:

  Unsupported operating system!

## 2. Build the project with `CMake`
Navigate to a source code folder.

1) Configure the build:

  ```
  mkdir build && cd build
  cmake -D USE_LATEX=ON ..
  ```
*Help on CMake keys:*
- `-D USE_LATEX=ON` enable `LaTeX` reports.

*A corresponding flag can be omitted if it's not needed.*

2) Build the project:
  ```
  cmake --build .
  ```
3) Check the task
  * View report `<project's folder>/build/bin`

## 3. How to submit you work
* There are `task_1`, `task_2`, `task_3`, `task_4` folders in `modules` directory. There are 4 task's reports for the semester. Move to a folder of your task. Make a directory named `<last name>_<first letter of name>_<short task name>`. Example: `task1/nesterov_a_vector_sum`.
* Go into the newly created folder and begin you work on the report. There must be only 2 files and 1 of them must be written by you:
  - `vector_sum.tex` - a LaTeX report file which consider information about your program, name it in the same way as `<short task name>`.
  - `CMakeLists.txt` - a file to configure your project. Examples for each configuration can be found in `test_tasks/test_latex`.
* The number of directories will increase with time. To build only your project, you need to do the following:
  ```
  cmake --build . --target <name task's directory> 
  ```
  Example:
  ```
  cmake --build . --target nesterov_a_vector_sum 
  ```
* Name your pull request in the following way:
  * for report:
  ```
  <Фамилия Имя>. Отчет. <Полное название задачи>.
  Нестеров Александр. Отчет. Сумма элементов вектора.
  ```
* Provide the full task definition in pull request's description.

  Example pull request is located in repo's pull requests.

* Work on your fork-repository. Keep your work on a separate branch and **NOT on `master`!!!**. Name you branch in the same way as your task's folder. To create a branch run:
  ```
  git checkout -b nesterov_a_vector_sum
  ```

*Failing to follow the rules makes the project build red.*

And finally, 

**All information of the course is in WIKI!!!**
