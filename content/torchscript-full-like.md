Title: Full tensors in Torchscript
Date: 2020-02-08 13:30
Category: Programming
Tags: tips, torchscript

# Full tensors in Torchscript

I was productizing some PyTorch models recently and ran in to an issue with the way `torch.full_like` behaves in Torchscript.


```python
import torch
```

The original code use `torch.full_like` to create a tensor with a given shape.  It also forced the type of the new tensor to `torch.float16`.  A minimal example that illustrates the issue is below.


```python
def full(val: float, base: torch.Tensor):
    return torch.full_like(base, val, dtype=torch.float16)
full(42.0, torch.tensor([1, 2]))
```




    tensor([42., 42.], dtype=torch.float16)



Converting directly to Torchscript fails, apparently because Torchscript can't select the appropriate overload.


```python
@torch.jit.script
def full1(val: float, base: torch.Tensor):
    return torch.full_like(base, val, dytpe=torch.float16)

full1(42.0, torch.tensor([1, 2]))
```
...

    RuntimeError: 
    Arguments for call are not valid.
    The following variants are available:
      
      aten::full_like(Tensor self, Scalar fill_value, *, int? memory_format=None) -> (Tensor):
      Keyword argument dytpe unknown.
      
      aten::full_like.dtype(Tensor self, Scalar fill_value, *, int dtype, int layout, Device device, bool pin_memory=False, int? memory_format=None) -> (Tensor):
      Argument dtype not provided.
    
    The original call is:
      File "<ipython-input-8-d96dada73816>", line 3
    @torch.jit.script
    def full1(val: float, base: torch.Tensor):
        return torch.full_like(base, val, dytpe=torch.float16)
               ~~~~~~~~~~~~~~~ <--- HERE



# Workarounds

## Provide all the arguments

The obvious solution is to provide all the arguments.  That works, but is rather more verbose.


```python
@torch.jit.script
def full2(val: float, base: torch.Tensor):
    return torch.full_like(
        base,
        val,
        dtype=torch.float16,
        layout=base.layout,
        device=base.device,
    )

full2(42.0, torch.tensor([1, 2]))
```




    tensor([42., 42.], dtype=torch.float16)



## Switch to torch.full

In this case, only the shape is needed.  The device and layout are already the defaults, so `torch.full` is appropriate.


```python
@torch.jit.script
def full3(val: float, base: torch.Tensor):
    return torch.full(base.shape, val, dtype=torch.float16)

full3(42.0, torch.tensor([1, 2]))
```




    tensor([42., 42.], dtype=torch.float16)


