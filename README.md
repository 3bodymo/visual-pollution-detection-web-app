# Visual Pollution Detection Web Application
![](https://github.com/3bodymo/visual-pollution-detection-web-app/blob/main/demo.gif)
I built a flask web application for [visual-pollution-detection](https://github.com/3bodymo/visual-pollution-detection.git) project, you can use it to object detection instead of dealing with command prompt.

Also you can use it with any YOLOv7 project, just replace `best.pt` file with your model file.

## Setup

```shell
git clone https://github.com/3bodymo/visual-pollution-detection-web-app.git
cd visual-pollution-detection-web-app
```

* **Before install the modules, make sure that you have python3.9 version and run the model on it.**

* After that, you have to install some python libraries by run the following command:

```shell
pip install -r requirements.txt
```

* Now you can run YOLOv7 model successfully, but it will run over the CPU, so if you want to run it over GPU, install PyTorch by this command:

```shell
pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113
```

## Getting Started

 ```shell
python app.py
```
