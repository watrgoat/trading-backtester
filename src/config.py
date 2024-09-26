import yaml

class Config:
    def __init__(self, config_file):
        """
        Initializes the Config class and loads the configuration from the YAML file.

        Parameters:
        - config_file (str): Path to the YAML configuration file.
        
        Raises:
        - FileNotFoundError: If the config file does not exist or can't be opened.
        - yaml.YAMLError: If the YAML file has syntax errors or can't be parsed.
        """
        try:
            with open(config_file, 'r') as f:
                self.config = yaml.safe_load(f)  # Load the YAML config as a Python dictionary
        except FileNotFoundError as e:
            print(f"Error: The config file {config_file} was not found.")
            raise e
        except yaml.YAMLError as e:
            print(f"Error: Failed to parse YAML file {config_file}. Please check the syntax.")
            raise e

    def get(self, key, default=None):
        """
        Retrieves a value from the configuration using the provided key.
        
        Parameters:
        - key (str): The key to access the configuration value (e.g., 'data', 'strategy').
        - default: The value to return if the key is not found in the config (default is None).
        
        Returns:
        - The value associated with the key from the config file, or the default value if the key is not found.
        
        Example:
        config.get('data')['tickers'] will return the list of tickers if the 'data' section exists.
        """
        return self.config.get(key, default)
