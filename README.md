# Computer Vision: Filtering, Object Recognition & Features [![HitCount](http://hits.dwyl.com/Adamouization/Computer-Vision-Filtering-and-Object-Recognition-and-Features.svg)](http://hits.dwyl.com/Adamouization/Computer-Vision-Filtering-and-Object-Recognition-and-Features) [![GitHub stars](https://img.shields.io/github/stars/Adamouization/Computer-Vision-Filtering-and-Object-Recognition-and-Features)](https://github.com/Adamouization/Computer-Vision-Filtering-and-Object-Recognition-and-Features/stargazers) [![GitHub license](https://img.shields.io/github/license/Adamouization/Computer-Vision-Filtering-and-Object-Recognition-and-Features)](https://github.com/Adamouization/Computer-Vision-Filtering-and-Object-Recognition-and-Features/blob/master/LICENSE)

**Intensity-based** template matching and **feature-based** template matching using **SIFT** algorithms for matching images are implemented. A [Training dataset](https://github.com/Adamouization/Computer-Vision-Filtering-and-Object-Recognition-and-Features/tree/master/dataset/Training) of images (icons) a [Testing dataset](https://github.com/Adamouization/Computer-Vision-Filtering-and-Object-Recognition-and-Features/tree/master/dataset/Test) (various combinations of icons) as shown in Figure 2 are used.

Project developed in collaboration with [yissok](https://github.com/yissok).

The report can be read [here](https://github.com/Adamouization/Computer-Vision-Filtering-and-Object-Recognition-and-Features/blob/master/report/report.pdf).

## Usage

Clone the repository (or download the zipped project):
`$ git clone https://github.com/Adamouization/Computer-Vision-Filtering-and-Object-Recognition-and-Features`

Create a virtual environment for the project and activate it:

```
virtualenv ~/Environments/Computer-Vision-Filtering-and-Object-Recognition-and-Features
source Computer-Vision-Filtering-and-Object-Recognition-and-Features/bin/activate
```

Once you have the virtualenv activated and set up, `cd` into the project directory and install the requirements needed to run the app:

```
pip install -r requirements.txt
```

You can now run the app:
```
python main.py -m <model_type> --mode <mode> --debug
```

where:
* `-m <model_type>` corresponds to the matching technique to use e.g. `convolution`, `intensity` or `sift`.
* `--mode <mode>` corresponds to `train` or `test`.
* `--d` runs the program in debug mode with additional print statements.

## Contact
* Email: adam@jaamour.com
* LinkedIn: [@adamjaamour](https://www.linkedin.com/in/adamjaamour/)
