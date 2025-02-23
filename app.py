
import streamlit as st
import random

# Define quiz questions
quiz_data = {
    "Beginner": [
        {"question": "What is the correct file extension for Python files?", "options": [".py", ".pyt", ".pt", ".python"], "answer": ".py"},
        {"question": "Which keyword is used to define a function in Python?", "options": ["func", "define", "def", "function"], "answer": "def"},
        {"question": "What data type is the result of: 3 + 2.5?", "options": ["int", "float", "str", "bool"], "answer": "float"},
        {"question": "Which of the following is used to take input from the user in Python?", "options": ["input()", "scan()", "read()", "get()"], "answer": "input()"},
        {"question": "What symbol is used for single-line comments in Python?", "options": ["//", "#", "/* */", "--"], "answer": "#"},
        {"question": "What will be the output of `print(type(10))` in Python?", "options": ["int", "float", "str", "bool"], "answer": "int"},
        {"question": "Which of the following is a valid variable name in Python?", "options": ["2var", "my_var", "var-2", "@name"], "answer": "my_var"},
        {"question": "How do you start a for loop in Python?", "options": ["for i = 0; i < 10; i++", "for i in range(10)", "foreach i in range(10)", "loop i in range(10)"], "answer": "for i in range(10)"},
    ],
    "Intermediate": [
        {"question": "Which of these is NOT a valid variable name in Python?", "options": ["my_var", "_var", "2var", "var_2"], "answer": "2var"},
        {"question": "How do you create a list in Python?", "options": ["()", "{}", "[]", "<>"], "answer": "[]"},
        {"question": "What does `len()` function return?", "options": ["Length of an object", "Last element of a list", "Index of an item", "Size of memory"], "answer": "Length of an object"},
        {"question": "What is the output of `range(5)` in Python?", "options": ["[0, 1, 2, 3, 4]", "range(0, 5)", "[0, 1, 2, 3, 4, 5]", "None"], "answer": "range(0, 5)"},
        {"question": "Which operator is used to concatenate strings in Python?", "options": ["+", "-", "*", "&"], "answer": "+"},
    ],
    "Advanced": [
        {"question": "What will `bool([])` return?", "options": ["True", "False", "None", "Error"], "answer": "False"},
        {"question": "Which module is used for regular expressions in Python?", "options": ["regex", "re", "regx", "pyregex"], "answer": "re"},
        {"question": "What is the time complexity of searching in a dictionary?", "options": ["O(1)", "O(n)", "O(log n)", "O(n log n)"], "answer": "O(1)"},
        {"question": "What does the `zip()` function do in Python?", "options": ["Combines two iterables", "Returns the length of an iterable", "Splits a string into a list", "None of the above"], "answer": "Combines two iterables"},
        {"question": "What will be the output of `print(set([1, 1, 2, 2]))`?", "options": ["[1, 2]", "[1, 1, 2, 2]", "[1, 2, 3]", "Error"], "answer": "[1, 2]"},
    ],
}

# App Title
st.title("🧠 Python Programming Quiz")

# Select Quiz Level
category = st.selectbox("Select Difficulty Level", list(quiz_data.keys()))

# Session State for Quiz Progress
if "quiz_index" not in st.session_state:
    st.session_state.quiz_index = 0
    st.session_state.score = 0
    st.session_state.questions = random.sample(quiz_data[category], len(quiz_data[category]))

# Get current question
total_questions = len(st.session_state.questions)
if st.session_state.quiz_index < total_questions:
    q = st.session_state.questions[st.session_state.quiz_index]
    st.subheader(f"Q{st.session_state.quiz_index + 1}: {q['question']}")
    
    selected_option = st.radio("Choose your answer:", q["options"], key=f"q{st.session_state.quiz_index}")
    
    if st.button("Submit Answer"):
        if selected_option == q["answer"]:
            st.success("✅ Correct! Well done.")
            st.session_state.score += 1
        else:
            st.error(f"❌ Incorrect! The correct answer is: {q['answer']}")
        
        st.session_state.quiz_index += 1
        st.rerun()
else:
    st.write(f"🎯 **Your Final Score: {st.session_state.score} / {total_questions}**")
    if st.session_state.score == total_questions:
        st.balloons()
        st.success("🎉 Perfect Score! You are a Python pro!")
    elif st.session_state.score >= total_questions // 2:
        st.info("👍 Good job! Keep practicing.")
    else:
        st.warning("📖 Keep learning! You'll get better.")
    
    if st.button("Restart Quiz"):
        st.session_state.quiz_index = 0
        st.session_state.score = 0
        st.session_state.questions = random.sample(quiz_data[category], len(quiz_data[category]))
        st.rerun()
