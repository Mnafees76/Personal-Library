import streamlit as st
import json
import time  # For delay (animation effect)

# 📚 Function to load the library from a JSON file
def load_library():
    try:
        with open("library.json", "r") as file:
            return json.load(file)
    except FileNotFoundError: 
        return []  # Return an empty list if the file is not found

# 💾 Function to save the library into a JSON file
def save_library():
    with open("library.json", "w") as file:
        json.dump(library, file, indent=4)

# 🏠 Load library data from file
library = load_library()

# 🎯 Main title
st.title("📖 Personal Library Manager")

# 📌 Sidebar menu
menu = st.sidebar.radio("📂 Select an option:", ["📚 View Library", "➕ Add Book", "🗑 Remove Book", "🔍 Search Book", "💾 Save and Exit"])

# 📖 View Library Section
if menu == "📚 View Library":  
    st.sidebar.title("📖 Your Library")
    
    if library:
        for book in library:
            read_status = "✅ Read" if book["read_status"] else "⬜ Not Read"
            st.write(f"📌 **{book['title']}** by {book['author']} ({book['Year']})")
            st.write(f"🎭 Genre: {book['Genre']} | {read_status}")
            st.markdown("---")  # Line separator
    else:
        st.write("❌ No books found!")

# ➕ Add Book Section
elif menu == "➕ Add Book":
    st.sidebar.title("➕ Add a New Book")
    
    title = st.text_input("📌 Title")
    author = st.text_input("✍️ Author")
    Year = st.number_input("📅 Year", min_value=2020, max_value=2100, step=1)
    Genre = st.text_input("🎭 Genre")
    read_status = st.checkbox("Mark as Read")

    if st.button("📥 Add Book"):
        if title and author:
            library.append({"title": title, "author": author, "Year": Year, "Genre": Genre, "read_status": read_status})
            save_library()
            st.success(f"🎉 Book '{title}' added successfully! ✅")
            time.sleep(1.5)  # Delay for a smooth effect
            st.rerun()
        else:
            st.warning("⚠️ Please enter both Title and Author!")

# 🗑 Remove Book Section
elif menu == "🗑 Remove Book":
    st.sidebar.title("🗑 Remove a Book")

    Book_titles = [book["title"] for book in library]  # Get list of book titles

    if Book_titles:
        selected_book = st.selectbox("📌 Select a Book to Remove", Book_titles)
        
        if st.button("❌ Remove Book"):
            library = [book for book in library if book["title"] != selected_book]  # Remove selected book
            save_library()
            st.success(f"🗑 Book '{selected_book}' removed successfully! ✅")
            time.sleep(1.5)  # Delay for a smooth effect
            st.rerun()
    else:
        st.warning("📭 No books in your library. Add some books!")

# 🔍 Search Book Section
elif menu == "🔍 Search Book":
    st.sidebar.title("🔎 Search a Book")
    
    search_term = st.text_input("🔍 Enter Title or Author Name")

    if st.button("🔎 Search"):
        results = [book for book in library if search_term.lower() in book["title"].lower() or search_term.lower() in book["author"].lower()]
        
        if results:
            for book in results:
                read_status = "✅ Read" if book["read_status"] else "⬜ Not Read"
                st.write(f"📌 **{book['title']}** by {book['author']} ({book['Year']})")
                st.write(f"🎭 Genre: {book['Genre']} | {read_status}")
                st.markdown("---")  # Line separator
        else:
            st.warning("🚫 No book found!")

# 💾 Save & Exit Section
elif menu == "💾 Save and Exit":
    save_library()
    st.success("✅ Library saved successfully! 💾")

# 📌 Project Creator's Name
st.markdown("---")
st.markdown("### 👨‍💻 **Project by Muhammad Nafees**")
