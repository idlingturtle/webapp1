import streamlit as st
from modules import functions

todolist = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todolist.append(todo)
    functions.write_todos(todolist)


st.title("ToDos in web space!")
st.subheader("Do these eventually.")

st.divider()

for index, todo in enumerate(todolist):
    checkbox = st.checkbox(todo.capitalize(), key=todo)
    if checkbox:
        todolist.pop(index)
        functions.write_todos(todolist)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label=" ", autocomplete="", placeholder="Add a ToDo...",
              on_change=add_todo, key='new_todo')
