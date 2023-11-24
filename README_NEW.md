# Personal Readme

## CIFAR-10 data
In downloads:
```bash
wget https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz
```

In root to make it zip and get data for FID score computation:
```bash
python dataset_tool.py --source=downloads/cifar-10-python.tar.gz --dest=datasets/cifar-10-python.zip
python fid.py ref --data=datasets/cifar-10-python.zip --dest=fid-refs/cifar-10-python.npz
```


## MNIST data
In downloads:
```bash
wget http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz
wget http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz 
```

In root to make it zip and get data for FID score computation:
```bash
python dataset_tool.py --source=downloads/train-images-idx3-ubyte.gz --dest=datasets/mnist_train.zip
python fid.py ref --data=datasets/mnist_train.zip --dest=fid-refs/mnist_train.npz
```








## Setup GPU support
https://docs.docker.com/config/containers/resource_constraints/#gpu

### Verify nvidia container setup
```bash
which nvidia-container-runtime-hook
```


### Expose GPUs
```bash
docker run -it --rm --gpus all ubuntu nvidia-smi
```


## Docker
### Base docker image
https://catalog.ngc.nvidia.com/orgs/nvidia/containers/pytorch

### Build docker image in curr dir
```bash
docker build -t pfgm_image .
```

### Check for GPU access via docker image
```bash
docker run pfgm_image python cuda_test.py
```


### Run arbitrary tasks via docker
```bash
docker run pfgm_image <<insert bash command here>>
```
