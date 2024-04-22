import json
class jsonReader:
    
    def __init__(self, json_file_path):
        '''
        initializes the jsonReader object with the JSON file path
        @param: json_file_path: the file to be processed
        '''
        self.json_file_path = json_file_path
        self.data= None
    def read_data(self):
        '''
        reads and loads the data from the JSON file
        @param: none
        @return: none 
        '''
        with open(self.json_file_path, 'r') as json_file:
            self.data = json.load(json_file)['Raccoon']
        def get_data(self):
            '''
            returns the json data
            @return: data from JSON file
            '''
            return self.data
        
        