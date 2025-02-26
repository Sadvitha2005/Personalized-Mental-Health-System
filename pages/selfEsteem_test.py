import streamlit as st
from menu import menu
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
st.set_page_config(
    page_title="Self Esteem Test",
    page_icon="📝",
    initial_sidebar_state="expanded",
)
def main():
    st.title("📜Self Esteem Test Questionnaire")
    st.write("***Use this questionnaire to explore your Self Esteem. Low Self Esteem can increase the risks of depression and other problems.***")
    questions = {
        "Choose your gender": ["Male", "Female", "Other"],
        "Age": None,  # Will use a number input
        "What is your course?": ["Schooling", "Intermediate/Diploma/B.Sc", "B.Tech", "other"],
        "Your current year of Study": ["Year 1", "Year 2", "Year 3", "Year 4", "Not in above"],
        "On the whole, I am not satisfied with myself.": ["Strongly agree", "Agree", "Disagree", "Strongly Disagree"],
        "At times, I think I am no good at all.": ["Strongly agree", "Agree", "Disagree", "Strongly Disagree"],
        "I feel that I don't have a good number of qualities.": ["Strongly agree", "Agree", "Disagree", "Strongly Disagree"],
        "I am not able to do things as well as most other people.": ["Yes", "No", "Maybe"],
        "I feel I do not have much to be proud of.": ["Strongly agree", "Agree", "Disagree", "Strongly Disagree"],
        "I certainly feel useless at times.": ["Strongly agree", "Agree", "Disagree", "Strongly Disagree"],
        "I feel that I am not a person of worth, at least not even on an equal plane with others.": ["Strongly agree", "Agree", "Disagree", "Strongly Disagree"],
        "I don't like to respect myself": ["Strongly agree", "Agree", "Disagree", "Strongly Disagree"],
        "All in all, I am inclined to think that I am a failure.": ["Strongly agree", "Agree", "Disagree", "Strongly Disagree"],
        "I do not take a positive attitude towards myself.": ["Strongly agree", "Agree", "Disagree", "Strongly Disagree"]
    }
    
    # Thresholds for gender, age, course, and year of study
    gender_thresholds = {"Male": 0.5, "Female": 1, "Other": 0.75}
    age_thresholds = {range(0, 13): 0.5, range(13, 19): 2, range(19, 26): 1.5, range(26, 36): 1, range(36, 41): 1}
    course_thresholds = {"Schooling": 1, "Intermediate/Diploma/B.Sc": 2, "B.Tech": 2, "other": 1}
    year_of_study_thresholds = {"Year 1": 0.25, "Year 2": 0.5, "Year 3": 1, "Year 4": 1.5, "Not in above": 0.1}

    # Function to display options as radio buttons (ensuring only one selection)
    def display_radio_buttons(question, options, key):
        st.write(question)
        selected_option = st.radio("", options, key=key)
        return selected_option

    # Streamlit UI
    st.title("Survey")

    # Dictionary to store user responses
    responses = {}

    # Display inputs for each question
    for i, (question, options) in enumerate(questions.items(), start=1):  # Start enumeration from 1
        if options is None:
            # Use number input for age
            responses[question] = st.number_input(f"**{i}. Enter your age:**", min_value=0, max_value=120, step=1, key=f"age_{i}")
            st.divider()
        else:
            # Use radio buttons for single selection with unique keys
            responses[question] = display_radio_buttons(f"**{i}. {question}**", options, key=f"option_{i}")
            st.divider()

    # Function to save responses to a CSV file
    def save_responses_to_csv(responses, filename="selfEsteemData.csv"):
        # Convert the responses dictionary to a DataFrame
        df = pd.DataFrame([responses])
                
        # Check if the file exists
        if os.path.isfile(filename):
            # Append the new data to the existing file
            df.to_csv(filename, mode='a', header=False, index=False)
        else:
            # Create a new file with the data
            df.to_csv(filename, mode='w', header=True, index=False)
            
    # Function to convert responses to numerical scores
    def map_responses_to_scores(responses):
        response_mapping = {
            "Strongly agree": 4,
            "Agree": 3,
            "Disagree": 2,
            "Strongly Disagree": 1,
            "Yes": 2,
            "No": 0,
            "Maybe": 1
        }
        
        score_labels = [
            "Self-dissatisfaction",
            "Self-Doubt",
            "Lack of Self-Acknowledgment",
            "Self-Comparison",
            "Lack of Self-Pride",
            "Feelings of Uselessness",
            "Worthlessness",
            "Lack of Self-Respect",
            "Self-Perceived Failure",
            "Negative Self-Attitude"
        ]
        
        scores = {
            "Self-dissatisfaction": response_mapping[responses["On the whole, I am not satisfied with myself."]],
            "Self-Doubt": response_mapping[responses["At times, I think I am no good at all."]],
            "Lack of Self-Acknowledgment": response_mapping[responses["I feel that I don't have a good number of qualities."]],
            "Self-Comparison": response_mapping[responses["I am not able to do things as well as most other people."]],
            "Lack of Self-Pride": response_mapping[responses["I feel I do not have much to be proud of."]],
            "Feelings of Uselessness": response_mapping[responses["I certainly feel useless at times."]],
            "Worthlessness": response_mapping[responses["I feel that I am not a person of worth, at least not even on an equal plane with others."]],
            "Lack of Self-Respect": response_mapping[responses["I don't like to respect myself"]],
            "Self-Perceived Failure": response_mapping[responses["All in all, I am inclined to think that I am a failure."]],
            "Negative Self-Attitude": response_mapping[responses["I do not take a positive attitude towards myself."]]
        }

        return scores, score_labels

    # Function to convert responses to numerical scores
    def map_responses_to_scores1(responses):
        response_mapping = {
            "Strongly agree": 4,
            "Agree": 3,
            "Disagree": 2,
            "Strongly Disagree": 1,
            "Yes": 1,
            "No": 0,
            "Maybe": 0.5
        }
        gender_mapping = {"Male": 1, "Female": 2, "Other": 1.5}
        age_mapping = {
            range(0, 13): 1,
            range(13, 19): 4,
            range(19, 26): 3,
            range(26, 36): 2,
            range(36, 41): 2,
        }
        course_mapping = {"Schooling": 2, "Intermediate/Diploma/B.Sc": 3, "B.Tech": 1.5, "other": 2}
        year_mapping = {"Year 1": 0.5, "Year 2": 1, "Year 3": 2, "Year 4": 3, "Not in above": 1}
        
        scores = {
            "Self-dissatisfaction": response_mapping[responses["On the whole, I am not satisfied with myself."]],
            "Self-Doubt": response_mapping[responses["At times, I think I am no good at all."]],
            "Lack of Self-Acknowledgment": response_mapping[responses["I feel that I don't have a good number of qualities."]],
            "Self-Comparison": response_mapping[responses["I am not able to do things as well as most other people."]],
            "Lack of Self-Pride": response_mapping[responses["I feel I do not have much to be proud of."]],
            "Feelings of Uselessness": response_mapping[responses["I certainly feel useless at times."]],
            "Worthlessness": response_mapping[responses["I feel that I am not a person of worth, at least not even on an equal plane with others."]],
            "Lack of Self-Respect": response_mapping[responses["I don't like to respect myself"]],
            "Self-Perceived Failure": response_mapping[responses["All in all, I am inclined to think that I am a failure."]],
            "Negative Self-Attitude": response_mapping[responses["I do not take a positive attitude towards myself."]],
            "Gender": gender_mapping[responses["Choose your gender"]],
            "Age": next(value for key, value in age_mapping.items() if int(responses["Age"]) in key),
            "Course": course_mapping[responses["What is your course?"]],
            "Year of Study": year_mapping[responses["Your current year of Study"]]
        }

        return scores
    
    def plot_averages_for_last_record(filename="selfEsteemData.csv"):
        if os.path.isfile(filename):
            df = pd.read_csv(filename)
            if not df.empty:
                last_record = df.iloc[-1]

                # Convert responses to scores
                scores_dict = map_responses_to_scores1(last_record)
                numerical_scores = list(scores_dict.values())

                # Calculate average numerical score
                avg_numerical_score = sum(numerical_scores) / len(numerical_scores)

                # Calculate average threshold value based on gender, age, course, and year of study
                gender_threshold = gender_thresholds[last_record["Choose your gender"]]
                age_threshold = next(value for key, value in age_thresholds.items() if int(last_record["Age"]) in key)
                course_threshold = course_thresholds[last_record["What is your course?"]]
                year_threshold = year_of_study_thresholds[last_record["Your current year of Study"]]
                avg_threshold = (gender_threshold + age_threshold + course_threshold + year_threshold + 2.5 + 2.5 + 2.5 + 1 + 3 + 2.7 + 3 + 3 + 3 + 3) / 15
                st.subheader("Overall self esteem Analysis")
                # Plotting
                plt.figure(figsize=(10, 6))
                sns.barplot(x=["Average Numerical Score"], y=[avg_numerical_score], color='blue', label='Average Numerical Score')
                plt.axhline(y=avg_threshold, color='red', linestyle='--', label='Average Threshold')
                plt.xlabel('Metrics')
                plt.ylabel('Severity Level')
                plt.title('Average Numerical Score and Threshold')
                plt.legend()
                st.pyplot(plt)

            else:
                st.warning("The CSV file is empty. No records to display.")
        else:
            st.warning("No CSV file found. Please submit responses first.")
    
    def plot_bar_chart(scores, labels, thresholds):
        plt.figure(figsize=(10, 10))
        bar_plot = sns.barplot(x=labels, y=list(scores.values()))
        plt.xlabel('Symptoms')
        plt.ylabel('Severity Level')
        plt.title('Low Self Esteem Symptom Analysis')
        plt.ylim(0, 4)  # Assuming a maximum score of 3
        
        # Plotting the threshold line
        plt.plot(labels, thresholds, color='r', linestyle='--', marker='o', label='Threshold')
        plt.legend()
        plt.xticks(rotation = 90)

        for idx, score in enumerate(scores.values()):
            bar_plot.text(idx, score + 0.1, round(score, 2), color='black', ha="center")

        st.pyplot(plt)
    
    def plot_last_record2(filename="selfEsteemData.csv"):
        if os.path.isfile(filename):
            df = pd.read_csv(filename)
            if not df.empty:
                last_record = df.iloc[-1]
                scores, labels = map_responses_to_scores(last_record)
                thresholds = [2.5, 2.5, 2.5, 1, 3, 2.7, 3, 3, 3, 3]
                st.subheader("Symptom Analysis")
                plot_bar_chart(scores, labels, thresholds)
                # Count the number of symptoms exceeding their thresholds
                num_exceeding = sum(score >= threshold for score, threshold in zip(scores.values(), thresholds))
                
                # Provide feedback based on the count
                if num_exceeding < 3:
                    st.success("You have High self-Esteem and don't need to worry.")
                elif 3 <= num_exceeding < 6:
                    st.warning("You have Average self-Esteem and There is further room for improvement.")
                else:
                    st.error("You show signs of Low self-Esteem. It's strongly recommended to focus on improving your self-esteem")
            else:
                st.warning("The CSV file is empty. No records to display.")
        else:
            st.warning("No CSV file found. Please submit responses first.")
            
    # Function to read the last record from the CSV file and plot a chart
    def plot_last_record1(filename="selfEsteemData.csv"):
        if os.path.isfile(filename):
            df = pd.read_csv(filename)
            if not df.empty:
                last_record = df.iloc[-1]
                st.subheader("Your Responses")
                st.write(last_record)

                # Assuming a simple mapping of responses to numerical values for plotting
                response_mapping = {
                    "Male": 1,
                    "Female": 2,
                    "other": 0.5,
                    "Schooling": 2,
                    "Intermediate/Diploma/B.Sc": 3,
                    "B.Tech": 1.5,
                    "Year 1": 0.5,
                    "Year 2": 1,
                    "Year 3": 2,
                    "Year 4": 3,
                    "Not in above": 1,
                    "Strongly agree": 4,
                    "Agree": 3,
                    "Disagree": 2,
                    "Strongly Disagree": 1,
                    "Yes": 1,
                    "No": 0,
                    "Maybe": 0.5
                }
                # Mapping age to scores
                age_mapping = {
                    range(0, 13): 1,
                    range(13, 19): 4,
                    range(19, 26): 3,
                    range(26, 36): 2,
                    range(36, 41): 2,
                }

                def map_age_to_score(age):
                    for age_range, score in age_mapping.items():
                        if age in age_range:
                            return score
                    return 0  # Default if age doesn't match any range

                plot_data = last_record.replace(response_mapping)
                plot_data["Age"] = map_age_to_score(last_record["Age"])
                st.subheader("Your Response Scores")
                st.bar_chart(plot_data)
            else:
                st.warning("The CSV file is empty. No records to display.")
        else:
            st.warning("No CSV file found. Please submit responses first.")
            
    def plot_averages_for_all_records(filename="selfEsteemData.csv"):
        if os.path.isfile(filename):
            df = pd.read_csv(filename)
            if not df.empty:
                # Convert responses to numerical scores for all records
                numerical_scores = []
                for index, row in df.iterrows():
                    scores_dict = map_responses_to_scores1(row)
                    numerical_score = sum(scores_dict.values()) / len(scores_dict)
                    numerical_scores.append(numerical_score)

                avg_gender_threshold = np.mean(list(gender_thresholds.values()))
                avg_age_threshold = np.mean(list(age_thresholds.values()))
                avg_course_threshold = np.mean(list(course_thresholds.values()))
                avg_year_threshold = np.mean(list(year_of_study_thresholds.values()))

                # Calculate average threshold
                avg_threshold = ((avg_gender_threshold + avg_age_threshold + avg_course_threshold + avg_year_threshold + 2.5 + 1 + 2 + 2 + 2 + 1 + 2 + 1 + 1) / 13)

                # Count records with numerical score >= threshold
                count_depressed = sum(score >= avg_threshold for score in numerical_scores)

                # Calculate average of numerical scores for the considered records
                avg_numerical_scores = sum(score for score in numerical_scores if score >= avg_threshold) / count_depressed

                # Grouping the records by course and calculating the percentage of depressed students
                course_wise_percentage = df.groupby('What is your course?').apply(lambda x: (x.apply(lambda row: sum(map_responses_to_scores1(row).values()) / len(map_responses_to_scores1(row)), axis=1) >= avg_threshold).mean() *10)

                # Plot the results
                plt.figure(figsize=(10, 6))
                sns.barplot(x=course_wise_percentage.index, y=course_wise_percentage.values, color='blue')
                plt.axhline(y=avg_numerical_scores, color='red', linestyle='--', label='Average Numerical Score')
                plt.xlabel('Course')
                plt.ylabel('Percentage of Students with Low Self-Esteem')
                plt.title('Course-wise Percentage of Students with Low Self-Esteem')
                plt.legend()
                plt.xticks(rotation=45)
                plt.tight_layout()
                st.pyplot(plt)

            else:
                st.warning("The CSV file is empty. No records to display.")
        else:
            st.warning("No CSV file found. Please submit responses first.")
            
    def plot_all_records(filename="depressionData.csv"):
        if os.path.isfile(filename):
            df = pd.read_csv(filename)
            if not df.empty:
                # Define response mapping
                response_mapping = {
                    "Male": 20,
                    "Female": 30,
                    "Other": 10,
                    "Schooling": 20,
                    "Intermediate/Diploma/B.Sc": 30,
                    "B.Tech": 15,
                    "Year 1": 5,
                    "Year 2": 10,
                    "Year 3": 20,
                    "Year 4": 30,
                    "Not in above": 10,
                    "Not at all": 0,
                    "Several days": 10,
                    "More than half the days": 20,
                    "Nearly every day": 30,
                    "Yes": 10,
                    "No": 0,
                    "Maybe": 5
                }
                
                # Define age mapping
                age_mapping = {
                    range(0, 13): 10,
                    range(13, 19): 40,
                    range(19, 26): 30,
                    range(26, 36): 20,
                    range(36, 41): 20,
                }

                def map_age_to_score(age):
                    for age_range, score in age_mapping.items():
                        if age in age_range:
                            return score
                    return 0  # Default if age doesn't match any range
                
                # Apply mapping to all records
                plot_data = df.replace(response_mapping)
                plot_data["Age"] = df["Age"].apply(map_age_to_score)
                # st.subheader("Line Chart for the responses received so far!")
                # Display plot
                # st.line_chart(plot_data)
                st.subheader("Scatter Chart for the responses received so far!")
                st.scatter_chart(plot_data)
            else:
                st.warning("The CSV file is empty. No records to display.")
        else:
            st.warning("No CSV file found. Please submit responses first.")
    
    # Save the responses to the CSV file when the user submits
    if st.button("Submit"):
        save_responses_to_csv(responses)
        st.success("Responses saved successfully!")
        st.session_state.show_tabs = True
    if st.session_state.show_tabs:
        # Display tabs
        tab1, tab2 = st.tabs(["Test Analysis Report", "Check out other statistics"])
    
        with tab1:
            st.title("Analysis of your self-Esteem Test Results:")
            plot_last_record1()
            plot_last_record2()
            plot_averages_for_last_record()
            
        with tab2:
            st.title("All Responses Analysis")
            st.subheader("Course-wise Low self-Esteem Analysis")
            plot_averages_for_all_records()
            plot_all_records()

if __name__ == "__main__":
    menu()
    st.session_state.show_tabs = False
    main()
