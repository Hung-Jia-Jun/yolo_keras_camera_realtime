## Requirements

- [Keras](https://github.com/fchollet/keras)
- [Tensorflow](https://www.tensorflow.org/)
- [Numpy](http://www.numpy.org/)
- [h5py](http://www.h5py.org/) (For Keras model serialization.)
- [Pillow](https://pillow.readthedocs.io/) (For rendering test results.)
- [Python 3](https://www.python.org/)
- [OpenCV](https://opencv.org/)

### Installation
```bash
git clone https://github.com/Hung-Jia-Jun/yolo_keras_camera_realtime.git
cd yad2k

# [Option 1] To replicate the conda environment:
conda env create -f environment.yml
source activate yad2k
# [Option 2] Install everything globaly.
pip install numpy h5py pillow
pip install tensorflow-gpu  # CPU-only: conda install -c conda-forge tensorflow
pip install keras # Possibly older release: conda install keras
```

## Quick Start

- Download Darknet model cfg and weights from the [official YOLO website](http://pjreddie.com/darknet/yolo/).
- Convert the Darknet YOLO_v2 model to a Keras model.
- Test the converted model on the small test set in `images/`.

```bash
wget http://pjreddie.com/media/files/yolo.weights
wget https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolo.cfg
#convert weight to yad2k
python yad2k.py yolo.cfg yolo.weights model_data/yolo.h5
python camera_yolo.py model_data/yolo.h5
```
## it will be show now streaming video by url
![preview](https://i.imgur.com/0Sw89bW.png)
![preview](https://i.imgur.com/WB8cquj.png)

## Video preview (you can click image to redirect youtube video)
[![](https://i.imgur.com/XYNPVnJ.png)](https://youtu.be/pvxmvBcPne8)
