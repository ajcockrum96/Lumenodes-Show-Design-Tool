from sdt_ops_frame import SDTOpsFrame
from tkinter.ttk import Button


class SDTPackOps(SDTOpsFrame):
    def __init__(self, master=None, sdt=None):
        SDTOpsFrame.__init__(self, master=master, sdt=sdt,
                             text="Pack Operations")

        self._init_ops()

    def add_pack_id(self):
        success = self.sdt.add_pack_id()
        if(success):
            self._sdt_status_update("Added Pack ID")

    def alias_pack_id(self):
        success = self.sdt.alias_pack_id()
        if(success):
            self._sdt_status_update("Aliased Pack ID")

    def assign_pack_id(self):
        success = self.sdt.assign_pack_id()
        if(success):
            self._sdt_status_update("Assigned Pack ID")

    def remove_pack_id(self):
        success = self.sdt.remove_pack_id()
        if(success):
            self._sdt_status_update("Removed Pack ID")

    def _init_ops(self):
        # Pack Operations
        self.add_pack_id_button = Button(master=self,
                                         text="Add Pack ID",
                                         command=self.add_pack_id)
        self._add(self.add_pack_id_button)

        self.remove_pack_id_button = Button(master=self,
                                            text="Remove Pack ID",
                                            command=self.remove_pack_id)
        self._add(self.remove_pack_id_button)

        self.alias_pack_id_button = Button(master=self,
                                           text="Alias Pack ID",
                                           command=self.alias_pack_id)
        self._add(self.alias_pack_id_button)

        self.assign_pack_id_button = Button(master=self,
                                            text="Assign Pack ID",
                                            command=self.assign_pack_id)
        self._add(self.assign_pack_id_button)
