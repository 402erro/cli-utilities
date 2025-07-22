import os
class Main:
    def __init__(self):
        self.user = os.getlogin()
        self.UtilityPath = r"C:\Users\rowdh\OneDrive\Documents\Tomfoolery\Personal Project\cli-utilities\utils"
        self.suffix = ".py"
    
    def get_utility_list(self):
        UtilityList = os.listdir(self.UtilityPath)
        # print(UtilityList)
        return UtilityList

    def get_utility_names(self):
        UtilityList = self.get_utility_list()
        CleanUtilityList = []

        for Utility in UtilityList:
            if Utility.endswith(self.suffix):
                CleanUtilityList.append(Utility[-3:-1])

        # print(CleanUtilityList)
        return CleanUtilityList

        

    
    
if __name__ == "__main__":
    main = Main()
    main.get_utils()