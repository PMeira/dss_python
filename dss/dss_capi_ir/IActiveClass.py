'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2020 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Base

class IActiveClass(Base):
    __slots__ = []

    _columns = [
        'ActiveClassName',
        'ActiveClassParent',
        'Name',
        'NumElements',
    ]

    @property
    def ActiveClassName(self):
        '''(read-only) Returns name of active class.'''
        return self._get_string(self.CheckForError(self._lib.ActiveClass_Get_ActiveClassName()))

    @property
    def AllNames(self):
        '''(read-only) Array of strings consisting of all element names in the active class.'''
        return self.CheckForError(self._get_string_array(self._lib.ActiveClass_Get_AllNames))

    @property
    def Count(self):
        '''(read-only) Number of elements in Active Class. Same as NumElements Property.'''
        return self.CheckForError(self._lib.ActiveClass_Get_Count())

    def __len__(self):
        return self.CheckForError(self._lib.ActiveClass_Get_Count())

    def __iter__(self):
        n = self.First
        while n:
            yield self
            n = self.Next

    @property
    def First(self):
        '''(read-only) Sets first element in the active class to be the active DSS object. If object is a CktElement, ActiveCktELment also points to this element. Returns 0 if none.'''
        return self.CheckForError(self._lib.ActiveClass_Get_First())

    @property
    def Name(self):
        '''Name of the Active Element of the Active Class'''
        return self._get_string(self.CheckForError(self._lib.ActiveClass_Get_Name()))

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._lib.ActiveClass_Set_Name(Value))

    @property
    def Next(self):
        '''(read-only) Sets next element in active class to be the active DSS object. If object is a CktElement, ActiveCktElement also points to this element.  Returns 0 if no more.'''
        return self.CheckForError(self._lib.ActiveClass_Get_Next())

    @property
    def NumElements(self):
        '''(read-only) Number of elements in this class. Same as Count property.'''
        return self.CheckForError(self._lib.ActiveClass_Get_NumElements())

    @property
    def ActiveClassParent(self):
        '''Get the name of the parent class of the active class'''
        return self._get_string(self.CheckForError(self._lib.ActiveClass_Get_ActiveClassParent()))
