import torch


def angles_l1_prior(B: int, N: int, device: torch.device):
    """Sample angles from the l1 prior distribution. Then project onto l2 surface.
    # Based on: https://mathoverflow.net/questions/9185/how-to-generate-random-points-in-ell-p-balls

    Args:
        B: Number of dimensions
        N: Number of samples
        device: Device to use for the samples
    Returns:
        A tensor of shape (D, N) containing the samples
    """
    # Sample B x N values from the distribution exp(-|x|^p) with p = 1
    Xn = torch.empty(B, N).exponential_(1).to(device)
    Xn *= torch.randint(0, 2, size=(B, N)) * 2 - 1  # Randomly assign signs

    # Sample a value from the exponential distribution with parameter 1
    Y = torch.empty(B, N).exponential_(1).to(device)

    # Calculate the ratio (X1, ..., Xn) / (Y + sum(|Xi|^p))^(1/p) with p = 1
    denominator = Y + torch.sum(torch.abs(Xn), dim=1, keepdim=True)
    samples = Xn / denominator
    angles = samples / torch.norm(samples, p=2, dim=1, keepdim=True)

    return angles


def angles_uniform_prior(B: int, N: int, device: torch.device):
    """Original: Sample angles from the Gaussian prior distribution. Then project onto l2 surface."""

    # Uniformly sample the angle direction
    gaussian = torch.randn(B, N).to(device)
    angles = gaussian / torch.norm(gaussian, p=2, dim=1, keepdim=True)

    return angles
