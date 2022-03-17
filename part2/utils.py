import json

def load_candidates_from_json(filename):
    """Create list with candidates from a json file"""
    with open(filename, mode='r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def get_candidate(candidates, candidate_id):
    """Get candidate data for specific ID"""
    return candidates[candidate_id - 1]

def find_candidates_by_name(candidates, name):
    """Get list of candidates with specific name"""
    candidates_found = []
    for candidate in candidates:
        if name.capitalize() in candidate['name']:
            candidates_found.append(candidate)
    return candidates_found

def find_candidates_by_skill(candidates, skill_name):
    """Get list of candidates with specific skill"""
    candidates_found = []
    for candidate in candidates:
        candidate_skills = [skill.lower() for skill in candidate['skills'].split(', ')]
        if skill_name.lower() in candidate_skills:
            candidates_found.append(candidate)
    return candidates_found

if __name__ == '__main__':
    # Test 1
    filename = "candidates.json"
    candidates = load_candidates_from_json(filename)
    print(candidates)
    # Test 2
    print(get_candidate(candidates, 1))
    # Test 3
    print(find_candidates_by_name(candidates, 'adela'))
    # Test 4
    print(find_candidates_by_skill(candidates, 'python'))