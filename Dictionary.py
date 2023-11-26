import json
import tkinter as tk
from tkinter import ttk, simpledialog, messagebox


def save_to_file(dictionary):
    with open("dictionary.json", "w", encoding="utf-8") as file:
        json.dump(dictionary, file)


def load_from_file():
    try:
        with open("dictionary.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def update_listbox(listbox, dictionary):
    listbox.delete(0, tk.END)
    for english in sorted(dictionary.keys()):
        listbox.insert(tk.END, english)


def add_word(dictionary, listbox, window):
    english = simpledialog.askstring("Input", "Enter English word:", parent=window)
    if english:
        thai = simpledialog.askstring("Input", "Enter Thai translation:", parent=window)
        part_of_speech = simpledialog.askstring("Input", "Enter part of speech:", parent=window)
        dictionary[english] = [thai, part_of_speech]
        save_to_file(dictionary)
        update_listbox(listbox, dictionary)
        messagebox.showinfo("Info", "Added successfully!")


def search(dictionary, listbox, search_entry):
    search_query = search_entry.get().strip()
    if search_query in dictionary:
        thai, part_of_speech = dictionary[search_query]
        messagebox.showinfo("Word Info", f"English: {search_query}\nThai: {thai}\nPart of Speech: {part_of_speech}")
    else:
        messagebox.showinfo("Info", f"Word '{search_query}' not found.")


def update_word(dictionary, listbox, window):
    english = simpledialog.askstring("Input", "Enter English word to update:", parent=window)
    if english and english in dictionary:
        thai = simpledialog.askstring("Input", "Enter new Thai translation:", parent=window)
        part_of_speech = simpledialog.askstring("Input", "Enter new part of speech:", parent=window)
        dictionary[english] = [thai, part_of_speech]
        save_to_file(dictionary)
        update_listbox(listbox, dictionary)
        messagebox.showinfo("Info", "Updated successfully!")
    else:
        messagebox.showinfo("Info", "Word not found!")


def delete_word(dictionary, listbox, window):
    english = simpledialog.askstring("Input", "Enter English word to delete:", parent=window)
    if english and english in dictionary:
        del dictionary[english]
        save_to_file(dictionary)
        update_listbox(listbox, dictionary)
        messagebox.showinfo("Info", "Deleted successfully!")
    else:
        messagebox.showinfo("Info", "Word not found!")


def next_word(listbox):
    if listbox.size() > 0:
        current_selection = listbox.curselection()
        if current_selection:
            listbox.select_clear(current_selection)
            listbox.select_set(current_selection[0] + 1)
        else:
            listbox.select_set(0)


def previous_word(listbox):
    if listbox.size() > 0:
        current_selection = listbox.curselection()
        if current_selection:
            listbox.select_clear(current_selection)
            listbox.select_set(max(current_selection[0] - 1, 0))
        else:
            listbox.select_set(listbox.size() - 1)


def display_word_info(dictionary, listbox):
    selected_index = listbox.curselection()
    if selected_index:
        selected_word = listbox.get(selected_index[0])
        thai, part_of_speech = dictionary[selected_word]
        messagebox.showinfo("Word Info", f"English: {selected_word}\nThai: {thai}\nPart of Speech: {part_of_speech}")
    else:
        messagebox.showinfo("Info", "Please select a word.")


def on_double_click(event, dictionary, listbox):
    display_word_info(dictionary, listbox)


def main():
    dictionary = load_from_file()
    window = tk.Tk()
    window.title("Dictionary App")
    window.geometry("540x300")

    listbox = tk.Listbox(window)
    listbox.pack(padx=2, pady=2, fill=tk.BOTH, expand=True)
    listbox.bind("<Double-1>", lambda event: on_double_click(event, dictionary, listbox))
    update_listbox(listbox, dictionary)

    search_frame = ttk.Frame(window)
    search_frame.pack(fill=tk.X, pady=1)

    search_entry = ttk.Entry(search_frame)
    search_entry.pack(side=tk.LEFT, padx=1, expand=True)

    ttk.Button(search_frame, text="Search", command=lambda: search(dictionary, listbox, search_entry)).pack(
        side=tk.LEFT)

    button_frame = ttk.Frame(window)
    button_frame.pack(fill=tk.X)

    ttk.Button(button_frame, text="Add", command=lambda: add_word(dictionary, listbox, window)).pack(side=tk.LEFT, expand=True)
    ttk.Button(button_frame, text="Edit", command=lambda: update_word(dictionary, listbox, window)).pack(side=tk.LEFT, expand=True)
    ttk.Button(button_frame, text="Delete", command=lambda: delete_word(dictionary, listbox, window)).pack(side=tk.LEFT, expand=True)
    ttk.Button(button_frame, text="Previous", command=lambda: previous_word(listbox)).pack(side=tk.LEFT, expand=True)
    ttk.Button(button_frame, text="Show Word", command=lambda: display_word_info(dictionary, listbox)).pack(side=tk.LEFT, expand=True)
    ttk.Button(button_frame, text="Next", command=lambda: next_word(listbox)).pack(side=tk.LEFT, expand=True)
    ttk.Button(button_frame, text="Exit", command=window.quit).pack(side=tk.LEFT, expand=True)

    window.mainloop()


if __name__ == "__main__":
    main()
