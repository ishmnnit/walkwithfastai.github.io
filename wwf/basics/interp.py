# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/05_interp.ipynb (unless otherwise specified).

__all__ = []

# Cell
from fastai.basics import *

# Cell
@patch
def __getitem__(self:Interpretation, idxs):
    "Get the inputs, preds, targets, decoded outputs, and losses at `idxs`"
    if not is_listy(idxs): idxs = [idxs]
    attrs = 'inputs,preds,targs,decoded,losses'
    res = L([getattr(self, attr)[idxs] for attr in attrs.split(',')])
    return res

# Cell
@patch
@delegates(TfmdDL.show_results)
def show_at(self:Interpretation, idxs, **kwargs):
    "Show predictions on the items at `idxs`"
    inp, _, targ, dec, _ = self[idxs]
    self.dl.show_results((inp, dec), targ, **kwargs)