from datetime import datetime
import os
import requests
import json


class Tracker():
    def __init__(self, username: str, token: str):
        self.token: str = token
        self.headers = {"X-USER-TOKEN":token}
        self.url: str = "https://pixe.la/v1/users"
        self.username: str = username
        self.graphs: dict = {}

    def create_user_account(self, username: str, token: str, terms: str, minor: str):
        """Creates a user account in Pixela website with given parameters.
        If terms and minor would not accepted, account cannot be opened.
        Args:
            username (str): Username of the account. Cannot be used second time.
            token (str): Unique token that would be assigned to the account.
            terms (str): Agree terms of service of the website pixela. If user would not accept it, 
            account cannot be created. 'yes' or 'no'.
            minor (str): Specify yes or no as to whether you are not a minor or 
            if you are a minor and you have the parental consent of using this service.
            If user would not accept it, account cannot be created. 'yes' or 'no'.
        """
        self.token = token
        self.username = username
        self.headers = {"X-USER-TOKEN": token}
        user_parameters = {
            "username": username,
            "token": self.token,
            "agreeTermsOfService": terms,
            "notMinor": minor
        }
        response = requests.post(url=self.url, json=user_parameters)
        print(response.text)

    def create_new_graph(self, graphid: str, graph_name: str, graph_unit: str, unit_type: str, pixel_color: str):
        """Crates a new graph with given parameters for currently used username.
        Args:
            graphid (str): Represents the Id of the graph. It's a unique data and will be saved in a hashmap.
            graph_name (str): Name of the graph. Example -> 'My Reading Graph'
            graph_unit (str): Unit of the quantity recorded in graph. Example with reading -> 'Page' 
            unit_type (str): Type of the unit. Example for page -> 'float', 'int'. (Only int and float are supported.)
            
            pixel_color (str): Colors of the pixels in graph.
            shibafu (green), momiji (red), sora (blue), ichou (yellow), ajisai (purple) and 
            kuro (black) are supported as color kind.
        """
        self.graphs[graphid] = f"{self.url}/{self.username}/graphs/{graphid}"
        endpoint = f"{self.url}/{self.username}/graphs"
        graph_config = {
            "id": graphid,
            "name": graph_name,
            "unit": graph_unit,
            "type": unit_type,
            "color": pixel_color
        }
        response = requests.post(url=endpoint, json=graph_config, headers=self.headers)
        print(response.text)


    def put_pixel(self, date: str, quantity: str, graphid: str):
        """Puts a pixel for given date and quantity. If quantity relatively higher than other pixels
        the color of it will be convert to dark tones of currently selected color.
        Args:
            date (str): Date for to put the pixel in that specific date. Should be in format yyyyMMdd.
            quantity (str): Represents the quantity of input. Example: If this is a book reading graph -> "20" would 
            represent the amount of pages read.
        """
        if len(self.graphs) > 0:
            for graph in self.graphs:
                if graphid == graph['id']:
                    url = f"{self.url}/{self.username}/graphs/{graphid}"
                    putting_pixel_config = {
                        "date": date,
                        "quantity": quantity
                    }
                    response = requests.post(url=url, json=putting_pixel_config, headers=self.headers)
                    if response["message"] == "Success.":
                        print("Entry has been saved.")
                    else:
                        print("Error by saving pixel.")
                    print(f"Response text: {response.text}")
                else:
                    print("Graphid isn't valid.")
        else:
            print("There isn't any graph. Please load the graphs first.")
    
    
    def get_pixel(self, date: str, graphid: str):
        """Gets the information of a specific graphs entry, for a given date.

        Args:
            date (str): Date of the pixel that user wants to learn if it exist ,what are the informations of that pixel.
            graphid (str): Id of the graph that being observed.
        """
        if len(self.graphs) > 0:
            for graph in self.graphs:
                if graphid == graph['id']:
                    url = f"{self.url}/{self.username}/graphs/{graphid}/{date}"
                    response = requests.get(url=url, headers=self.headers)
                    print(f"Response text: {response.text}")
                else:
                    print("Graphid isn't valid.")
        else:
            print("There isn't any graph. Please load the graphs first.")
        
        
    def update_pixel(self, date: str, quantity: str, graphid: str):
        """Updates a already existed pixel.
        Useful for fixing wrong inputs/entries.
        Args:
            date (str): Date of the pixel should be fixed. Should be in format yyyyMMdd.
            quantity (str): Actual value of the input/entry. Ex. if int -> '20', '50', if float -> '20.51', '50.99'
        """
        if len(self.graphs) > 0:
            for graph in self.graphs:
                if graphid == graph['id']:
                    url = f"{self.url}/{self.username}/graphs/{graphid}/{date}"
                    update_config = {"quantity": quantity}
                    response = requests.put(url=url, json=update_config, headers=self.headers)
                    print(f"Response text: {response.text}")
                else:
                    print("Graphid isn't valid.")
        else:
            print("There isn't any graph. Please load the graphs first.")


    def delete_pixel(self, date: str, graphid: str):
        """Deleting an existing entry.
        Args:
            date (str): Date of the entry that should be deleted. Should be in format yyyyMMdd.
        """
        if len(self.graphs) > 0:
            for graph in self.graphs:
                if graphid == graph['id']:
                    url = f"{self.url}/{self.username}/graphs/{graphid}/{date}"
                    response = requests.delete(url=url, headers=self.headers)
                    print(f"Response text: {response.text}")
                else:
                    print("Graphid isn't valid.")
        else:
            print("There isn't any graph. Please load the graphs first.")
    

    def load_graphs(self):
        """Loads the existing graphs and their infos from pixela and saves its response.
        Response will be converted to JSON format and saved into a dictionary as self variable.
        """
        if self.username != "" and self.token != "":
            url = str(f"{self.url}/{self.username}/graphs")
            response = requests.get(url=url, headers=self.headers)
            json_data = response.json()
            print(f"JSON Data:{json_data}")
            try:
                self.graphs = json_data['graphs']
            except KeyError as e:
                print(f"KeyError:{e}")
                print("Try to reload the data. JSON could have been not downloaded properly.")
            else:
                print("Urls are successfully loaded.")
        else:
            print("Urls cannot loaded. Username and token are needed.")
            

    def show_graph_infos(self):
        """
        Returns:
            _List_: Contains formatted string variables as elements. Elements contains ID of graph and its URL.
        """
        if len(self.graphs) > 0:
            for graph in self.graphs:
                graphid = graph['id']
                url = f"{self.url}/{self.username}/graphs/{graph['id']}"
                return f"Graph ID:{graphid}, Graph URL:{url}"
        else:
            print("There isn't any graph. Please load the graphs first.")

            
    def set_token(self, token: str):
        self.token = token

    def set_username(self, username: str):
        self.username = username
