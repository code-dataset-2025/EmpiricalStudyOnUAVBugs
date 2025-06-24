# Assessing the Impact of Hardware Factors on Bug Analysis and Reproduction: An Empirical Study of Bugs in Unmanned Aerial Vehicle Systems

This repository stores our experimental codes and results.

## Dataset

Our dataset is divided into 3 parts:

**Webpage Record**: Since we met a lot of LLM illusion phenomena when we used LLM's web browsing tool to directly access the URL, we converted the web page into a specific markdown document and kept its content unchanged, and then input the document into LLM in the prompt. 

The data is shown in folder`.\Dataset\Webpage Record` .

**S2R Refinement**: We extract S2Rs and other information required to reproduce bugs into specified structured markdown files from ChatGPT-4o. As designed in our prompt, the content of the bug report is extracted into six sections:  (1) ''Environment where the bug occurred''. This section includes hardware environment, software environment, report time, px4 autopilot commit version. (2) ''Steps for bug reproduce(S2Rs)''. This section usually appears in a structured way in bug reports, but there are still a few exceptions. Sometimes S2R lacks some context information, and LLM will help us complete it. (3) ''Observed behavior by the user''. This section describes the bug behavior observed by the bug reporter. It is usually reported in an unstructured manner. (4) ''Expected behavior''. This section records the phenomena that should be observed. (5) ''Additional information provided by the user for bug investigation''. This section records other information provided by the author that is useful for reproducing the bug. (6) ''Communication between developers or other personnel and the user''. This section records the interaction between other developers and the reporter in the comments.

The data is shown in folder`.\Dataset\S2R Refinement` . 

**Metrics Data**: For a deeper analysis of UAV defect bug reports, this step employs software to evaluate them from four perspectives: the author's development experience, the author's experience with PX4, the author's hardware experience, and developer involvement. The four groups of metrics are presented as follows. 

In the category of **the author's development experience**, we employ the following metrics to assess the development experience of report authors:

​	**Author followers (AF)**: The number of followers of the author shows his/her level of recognition by other community users.
​    **Author repositories (AR)**: The number of repositories of the author shows his/her level of activity and development experience.
​    **Author stars (AS)**: The number of stars the author gets, shows the approvals he/she received from other developers.
​    **Author registration time (ART)**: The number of repositories of an author shows his/her development experience.
​    **Total contributions (TC)**: The total contributions of the author on GitHub reflect his/her level of activity in the community.
​    **Real-time contributions (RC)**: The total contributions of the author on GitHub before raising this issue, reflects his/her level of activity and development experience in the community before submitting the bug report.
​    **Real-time current contributions (RCC)**: The author's total contributions on GitHub in one year before raising this issue, reflects his/her more specific level of activity and development experience when submitting bug reports.

In the category of **the author's experience in PX4**, we have the following metrics to measure the development experience of report authors in the PX4 Autopilot repository:
    **Real-time contributions in PX4 (RCP)**: The contributions made by the author in the PX4 repository prior to submitting the bug report reflect their level of activity and development experience on this project at the time of the submission.
    **Total contributions in PX4 (TCP)**: The total contributions of the author in the PX4 repository reflect his/her level of activity and development experience in this project.

In the category of **the author's experience in hardware**, we have the following metrics to measure the report author's familiarity with hardware:

​    **Frequency of hardware (FOH)**: The frequency of the author's raised hardware-related bug reports before this report shows the author's familiarity with the hardware in the PX4 project.
​    **Frequency of same hardware (FOSH)**: The frequency of the author's raised hardware-related bug reports of the same hardware before this report shows the author's familiarity with the same hardware in the bug report.

In the category of **developer involvement**, we have the following metrics to characterize the bug issue:
	**Issue assignees (IA)**: Assignees are personnel responsible for solving problems in specific issues, assigned by users with write access to the repository, usually by project team members who have relevant knowledge. The number of assignees for an issue can, to some extent, indicate the level of attention the project team pays to the issue.
    **Issue participants (IP)**: Participants refer to the total number of users who participate in the discussion of this issue, which can reflect the level of community attention to this issue.
    **Issue comments (IC)**: The number of comments on an issue reflects the level of community attention to it.
    **Issue closed time (ICT)**: The duration of an issue from opening to closing reflects, to some extent, the speed at which the issue is resolved. We believe that for bug issues of the same difficulty to fix, the shorter the closure time, the more attention it receives.

The data is shown in folder`.\Dataset\MetricsData.xlsx` . 


## Source Code

We've tested our code on Windows 11 with Python 3.7.

### Requirements

```
beautifulsoup4==4.12.3
h5py==2.10.0
httpcore==0.17.3
httpx==0.24.1
Markdown==3.4.3
matplotlib==3.1.2
numpy==1.21.6
openai==1.39.0
openpyxl==3.1.3
Pillow==9.5.0
PyGithub==2.3.0
requests==2.28.1
requests-oauthlib==1.3.1
scikit-image==0.19.3
scipy==1.7.3
selenium==4.11.2
webdriver-manager==4.0.2
```

### Run

For recording issue webpage into local file:

```
python .\Code\downloadWeb.py
```

For getting answer from LLM:

```
python .\Code\gpt.py
```

For RQ4:

```
python .\Code\RQ4\MW with cliff'sdelta.py
# or python .\Result\RQ4\MW with cliff'sdelta.py
```

For RQ5:

```
python .\Code\RQ5\MW with cliff'sdelta.py
# or python .\Result\RQ5\MW with cliff'sdelta.py
python .\Code\RQ5\Img.py
# or python .\Result\RQ5\Img.py
```

For RQ7:

```
python .\Code\RQ7\spearman.py
# or python .\Result\RQ7\spearman.py
```

## Results

The `results` folder contains the full results of our experiment. The structure of the folder is shown as below:

```
Result
├─Discussion1
├─Discussion2
│  ├─hardware-compatible
│  ├─hardware-incompatible
│  └─hardware-unrelated
├─RQ1
├─RQ2
├─RQ3
│  └─classification
│      ├─Airframe (not flight controller)
│      ├─Beaglebone Blue
│      ├─CUAV
│      ├─Cube Blue
│      ├─Drotek Pixhwak 3 Pro
│      ├─fmuk66
│      ├─Hex Cude
│      ├─Holybro Pix32
│      ├─Holybro Pixhawk 5X
│      ├─Holybro Pixhwak6C
│      ├─HOLYBRO_KAKUTE F7
│      ├─Matek H743-Slim
│      ├─Mind Racer & Mind PX
│      ├─ModalAI FC-v1
│      ├─MRO Control Zero H7
│      ├─MRO X2.1
│      ├─OmnibusF4SD
│      ├─only FMU version (a hardware design standard)
│      ├─Other Device (not flight controller)
│      ├─Pixhawk 4
│      ├─Pixhawk 4 mini
│      ├─Pixhawk 6X
│      ├─pixhawk1
│      ├─pixhawk2(cube)
│      ├─Pixracer
│      ├─Qualcomm Snapdragon
│      └─Raspberry Pi
├─RQ4
├─RQ5
├─RQ6
│  ├─hardware-compatible
│  │  ├─Executable with divergent bugs
│  │  ├─Executable with identical bugs
│  │  ├─Executable without observed bugs
│  │  ├─Non-executable
│  │  └─Partially executable
│  ├─hardware-incompatible
│  │  ├─Executable with divergent bugs
│  │  ├─Executable with identical bugs
│  │  ├─Executable without observed bugs
│  │  ├─Non-executable
│  │  └─Partially executable
│  └─hardware-unrelated
│      ├─Executable with divergent bugs
│      ├─Executable with identical bugs
│      ├─Executable without observed bugs
│      ├─Non-executable
│      └─Partially executable
└─RQ7
    └─FailedReasonsOfS2Rs
        ├─Compilation or code execution error
        │  ├─hardware-compatible
        │  ├─hardware-incompatible
        │  └─hardware-unrealted
        ├─External software library issues
        │  ├─hardware-compatible
        │  ├─hardware-incompatible
        │  └─hardware-unrealted
        ├─Hardware-incompatible problem
        │  ├─hardware-compatible
        │  ├─hardware-incompatible
        │  └─hardware-unrealted
        ├─Links or files in the report are invalid
        │  ├─hardware-compatible
        │  ├─hardware-incompatible
        │  └─hardware-unrealted
        ├─Others
        │  ├─hardware-compatible
        │  ├─hardware-incompatible
        │  └─hardware-unrealted
        ├─Problems during QGC operation
        │  ├─hardware-compatible
        │  ├─hardware-incompatible
        │  └─hardware-unrealted
        ├─Problems in simulation environment
        │  ├─hardware-compatible
        │  ├─hardware-incompatible
        │  └─hardware-unrealted
        └─Related to real-time flying
            ├─hardware-compatible
            ├─hardware-incompatible
            └─hardware-unrealted
```

 - Any folder corresponds to the result of its corresponding Research Question(RQ). 
 - The folder `RQ1` contains the hardware information frequency data in UAV bug report in `RQ1.xlsx`. 
 - The folder `RQ2` contains the counts of S2R involving hardware in `RQ2.csv`. 
 - The folder `RQ3` contains the frequency data of different hardware in `RQ3.csv`. The folder `classification` includes the details of the classification.
 - The folder `RQ4` contains the metrics data needed for `RQ4` in `RQ4.xlsx`. The file `output.txt` shows the result of `Mann-Whitney U test` and `Cliff's delta`.
 - The folder `RQ5` contains the metrics data needed for `RQ5` in `RQ5.xlsx`. The file `output.txt` shows the result of `Mann-Whitney U test` and `Cliff's delta`. The image `RQ5.png` shows the result of `Img.py`.
 - The folder `RQ6` contains the results of reproduction experiments in  the folder `hardware-compatible`, `hardware-incompatible` and `hardware-unrelated`.
 - The folder `RQ7` contains the metrics data needed for `RQ7` in `RQ7.xlsx`. The file `output.txt` shows the result of `Spearman's rank correlation coefficient` . The folder `FailedReasonsOfS2Rs` includes the classification details of the S2Rs failed reason.
 - The folder `Discussion1` contains the label results of S2R accuracy in `Discussion.xlsx`. 
 - The folder `Discussion2` contains the classification details of the category `Executable with divergent bugs` in  the folder `hardware-compatible`, `hardware-incompatible` and `hardware-unrelated`. The file `summary.txt` shows the description of the divergent bug behavior. 