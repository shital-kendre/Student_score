import pickle
import json

with open('artifacts/lin_reg_model_student.pkl', 'rb') as f:
    linear_model = pickle.load(f)

with open('artifacts/column_data.json', 'r') as f:
    column_data = json.load(f)

def get_s_score(data):
    try:
        print("Data received: ", data)

        Hours_Studied = float(data['Hours_Studied'])
        Attendance = float(data['Attendance'])
        Sleep_Hours = float(data['Sleep_Hours'])
        Previous_Scores = float(data['Previous_Scores'])
        Tutoring_Sessions = float(data['Tutoring_Sessions'])
        Physical_Activity = float(data['Physical_Activity'])

        # Access categorical data mappings
        Parental_Involvement = column_data["Parental_Involvement"].get(data['Parental_Involvement'])
        Access_to_Resources = column_data["Access_to_Resources"].get(data['Access_to_Resources'])
        Extracurricular_Activities = column_data["Extracurricular_Activities"].get(data['Extracurricular_Activities'])
        Motivation_Level = column_data["Motivation_Level"].get(data['Motivation_Level'])
        Internet_Access = column_data["Internet_Access"].get(data['Internet_Access'])
        Family_Income = column_data["Family_Income"].get(data['Family_Income'])
        Teacher_Quality = column_data["Teacher_Quality"].get(data['Teacher_Quality'])
        School_Type = column_data["School_Type"].get(data['School_Type'])
        Peer_Influence = column_data["Peer_Influence"].get(data['Peer_Influence'])
        Learning_Disabilities = column_data["Learning_Disabilities"].get(data['Learning_Disabilities'])
        Parental_Education_Level = column_data["Parental_Education_Level"].get(data['Parental_Education_Level'])
        Distance_from_Home = column_data["Distance_from_Home"].get(data['Distance_from_Home'])
        Gender = column_data["Gender"].get(data['Gender'])

        # Check if any of the mappings failed
        for field, value in zip(["Parental_Involvement", "Access_to_Resources", "Extracurricular_Activities",
                                 "Motivation_Level", "Internet_Access", "Family_Income", "Teacher_Quality",
                                 "School_Type", "Peer_Influence", "Learning_Disabilities",
                                 "Parental_Education_Level", "Distance_from_Home", "Gender"],
                                [Parental_Involvement, Access_to_Resources, Extracurricular_Activities,
                                 Motivation_Level, Internet_Access, Family_Income, Teacher_Quality,
                                 School_Type, Peer_Influence, Learning_Disabilities,
                                 Parental_Education_Level, Distance_from_Home, Gender]):
            if value is None:
                print(f"Mapping failed for {field} with value '{data[field]}'")
        
        # Ensure test_array is correct before passing it to the model
        test_array = [[Hours_Studied, Attendance, Sleep_Hours, Previous_Scores, Tutoring_Sessions,
                       Physical_Activity, Parental_Involvement, Access_to_Resources,
                       Extracurricular_Activities, Motivation_Level, Internet_Access, Family_Income,
                       Teacher_Quality, School_Type, Peer_Influence, Learning_Disabilities,
                       Parental_Education_Level, Distance_from_Home, Gender]]

        score = linear_model.predict(test_array)[0]
        return score

    except Exception as e:
        print("Error occurred in get_s_score:", e)
        return "Error: " + str(e)
