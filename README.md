# Group 06 - Project 3

GitHub repository for the final Project of DL for Image Analysis Autumn 2023 at UiO.

Based on the work of [Song et al. (2021)](https://github.com/yang-song/score_sde_pytorch)

## Setup
Set up virtual environment
```shell	
python -m venv venv
```

Activate custom virtual environment 
```shell
source venv/bin/activate
```

Install required packages
```shell
pip install -r requirements.txt
```

Add environment to Jupyter Notebook
```shell
python -m ipykernel install --user --name=venv
```

Create workdir and (TODO adapt later)
```shell
mkdir output output/eval output/workdir
```


## Run Training
To run DDPM++ VP-SDE on CIFAR10
```shell
python main.py --config ./configs/vp/cifar10_ddpmpp.py --mode train
```

Run poisson with DDPM++ backbone on CIFAR10
```shell
python main.py --config ./configs/poisson/cifar10_ddpmpp.py --mode train
```


[WIP] Run on MNIST
```shell
python main.py --config ./configs/vp/mnist_ddpmpp.py --mode train
```


## Run Evaluation
To evaluate DDPM++ VP-SDE
```shell
python main.py --config ./configs/vp/cifar10_ddpmpp.py --mode eval
```


## Specify parameters
Change parameter values in respective [config file(s)](/configs).

<br/>
