#!python3

import os
import re
import yaml

def extract_intents_from_nlu(nlu_rules_file, intents):
  with open(nlu_rules_file, 'r') as f:
      nlu_rules = yaml.safe_load(f)['nlu']
      if nlu_rules is None:
          return
      for rule in nlu_rules:
          if rule.get('intent'):
            intents.add(rule['intent'])

def extract_entities_from_nlu(nlu_rules_file, entities):
  pattern = r'\((.*?)\)'
  with open(nlu_rules_file, 'r') as f:
      nlus = yaml.safe_load(f)['nlu']
      if nlus is None:
          return
      for rule in nlus:
          matches = re.findall(pattern, rule['examples'])
          if matches:
              for match in matches:
                  entities.add(match)

def extract_actions_from_stories(stories_file, actions):
    with open(stories_file, 'r') as f:
        stories = yaml.safe_load(f).get('stories')
        if stories is None:
            return
        for story in stories:
            for step in story['steps']:
                if step.get('action'):
                    actions.add(step['action'])

def extract_actions_from_rules(rules_file, actions):
    with open(rules_file, 'r') as f:
        rules = yaml.safe_load(f).get('rules')
        if rules is None:
            return
        for rule in rules:
          for step in rule['steps']:
              if step.get('action'):
                actions.add(step['action'])

def generate_domain_yaml(intents, actions, entities, output_file):
    domain_yaml = {
        'intents': list(intents),
        'actions': list(actions),
        'entities': list(entities),
    }

    with open(output_file, 'w') as f:
        #write version: 3.1
        f.write("version: \"3.1\"\n")
        yaml.dump(domain_yaml, f)

if __name__ == '__main__':
  intents = set()
  entities = set()
  actions = set()
  for filename in os.listdir("./data"):
      if filename.endswith(".yml"):
          extract_intents_from_nlu("./data/" + filename, intents)
          extract_entities_from_nlu("./data/" + filename, entities)
          extract_actions_from_stories("./data/" + filename, actions)
          extract_actions_from_rules("./data/" + filename, actions)
  generate_domain_yaml(intents, actions, entities, "./domains/domain.yml")
