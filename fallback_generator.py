#!/usr/bin/env python3
"""
Cultivation Story Moments Generator
Creates thousands of unique cultivation novel scenarios in JSON format
"""

import json
import random

class CultivationMomentGenerator:
    def __init__(self):
        self.moments = []
        
        # Building blocks for cultivation scenarios
        self.cultivation_terms = {
            'energy': ['qi', 'spiritual energy', 'essence', 'divine power', 'heavenly energy', 
                      'demonic qi', 'celestial force', 'dao essence', 'primordial energy'],
            'body_parts': ['dantian', 'meridians', 'golden core', 'nascent soul', 'sea of consciousness',
                         'third eye', 'spiritual root', 'energy channels', 'qi vessels', 'inner world'],
            'stages': ['foundation establishment', 'core formation', 'nascent soul', 'spirit severing',
                      'dao seeking', 'immortal ascension', 'transcendence', 'saint realm'],
            'techniques': ['cultivation method', 'secret art', 'forbidden technique', 'divine ability',
                         'ancient manual', 'supreme law', 'heavenly scripture', 'dao technique'],
            'items': ['jade slip', 'spirit stone', 'pill furnace', 'formation plate', 'dao artifact',
                     'ancient talisman', 'divine weapon', 'spirit herb', 'heavenly treasure'],
            'locations': ['spirit realm', 'secret realm', 'ancient ruins', 'forbidden zone', 'mystic peak',
                        'hidden valley', 'dao platform', 'cultivation cave', 'sacred ground'],
            'entities': ['sect elder', 'hidden expert', 'ancient spirit', 'dao companion', 'rival disciple',
                        'mysterious figure', 'sect master', 'rogue cultivator', 'demon beast'],
            'phenomena': ['tribulation lightning', 'heavenly vision', 'dao epiphany', 'qi deviation',
                         'bottleneck', 'enlightenment', 'karmic backlash', 'spiritual resonance'],
            'colors': ['jade', 'crimson', 'azure', 'golden', 'violet', 'emerald', 'obsidian', 'silver'],
            'elements': ['wood', 'fire', 'water', 'metal', 'earth', 'wind', 'lightning', 'ice', 'darkness'],
        }
        
        self.green_related = ['jade', 'emerald', 'verdant', 'viridian', 'forest', 'spring', 'life', 'growth']
        
    def generate_discovery_moments(self, count=500):
        """Moments about discovering secrets or abilities"""
        templates = [
            {
                's': 'You discover {item} hidden in {location}. {energy_desc}.',
                'c1': 'Take it immediately',
                'c2': 'Study it first'
            },
            {
                's': 'Your {body_part} reacts to {phenomenon}. Ancient memories flood your mind.',
                'c1': 'Embrace the memories',
                'c2': 'Resist the influence'
            },
            {
                's': '{entity} offers to teach you {technique}. The price is steep.',
                'c1': 'Accept the offer',
                'c2': 'Decline politely'
            },
            {
                's': 'You find a hidden chamber. {color} light pulses from within.',
                'c1': 'Enter carefully',
                'c2': 'Mark it and return later'
            },
            {
                's': 'Your cultivation suddenly breaks through. {element} energy surges uncontrollably.',
                'c1': 'Channel it into attack',
                'c2': 'Stabilize your foundation'
            },
        ]
        
        for _ in range(count):
            template = random.choice(templates)
            moment = {
                's': template['s'].format(
                    item=random.choice(self.cultivation_terms['items']),
                    location=random.choice(self.cultivation_terms['locations']),
                    energy_desc=f"It radiates {random.choice(self.cultivation_terms['colors'])} {random.choice(self.cultivation_terms['energy'])}",
                    body_part=random.choice(self.cultivation_terms['body_parts']),
                    phenomenon=random.choice(self.cultivation_terms['phenomena']),
                    entity=random.choice(self.cultivation_terms['entities']),
                    technique=random.choice(self.cultivation_terms['techniques']),
                    color=random.choice(self.cultivation_terms['colors']),
                    element=random.choice(self.cultivation_terms['elements'])
                ),
                'c1': template['c1'],
                'c2': template['c2']
            }
            self.moments.append(moment)
    
    def generate_conflict_moments(self, count=500):
        """Moments involving combat or confrontation"""
        templates = [
            {
                's': '{entity} challenges you to a duel. Their {element} cultivation surpasses yours by {stages}.',
                'c1': 'Accept the challenge',
                'c2': 'Find another solution'
            },
            {
                's': 'Demonic cultivators attack your sect. {phenomenon} darkens the sky.',
                'c1': 'Fight at the frontlines',
                'c2': 'Protect the disciples'
            },
            {
                's': 'Your rival obtains {item}. Their power grows exponentially.',
                'c1': 'Confront them now',
                'c2': 'Cultivate harder'
            },
            {
                's': 'A spirit beast blocks your path. Its {color} eyes show intelligence.',
                'c1': 'Attempt to tame it',
                'c2': 'Fight your way through'
            },
            {
                's': 'The sect tournament begins. Victory means access to {location}.',
                'c1': 'Go all out',
                'c2': 'Hide your true strength'
            },
        ]
        
        for _ in range(count):
            template = random.choice(templates)
            moment = {
                's': template['s'].format(
                    entity=random.choice(self.cultivation_terms['entities']),
                    element=random.choice(self.cultivation_terms['elements']),
                    stages=random.choice(['one stage', 'two stages', 'an entire realm']),
                    phenomenon=random.choice(self.cultivation_terms['phenomena']),
                    item=random.choice(self.cultivation_terms['items']),
                    color=random.choice(self.cultivation_terms['colors']),
                    location=random.choice(self.cultivation_terms['locations'])
                ),
                'c1': template['c1'],
                'c2': template['c2']
            }
            self.moments.append(moment)
    
    def generate_cultivation_moments(self, count=500):
        """Moments about cultivation progress and breakthroughs"""
        templates = [
            {
                's': 'You reach a bottleneck at {stage}. {phenomenon} blocks your path forward.',
                'c1': 'Force a breakthrough',
                'c2': 'Consolidate your foundation'
            },
            {
                's': 'A {color} pill appears before you. It could advance you three minor realms instantly.',
                'c1': 'Consume it immediately',
                'c2': 'Refine it further'
            },
            {
                's': 'Your {technique} shows signs of mutation. {element} energy behaves strangely.',
                'c1': 'Investigate the change',
                'c2': 'Return to orthodox methods'
            },
            {
                's': 'Enlightenment strikes during meditation. The dao of {element} reveals itself.',
                'c1': 'Comprehend deeply',
                'c2': 'Record it for later'
            },
            {
                's': 'Your {body_part} shows cracks. Breakthrough is imminent but dangerous.',
                'c1': 'Breakthrough now',
                'c2': 'Seek guidance first'
            },
        ]
        
        for _ in range(count):
            template = random.choice(templates)
            moment = {
                's': template['s'].format(
                    stage=random.choice(self.cultivation_terms['stages']),
                    phenomenon=random.choice(self.cultivation_terms['phenomena']),
                    color=random.choice(self.cultivation_terms['colors']),
                    technique=random.choice(self.cultivation_terms['techniques']),
                    element=random.choice(self.cultivation_terms['elements']),
                    body_part=random.choice(self.cultivation_terms['body_parts'])
                ),
                'c1': template['c1'],
                'c2': template['c2']
            }
            self.moments.append(moment)
    
    def generate_mystery_moments(self, count=500):
        """Mysterious and intrigue-filled moments"""
        templates = [
            {
                's': 'Strange symbols appear in your {body_part}. They glow {color} when you cultivate.',
                'c1': 'Investigate their meaning',
                'c2': 'Conceal them from others'
            },
            {
                's': '{entity} whispers about the forbidden {technique}. Many who sought it vanished.',
                'c1': 'Pursue the knowledge',
                'c2': 'Report them to elders'
            },
            {
                's': 'You witness {entity} performing a ritual. {phenomenon} warps reality around them.',
                'c1': 'Interrupt the ritual',
                'c2': 'Watch and learn'
            },
            {
                's': 'A prophecy mentions someone with your exact cultivation signature. You are not the first.',
                'c1': 'Search for the others',
                'c2': 'Dismiss it as coincidence'
            },
            {
                's': 'The {item} you found contains a fragment of someone\'s soul. It speaks to you.',
                'c1': 'Listen to its wisdom',
                'c2': 'Attempt to exorcise it'
            },
        ]
        
        for _ in range(count):
            template = random.choice(templates)
            moment = {
                's': template['s'].format(
                    body_part=random.choice(self.cultivation_terms['body_parts']),
                    color=random.choice(self.cultivation_terms['colors']),
                    entity=random.choice(self.cultivation_terms['entities']),
                    technique=random.choice(self.cultivation_terms['techniques']),
                    phenomenon=random.choice(self.cultivation_terms['phenomena']),
                    item=random.choice(self.cultivation_terms['items'])
                ),
                'c1': template['c1'],
                'c2': template['c2']
            }
            self.moments.append(moment)
    
    def generate_green_truth_moments(self, count=300):
        """Moments specifically about the mysterious "green truth" """
        templates = [
            {
                's': 'Jade qi pulses in your {body_part}. Something ancient stirs within.',
                'c1': 'Absorb the jade energy',
                'c2': 'Study it carefully'
            },
            {
                's': 'An elder mentions the Emerald Truth in passing. Their eyes gleam knowingly.',
                'c1': 'Ask directly about it',
                'c2': 'Investigate secretly'
            },
            {
                's': 'Green light emanates from your meridians during breakthrough. It feels alive.',
                'c1': 'Embrace the green qi',
                'c2': 'Control and suppress it'
            },
            {
                's': 'The forbidden scroll speaks of "those touched by verdant fate." The ink is still wet.',
                'c1': 'Read the entire scroll',
                'c2': 'Seal it immediately'
            },
            {
                's': 'Your reflection shows jade patterns spreading across your skin. Others cannot see them.',
                'c1': 'Accelerate the transformation',
                'c2': 'Find a way to reverse it'
            },
            {
                's': 'A voice from the emerald realm calls your name. You are the only one who hears it.',
                'c1': 'Answer the call',
                'c2': 'Shut out the voice'
            },
            {
                's': 'Ancient texts describe the "Jade Path" as both salvation and damnation.',
                'c1': 'Walk the Jade Path',
                'c2': 'Seek an alternative'
            },
            {
                's': 'Green flames consume your enemies without burning them. They become something else.',
                'c1': 'Study this phenomenon',
                'c2': 'Never use it again'
            },
            {
                's': 'The sect\'s forbidden archive contains one file marked "Viridian Ascendants." It lists your name.',
                'c1': 'Confront the sect master',
                'c2': 'Erase the records'
            },
            {
                's': 'Every cultivator you kill leaves behind a jade seed. They sprout into something impossible.',
                'c1': 'Cultivate the seeds',
                'c2': 'Destroy them all'
            },
        ]
        
        for _ in range(count):
            template = random.choice(templates)
            # Add some variation
            body_part = random.choice(self.cultivation_terms['body_parts'])
            
            if '{body_part}' in template['s']:
                moment = {
                    's': template['s'].format(body_part=body_part),
                    'c1': template['c1'],
                    'c2': template['c2']
                }
            else:
                moment = template
            
            self.moments.append(moment)
    
    def generate_relationship_moments(self, count=300):
        """Moments involving other characters and relationships"""
        templates = [
            {
                's': 'Your dao companion\'s cultivation diverges from yours. The gap widens daily.',
                'c1': 'Help them catch up',
                'c2': 'Continue your own path'
            },
            {
                's': 'A junior disciple idolizes you. They copy your every technique recklessly.',
                'c1': 'Take them as apprentice',
                'c2': 'Keep your distance'
            },
            {
                's': 'The sect master\'s daughter confesses feelings for you. Political implications are vast.',
                'c1': 'Accept her feelings',
                'c2': 'Decline respectfully'
            },
            {
                's': 'Your sworn brother betrays you for {item}. The sect demands judgment.',
                'c1': 'Show mercy',
                'c2': 'Execute him personally'
            },
            {
                's': 'A mysterious figure offers to become your master. They know your deepest secret.',
                'c1': 'Accept their tutelage',
                'c2': 'Refuse and flee'
            },
        ]
        
        for _ in range(count):
            template = random.choice(templates)
            moment = {
                's': template['s'].format(
                    item=random.choice(self.cultivation_terms['items'])
                ) if '{item}' in template['s'] else template['s'],
                'c1': template['c1'],
                'c2': template['c2']
            }
            self.moments.append(moment)
    
    def generate_consequence_moments(self, count=400):
        """Moments about facing consequences of past choices"""
        templates = [
            {
                's': 'The {technique} you practiced has side effects. Your personality slowly changes.',
                'c1': 'Continue anyway',
                'c2': 'Abandon the technique'
            },
            {
                's': 'Those you killed in the past return as vengeful spirits. They grow stronger nightly.',
                'c1': 'Face them in battle',
                'c2': 'Seek exorcism methods'
            },
            {
                's': 'Your rapid advancement damaged your foundation. Cracks appear in your {body_part}.',
                'c1': 'Push through anyway',
                'c2': 'Spend years repairing it'
            },
            {
                's': 'The forbidden art you learned brands you. All orthodox cultivators can sense it.',
                'c1': 'Embrace your path',
                'c2': 'Seek cleansing rituals'
            },
            {
                's': 'Your cultivation method conflicts with the sect\'s. You must choose one.',
                'c1': 'Stay loyal to sect',
                'c2': 'Follow your own dao'
            },
        ]
        
        for _ in range(count):
            template = random.choice(templates)
            moment = {
                's': template['s'].format(
                    technique=random.choice(self.cultivation_terms['techniques']),
                    body_part=random.choice(self.cultivation_terms['body_parts'])
                ),
                'c1': template['c1'],
                'c2': template['c2']
            }
            self.moments.append(moment)
    
    def generate_all(self, total=3000):
        """Generate all types of moments"""
        print(f"Generating {total} cultivation story moments...")
        
        self.generate_discovery_moments(500)
        print(f"Generated {len(self.moments)} discovery moments")
        
        self.generate_conflict_moments(500)
        print(f"Generated {len(self.moments)} total moments (conflicts added)")
        
        self.generate_cultivation_moments(500)
        print(f"Generated {len(self.moments)} total moments (cultivation added)")
        
        self.generate_mystery_moments(500)
        print(f"Generated {len(self.moments)} total moments (mystery added)")
        
        self.generate_green_truth_moments(300)
        print(f"Generated {len(self.moments)} total moments (green truth added)")
        
        self.generate_relationship_moments(300)
        print(f"Generated {len(self.moments)} total moments (relationships added)")
        
        self.generate_consequence_moments(400)
        print(f"Generated {len(self.moments)} total moments (consequences added)")
        
        # Shuffle for variety
        random.shuffle(self.moments)
        
        return self.moments
    
    def save(self, filename='cultivation_moments.json'):
        """Save to JSON file"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.moments, f, indent=2, ensure_ascii=False)
        
        print(f"\nSaved {len(self.moments)} moments to {filename}")
        print(f"File size: {len(json.dumps(self.moments))} bytes")

if __name__ == '__main__':
    generator = CultivationMomentGenerator()
    generator.generate_all(3000)
    generator.save()
    
    print("\n=== Sample Moments ===")
    for moment in random.sample(generator.moments, 5):
        print(f"\nStory: {moment['s']}")
        print(f"  Choice 1: {moment['c1']}")
        print(f"  Choice 2: {moment['c2']}")
