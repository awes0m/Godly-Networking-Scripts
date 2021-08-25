from tkinter import *
from ..main import window
from requests import NullHandler

def assetUpdateUI():
    asset_window= Toplevel(window)
    asset_window.minsize(400,400)
    asset_window.title("Asset group updation window")
    
    #labels
    assetgrpUID= Label(text="-Unique ID-")
    uidAssetgroup=Entry(width=30)
    uidAssetgroup.insert(asset_window,"Asset Group UniqueID")
    uidAssetgroup.focus()
    #buttons
    uidSubmit= Button(asset_window,text="Submit",onpressed=NullHandler)
    helpButton= Button(asset_window,text="Help",onpressed=NullHandler)
    
    
    assetgrpUID.pack()
    uidAssetgroup.pack()
    uidSubmit.pack()
    helpButton.pack()
    
    asset_window.mainloop()