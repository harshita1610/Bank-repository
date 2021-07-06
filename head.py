import yaml
import pprint as pp

with open('Head.yml','r') as f :
     result = yaml.safe_load(f)
pp.pprint(result)