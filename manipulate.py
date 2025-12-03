import copy
import json

def load_template(filename):
    with open(filename, "r") as f:
        return json.load(f)

def replace_value(obj, old, new):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(v, (dict, list)):
                replace_value(v, old, new)
            elif v == old:
                obj[k] = new

    elif isinstance(obj, list):
        for i in range(len(obj)):
            if isinstance(obj[i], (dict, list)):
                replace_value(obj[i], old, new)
            elif obj[i] == old:
                obj[i] = new
    
def main():
    print("Starting main function...")
    var_Query = load_template("./templates/Query.json")
    print("Loaded template:")
    print(json.dumps(var_Query, indent=4))
    replace_value(var_Query, "POD_NAME", "new-pod-name")
    print("Modified template:")
    print(json.dumps(var_Query, indent=4))
    print("Finishing main function...")
    
if __name__ == "__main__":
    main()
