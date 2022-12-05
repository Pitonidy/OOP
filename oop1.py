# class PC:
#     def __init__(self,name, CPU, OZU, GPU, SSD, motherboard, monitor):
#         self.name = name
#         self.CPU = CPU
#         self.OZU = OZU
#         self.GPU = GPU
#         self.SSD = SSD
#         self.motherboard = motherboard
#         self. monitor = monitor

#     def get_info(self):
#         return {
#             self.name: {
#                 "processor":self.CPU,
#                 "Random Access Memory":self.OZU,
#                 "VIdeocard":self.GPU,
#                 "Harddisk":self.SSD,
#                 "Motherboard":self.motherboard,
#                 "Monitor":self.monitor
#                 }
#         }

# pc1 = PC(name="Dell", CPU="core i9",  OZU="32GB",  GPU="GeForce 3080 RTX",  SSD="Samsung Evo960 Pro",  motherboard="Gigabyte X570 GBT", monitor="Dell 27")


# print(pc1.get_info())

colors = {
    "black": {
        "category": "hue",
        "type": "primary",
        "code": {
            "rgba": [255, 255, 255, 1],
            "hex": "#000"
        }
    },
    "white": {
        "category": "value",
        "code": {
            "rgba": [0, 0, 0, 1],
            "hex": "#FFF"
        }
    },
    "red": {
        "category": "hue",
        "type": "primary",
        "code": {
            "rgba": [255, 0, 0, 1],
            "hex": "#FF0"
        }
    },
    "blue": {
        "category": "hue",
        "type": "primary",
        "code": {
            "rgba": [0, 0, 255, 1],
            "hex": "#00F"
        }
    },
    "yellow": {
        "category": "hue",
        "type": "primary",
        "code": {
            "rgba": [255, 255, 0, 1],
            "hex": "#FF0",
            "green": {
                "category": "hue",
                "type": "secondary",
                "code": {
                    "rgba": [0, 255, 0, 1],
                    "hex": "#0F0"
        }
    }
        }
    }
}





class ParseData:
    def __init__(self):
        self.keys = []
        self.values = []
    
    def get_keys_list(self, data):
        for key in data:
            self.keys.append(key)
            if type(data[key]) == dict:
                self.get_keys_list(data[key])
    def get_values_list(self, data):
        for key in data:
            if type(data[key]) != dict:
                self.values.append(data[key])
            if type(data[key]) == dict:
                self.get_values_list(data[key])
        
    def get_keys_tule(self):
        return tuple(self.keys)
    
    def get_keys_set(self):
        return set(self.keys)

p = ParseData()
p.get_keys_list(colors)
p.get_values_list(colors)

print(p.values)


