from datetime import datetime
import os
from urllib.parse import urlparse
import requests
import json


class Tracker():
    def __init__(self, username:str, token:str):
        self.token:str = ""
        self.headers = ""
        self.url:str = "https://pixe.la/v1/users"
        self.username:str = ""
        self.graphs:dict = {}

    
    def create_user_account(self, username:str, token:str, terms:str, minor:str):
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
    
    
    def create_new_graph(self, graphid:str, graph_name:str, graph_unit:str, unit_type:str, pixel_color:str):
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
    
    
    def put_pixel(self, date:str, quantity:str, graphid:str):
        """Puts a pixel for given date and quantity. If quantity relatively higher than other pixels
        the color of it will be convert to dark tones of currently selected color.
        Args:
            date (str): Date for to put the pixel in that specific date. Should be in format yyyyMMdd.
            quantity (str): Represents the quantity of input. Example: If this is a book reading graph -> "20" would 
            represent the amount of pages read.
        """
        if graphid:
            url = self.graphs[graphid]
            putting_pixel_config = {
                "date": date,
                "quantity": quantity
            }
            response = requests.post(url=url, json=putting_pixel_config, headers=self.headers)
            print(response.text)
        else:
            print("Graphid cannot be recognized.")
        
    
    def update_pixel(self, date:str, quantity:str, graphid:str):
        """Updates a already existed pixel.
        Useful for fixing wrong inputs/entries.
        Args:
            date (str): Date of the pixel should be fixed. Should be in format yyyyMMdd.
            quantity (str): Actual value of the input/entry. Ex. if int -> '20', '50', if float -> '20.51', '50.99'
        """
        if graphid:
            url = self.graphs[graphid] + f"/{date}"
            update_config = {"quantity": quantity}
            response = requests.put(url=url, json=update_config, headers=self.headers)
            print(response.text)
        else:
            print("Graphid cannot be recognized.")
    
    
    def delete_pixel(self, date:str, graphid:str):
        """Deleting an existing entry.
        Args:
            date (str): Date of the entry that should be deleted. Should be in format yyyyMMdd.
        """
        if graphid:
            url = self.graphs[graphid] + f"/{date}"
            response = requests.delete(url=url, headers=self.headers)
            print(response.text)
        else:
            print("Graphid cannot be recognized.")
    
    
    def read_graphs(self):
        """Reads and the existed graphs from a json data and saves into a dict variable.
        If there is no file, opens one.
        Returns:
            _bool_: False if there is no graph data to read or file is not opened.
        """
        try:
            file = open("intermediate+/habbit_tracker/graphs.json", mode="r")
            json.load(file)
            file.close()
        except FileNotFoundError:
            with open("intermediate+/habbit_tracker/graphs.json", mode="w") as file:
                file.close()
            print("File was not found. New one is now opened.")
            return False
        except json.decoder.JSONDecodeError as e:
            print("JSONDecodeError:", e)
            print("File can be empty.")
            return False
        else:
            with open("intermediate+/habbit_tracker/graphs.json", mode="r") as file:
                self.graphs = json.load(file)
                file.close()
            print("Datas are succesfully readed.")
            return True
            
            
    def save_graphs(self):
        """If there is graph to save and no json data, opens a json data and save them into it.
        If there is a empty json data, writes the graph datas into it.
        If there is a not empty json data, append the new graph datas to the existing ones.
        """
        if self.graphs:
            try:
                file = open("intermediate+/habbit_tracker/graphs.json", mode="r")
                json.load(file)
                file.close()
            except FileNotFoundError as e:
                print("File not found:", e)
                with open("intermediate+/habbit_tracker/graphs.json", mode="w") as file:
                    json.dump(self.graphs, file)
                    file.close()
                print("File has opened and graph link is saved into it.")
            except json.decoder.JSONDecodeError as e:
                print("JSONDecodeError:", e)
                with open("intermediate+/habbit_tracker/graphs.json", mode="w") as file:
                    json.dump(self.graphs, file)
                    file.close()
                print("File was empty but data has been saved.")
            else:
                with open("intermediate+/habbit_tracker/graphs.json", mode="r") as file:
                    existed_graphs = json.load(file)
                    file.close()
                existed_graphs.update(self.graphs)
                with open("intermediate+/habbit_tracker/graphs.json", mode="w") as file:
                    json.dump(existed_graphs, file)
                    file.close()
                print("Graphs were saved.")
        else:
            print("There is no graph data to save.")
        
        
    def get_graph_urls(self):
        """
        Returns:
            _List_: List that contains in tuple format of graphid-url of graph.
        """
        if self.read_graphs():
            urls = []
            for key, value in self.graphs.items():
                urls.append((f"Graph ID:{key}, Graph URL:{value}"))
            return urls
        else:
            print("No graph url to show.")
    
    def is_valid_url(self, url:str):
        try:
            response = requests.head(url, allow_redirects=True)
            print(f"Response = {response}")
            print(f"Response status code = {response.status_code}")
            print(f"Response JSON= {response.json()}")
            print(f"Response Text = {response.text}")
            final_url = response.url  # Get the final URL after following redirections
            print(f"Final Url: {final_url}")
            final_response = requests.head(final_url)  # Make a request to the final URL
            print(f"Final Response = {final_response}")
            print(f"Final Response status code = {final_response.status_code}")
            print(f"Final Response JSON = {final_response.json()}")
            print(f"Final Response Text = {final_response.text}")
            
            if final_response.status_code == 200 and 'text/html' in final_response.headers.get('content-type', '').lower():
                return True  # Returns True if the final URL exists and responds with HTML content
            else:
                return False
        except requests.RequestException:
            return False
            
            
    def set_token(self, token:str):
        self.token = token
    
    
    def set_username(self, username:str):
        self.username = username
        
    
    def set_graph(self, graphid:str):
        url = f"{self.url}/{self.username}/graphs/{graphid}.html"
        if self.is_valid_url(url=url):
            self.graphs[graphid] = url
        else:
            print("There is no URL under the name of this graphid.")
        