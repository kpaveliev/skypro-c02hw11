from flask import Flask, request, render_template
from part2.utils import load_candidates_from_json, get_candidate, find_candidates_by_name, find_candidates_by_skill

app = Flask(__name__, template_folder='part2', static_folder='part2')
filename ='part2/candidates.json'
candidates = load_candidates_from_json(filename)


@app.route('/')
def all_candidates():
    return render_template('list.html', candidates=candidates)

@app.route('/candidate/<int:candidate_id>')
def candidate_by_id(candidate_id):
    candidate = get_candidate(candidates, candidate_id)
    return render_template('card.html', candidate=candidate)

@app.route('/search/<candidate_name>')
def candidates_by_name(candidate_name):
    candidates_found = find_candidates_by_name(candidates, candidate_name)
    return render_template('search.html',
                           candidates=candidates_found, number_found=len(candidates_found))

@app.route('/skill/<skill_name>')
def candidates_by_skill(skill_name):
    candidates_found = find_candidates_by_skill(candidates, skill_name)
    return render_template('skill.html', candidates=candidates_found,
                           number_found=len(candidates_found), skill_name=skill_name)

# Additional (not required)
@app.route('/search', methods=["GET", "POST"])
def search_skill():
    searched_skill = request.form['searched_skill']
    candidates_found = find_candidates_by_skill(candidates, searched_skill)
    return render_template('skill.html', candidates=candidates_found,
                           number_found=len(candidates_found), skill_name=searched_skill)

if __name__ == '__main__':
    app.run()