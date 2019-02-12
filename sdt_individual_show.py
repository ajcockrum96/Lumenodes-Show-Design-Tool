class SDTIndividualShow:
    def __init__(self, master=None, sdt=None, set_cnt=1):
        self.master = master
        self.sdt = sdt

        # Initialize Variables
        self.set_cnt = set_cnt
        self.set_instructions = []

        self._init_show()

    def add_set_instruction(self):
        # Tuple Representing R, G, and B values respectively
        set_instruction = (0, 0, 0)
        self.set_instructions.append(set_instruction)

    def get_show_info(self):
        show_info = {}
        show_info["type"] = "individual_show"
        show_info["set_instructions"] = self._get_set_instructions()
        return show_info

    def reconfigure_show(self, individual_show_info, new_set_cnt):
        self._adjust_set_cnt(new_set_cnt)
        self._reconfigure_set_instructions(
            individual_show_info["set_instructions"])

    def _adjust_set_cnt(self, new_set_cnt):
        diff = new_set_cnt - self.set_cnt
        self.set_cnt = new_set_cnt
        if(diff > 0):
            for i in range(diff):
                self.add_set_instruction()
        elif(diff < 0):
            for i in range(-diff):
                self.set_instructions.pop()

    def _get_set_instructions(self):
        set_instructions = []
        for i in range(self.set_cnt):
            set_instruction = self.set_instructions[i]
            set_instruction_info = {}
            set_instruction_info["type"] = "set_instruction"
            set_instruction_info["r"] = set_instruction[0]
            set_instruction_info["g"] = set_instruction[1]
            set_instruction_info["b"] = set_instruction[2]
            set_instructions.append(set_instruction_info)
        return set_instructions

    def _init_show(self):
        for i in range(self.set_cnt):
            self.add_set_instruction()

    def _reconfigure_set_instructions(self, new_set_instructions):
        for i in range(self.set_cnt):
            r = new_set_instructions[i]["r"]
            g = new_set_instructions[i]["g"]
            b = new_set_instructions[i]["b"]
            self.set_instructions[i] = (r, g, b)
