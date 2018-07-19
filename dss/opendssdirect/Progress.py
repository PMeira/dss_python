from ._utils import *

def Close():
    lib.DSSProgress_Close()
    return 0

def Show():
    lib.DSSProgress_Show()
    return 0

def Caption(Value):
    '''(write-only) Caption to appear on the bottom of the DSS Progress form.'''
    if type(Value) is not bytes:
        Value = Value.encode(codec)

    lib.DSSProgress_Set_Caption(Value)
    return '0'

def PctProgress(Value):
    '''(write-only) Percent progress to indicate [0..100]'''
    lib.DSSProgress_Set_PctProgress(Value)



_columns = []
__all__ = ['Close', 'Show', 'Caption', 'PctProgress']

