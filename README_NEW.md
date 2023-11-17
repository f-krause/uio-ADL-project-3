# Personal Readme

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
