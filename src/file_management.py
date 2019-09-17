import pickle

def save_data_to_file(data, filename):
    with open(f"files/{filename}.pickle", 'wb') as handle:
        pickle.dump(data, handle)

def load_file_to_data(filename):
    try:
        with open(f"files/{filename}.pickle", 'rb') as handle:
            data = pickle.load(handle)
        return data
    except:
        return []

def save_all(people, drinks, teams, rounds, completed_rounds):
    save_data_to_file(people, "people")
    save_data_to_file(drinks, "drinks")
    save_data_to_file(teams, "teams")
    save_data_to_file(rounds, "rounds")
    save_data_to_file(completed_rounds, "completed_rounds")

def nuke_data(people, drinks, teams, rounds, completed_rounds):
    save_data_to_file(people, "people_back_up")
    save_data_to_file(drinks, "drinks_back_up")
    save_data_to_file(rounds, "rounds_back_up")
    save_data_to_file(teams, "teams_back_up")
    save_data_to_file(completed_rounds, "completed_rounds_back_up")
    save_data_to_file([], "people")
    save_data_to_file([], "drinks")
    save_data_to_file([], "rounds")
    save_data_to_file([], "teams")
    save_data_to_file([], "completed_rounds")
